# -*- coding: utf-8 -*-
"""Генератор слоёв анимации титула по пикселям cover.png + разметке
   «Какие элементы выделить -титул.svg»:
   twinkle, орбитеры вихря, треки гребней, ЛУЧИ звезды, доп. линии волн.
   Патчит движок в presentation/index.html."""
import io, json, math, random, re
from PIL import Image

random.seed(42)
im = Image.open(r'presentation/assets/img/bg/cover.png').convert('RGB')
W, H = im.size
px = im.load()
CX, CY, AR = 1749, 363, 0.42          # центр звезды — ТОЧКА из разметки пользователя
R_VORTEX = 640

def bright(x, y):
    r, g, b = px[x, y]
    return max(r, g, b)

def vdist(x, y):
    return math.hypot(x - CX, (y - CY) / AR)

# ── разметка: лучи (line) и доп. волновые линии (path) ──
ann = io.open(r'presentation/assets/img/objects/Какие элементы выделить.svg',
              encoding='utf-8').read()
rays = []
for m in re.finditer(r'<line x1="([\d.]+)" y1="([\d.]+)" x2="([\d.]+)" y2="([\d.]+)"', ann):
    x1, y1, x2, y2 = (float(v) for v in m.groups())
    # луч всегда ОТ центра наружу: ближний к центру конец — старт
    if math.hypot(x1-CX, y1-CY) > math.hypot(x2-CX, y2-CY):
        x1, y1, x2, y2 = x2, y2, x1, y1
    rays.append([round(x1), round(y1), round(x2), round(y2)])

extra_paths = []
for m in re.finditer(r'<path d="(M[^"]+)" stroke="#FF00E6"', ann):
    nums = [float(n) for n in re.findall(r'-?\d+\.?\d*', m.group(1))]
    pts = [(nums[i], nums[i+1]) for i in range(0, len(nums)-1, 2)]
    if len(pts) >= 3:
        extra_paths.append(pts)

# ── бусины-звёзды (circle/ellipse в разметке), кроме маркера центра звезды ──
beads = []
for m in re.finditer(r'<circle cx="([\d.]+)" cy="([\d.]+)" r="([\d.]+)"', ann):
    x, y, r = float(m.group(1)), float(m.group(2)), float(m.group(3))
    if abs(x - CX) < 3 and abs(y - CY) < 3:
        continue                                 # это маркер центра звезды — пропустить
    beads.append([round(x), round(y), round(r)])
for m in re.finditer(r'<ellipse cx="([\d.]+)" cy="([\d.]+)" rx="([\d.]+)" ry="([\d.]+)"', ann):
    x, y, rx, ry = (float(g) for g in m.groups())
    beads.append([round(x), round(y), round((rx + ry) / 2)])

def near_ray(x, y, tol=16):
    """точка близко к какому-либо лучу? (расстояние до отрезка < tol) —
       чтобы мерцающие точки НЕ ложились на линии лучей (не мигали вдоль них)"""
    for x1, y1, x2, y2 in rays:
        vx, vy = x2 - x1, y2 - y1
        L2 = vx * vx + vy * vy
        if L2 < 1e-6:
            continue
        tt = ((x - x1) * vx + (y - y1) * vy) / L2
        tt = max(0.0, min(1.0, tt))
        px, py = x1 + vx * tt, y1 + vy * tt
        if math.hypot(x - px, y - py) < tol:
            return True
    return False

def resample(pts, ds):
    """полилиния → точки с равным шагом ds"""
    out = [list(pts[0])]
    ax, ay = pts[0]; acc = 0.0
    for bx, by in pts[1:]:
        dx, dy = bx-ax, by-ay
        L = math.hypot(dx, dy)
        if L < 1e-6:
            continue
        dx, dy = dx/L, dy/L
        d = ds - acc
        while d <= L:
            out.append([round(ax+dx*d), round(ay+dy*d)])
            d += ds
        acc = L - (d - ds); ax, ay = bx, by
    return out

# ── 1) TWINKLE ──
tw = []
for _ in range(9000):
    x = random.randrange(4, W-4); y = random.randrange(4, H-4)
    v = bright(x, y)
    if v > 120 and vdist(x, y) > 70 and not near_ray(x, y, 40):
        tw.append([x, y, v])
random.shuffle(tw); tw = tw[:700]

# ── 2) ОРБИТЕРЫ вихря ──
orb = []
for _ in range(30000):
    x = random.randrange(4, W-4); y = random.randrange(4, H-4)
    d = vdist(x, y)
    if 60 < d < R_VORTEX and bright(x, y) > 100 and not near_ray(x, y, 40):
        ang = math.atan2((y-CY)/AR, x-CX)
        orb.append([round(d), round(ang*100), bright(x, y)])
random.shuffle(orb); orb = orb[:800]

# ── 3) ТРЕКИ ГРЕБНЕЙ (walk по яркости) + доп. линии из разметки ──
tracks = []
attempts = 0
while len(tracks) < 70 and attempts < 4000:
    attempts += 1
    x = random.randrange(10, 1420); y = random.randrange(120, H-10)
    if bright(x, y) < 150 or vdist(x, y) < R_VORTEX*0.85:
        continue
    pts = [(x, y)]
    for _ in range(random.randrange(50, 130)):
        best, bx, by = -1, None, None
        for dy in (-3, -2, -1, 0, 1, 2, 3):
            nx, ny = x+4, y+dy
            if nx >= W-5 or ny < 5 or ny >= H-5:
                continue
            v = bright(nx, ny)
            if v > best:
                best, bx, by = v, nx, ny
        if best < 90 or bx is None:
            break
        x, y = bx, by
        pts.append((x, y))
    if len(pts) >= 30:
        tracks.append([[p[0], p[1]] for p in pts[::2]])
# доп. волновые линии из разметки — тем же стилем (шаг 8 = как прореженный walk)
for pts in extra_paths:
    tracks.append(resample(pts, 8))

data = ('const TW='+json.dumps(tw, separators=(',', ':')) +
        ';\nconst ORB='+json.dumps(orb, separators=(',', ':')) +
        ';\nconst TRK='+json.dumps(tracks, separators=(',', ':')) +
        ';\nconst RAYS='+json.dumps(rays, separators=(',', ':')) +
        ';\nconst BEADS='+json.dumps(beads, separators=(',', ':')) + ';')
print('tw:', len(tw), 'orb:', len(orb), 'tracks:', len(tracks),
      'rays:', len(rays), 'beads:', len(beads), 'data:', len(data), 'bytes')

ENGINE = r"""(function(){
  const W=2172,H=724; waveCv.width=W; waveCv.height=H;
  const ctx=waveCv.getContext('2d');
  const CX=1749, CY=363, AR=0.42;              // центр звезды (точка из разметки) и наклон вихря
  /* ═══ КОНФИГ ЧАСТИЦ — размеры/количество/цвет/стиль крутить ЗДЕСЬ ═══ */
  const CFG={
    twinkle:{size:[3.3,7.8], alpha:0.8, speed:[0.5,2.3]},        // МЕРЦАНИЕ точек фона
    orbit:  {size:[2.7,6.6], alpha:0.62, speed:1.0},             // ЧАСТИЦЫ ВОКРУГ ЗВЕЗДЫ
    circles:{radii:[150,270,400,540], dot:4.6, gap:15, alpha:0.9, speed:0.5, pulse:0.5},  // КРУГИ: пунктир из светящихся бусин + бегущий пульс, по часовой
    waves:  {size:5.2, tail:10, alpha:0.6, speed:0.5},           // ЛИНИИ ВОЛНЫ (светлячки; размер ÷1.5, скорость ÷2)
    rays:   {coreW:1.5, alpha:0.7, spread:30, dots:0.6, dotSize:2.2, glowSpeed:1.6, glowAmt:0.85},  // ЛУЧИ: рассеивание + пульс цвета от текущего к неону
    star:   {base:0.22, amp:0.045},                              // ЦЕНТР ЗВЕЗДЫ (ровный, слабый пульс)
    sparks: {rate:7, size:5.1}                                   // ИСКРЫ ВВЕРХ от звезды
  };
  /* стиль частиц: круглая точка с мягким свечением (спрайты 3 цветов) */
  function mkSpr(color){ const c=document.createElement('canvas'); c.width=c.height=32;
    const g=c.getContext('2d'); const gr=g.createRadialGradient(16,16,0,16,16,16);
    gr.addColorStop(0,'rgba(255,255,255,1)'); gr.addColorStop(0.28,color); gr.addColorStop(1,'rgba(0,0,0,0)');
    g.fillStyle=gr; g.fillRect(0,0,32,32); return c; }
  const SPR={ deep:mkSpr('rgba(90,150,245,0.55)'),          // глубокий синий
              cyan:mkSpr('rgba(140,210,255,0.6)'),          // циан
              white:mkSpr('rgba(225,242,255,0.72)'),        // почти белый
              blue:mkSpr('rgba(52,118,255,0.95)'),          // НАСЫЩЕННЫЙ синий
              bluehead:mkSpr('rgba(120,180,255,0.95)') };   // яркая голова линий
  /* спрайт-пульс: БЕЛОЕ ядро + неон-синий контур (свет, бегущий по линии) */
  (function(){ const c=document.createElement('canvas'); c.width=c.height=32;
    const g=c.getContext('2d'); const gr=g.createRadialGradient(16,16,0,16,16,16);
    gr.addColorStop(0,'rgba(255,255,255,1)'); gr.addColorStop(0.20,'rgba(235,246,255,0.95)');
    gr.addColorStop(0.42,'rgba(48,120,255,0.9)'); gr.addColorStop(0.75,'rgba(40,110,255,0.35)');
    gr.addColorStop(1,'rgba(0,0,0,0)'); g.fillStyle=gr; g.fillRect(0,0,32,32); SPR.core=c; })();
  /* спрайт-бусина: белое ядро + ЯРКИЙ неон-синий контур (для кругов) */
  (function(){ const c=document.createElement('canvas'); c.width=c.height=32;
    const g=c.getContext('2d'); const gr=g.createRadialGradient(16,16,0,16,16,16);
    gr.addColorStop(0,'rgba(255,255,255,1)'); gr.addColorStop(0.14,'rgba(240,248,255,0.98)');
    gr.addColorStop(0.30,'rgba(70,150,255,1)'); gr.addColorStop(0.50,'rgba(40,110,255,0.85)');
    gr.addColorStop(0.72,'rgba(30,90,255,0.4)'); gr.addColorStop(1,'rgba(0,0,0,0)');
    g.fillStyle=gr; g.fillRect(0,0,32,32); SPR.bead=c; })();
  const NEON='rgba(40,120,255,';                            // неон-синий контур линий
  function dot(spr,x,y,s,al){ ctx.globalAlpha=Math.min(1,al); ctx.drawImage(spr,x-s,y-s,s*2,s*2); }
""" + data + r"""
  /* twinkle: параметры мерцания каждой точки */
  const tws=TW.map(p=>({x:p[0],y:p[1],v:p[2]/255, ph:Math.random()*6.28, sp:CFG.twinkle.speed[0]+Math.random()*(CFG.twinkle.speed[1]-CFG.twinkle.speed[0]), s:CFG.twinkle.size[0]+Math.random()*(CFG.twinkle.size[1]-CFG.twinkle.size[0])}));
  /* орбитеры вихря: вращение вокруг звезды (ближе к центру — быстрее) */
  const orbs=ORB.map(p=>({r:p[0], a:p[1]/100, v:p[2]/255, w:(0.04+0.22*(1-p[0]/640))*CFG.orbit.speed, ph:Math.random()*6.28, s:CFG.orbit.size[0]+Math.random()*(CFG.orbit.size[1]-CFG.orbit.size[0])}));
  /* светлячки по гребням и доп. линиям волн */
  const RUNNERS=84;
  const runners=[];
  function respawn(r){ r.tr=TRK[(Math.random()*TRK.length)|0]; r.pos=Math.random()*3; r.sp=(14+Math.random()*26); }
  for(let i=0;i<RUNNERS;i++){ const r={}; respawn(r); r.pos=Math.random()*r.tr.length; runners.push(r); }
  /* ЛУЧИ звезды: мягкое ядро без контура + ОБЛАКО рассеивания (точки с разбросом,
     растущим к концу луча) */
  const rayruns=RAYS.map(rr=>{
    const L=Math.hypot(rr[2]-rr[0], rr[3]-rr[1]);
    const M=Math.max(10, Math.round(L*CFG.rays.dots/10));       // сколько точек рассеивания
    const scat=[]; for(let i=0;i<M;i++) scat.push({
      q:Math.random(), off:(Math.random()*2-1)*Math.sign(Math.random()-0.5||1),
      s:0.7+Math.random()*1.4, tw:Math.random()*6.283, sp:0.8+Math.random()*1.6});
    return {x1:rr[0],y1:rr[1],x2:rr[2],y2:rr[3],L, scat, ph:Math.random()*6.283};
  });
  /* КРУГИ: бусины с РАЗНЫМ шагом/размером/яркостью; пульс бежит ПО ЧАСОВОЙ */
  const cMaxR=CFG.circles.radii[CFG.circles.radii.length-1];
  const circruns=CFG.circles.radii.map((r,i)=>{
    const perim=6.283*r*(1+AR)/2;
    const n=Math.max(24,Math.round(perim/CFG.circles.gap));
    const beads=[]; let ang=0;
    for(let j=0;j<n*2 && ang<6.283;j++){
      beads.push({an:ang, sz:0.55+Math.random()*1.0, br:0.45+Math.random()*0.95, tw:Math.random()*6.28});
      ang += (6.283/n)*(0.55+Math.random()*1.1);   // РАЗНЫЙ шаг между бусинами
    }
    return {r, a:Math.random()*6.283, w:CFG.circles.speed*(1+(i%2? .15 : -.1)), beads};
  });

  /* ОДНА бусина-звезда: белый центр + неон-контур + лучики-крест; k = общий множитель прозрачности */
  function drawStar(x,y,r,pulse,k){
    ctx.globalAlpha=1;
    const L=r*(4.0+4.0*pulse);
    for(const [ux,uy] of [[1,0],[-1,0],[0,1],[0,-1]]){
      const g=ctx.createLinearGradient(x,y,x+ux*L,y+uy*L);
      g.addColorStop(0,'rgba(225,242,255,'+((0.7*pulse+0.15)*k).toFixed(3)+')');
      g.addColorStop(1,'rgba(40,120,255,0)');
      ctx.strokeStyle=g; ctx.lineWidth=1.2;
      ctx.beginPath(); ctx.moveTo(x,y); ctx.lineTo(x+ux*L,y+uy*L); ctx.stroke();
    }
    const L2=L*0.5;
    for(const [ux,uy] of [[.71,.71],[-.71,.71],[.71,-.71],[-.71,-.71]]){
      const g=ctx.createLinearGradient(x,y,x+ux*L2,y+uy*L2);
      g.addColorStop(0,'rgba(120,190,255,'+((0.4*pulse)*k).toFixed(3)+')'); g.addColorStop(1,'rgba(40,120,255,0)');
      ctx.strokeStyle=g; ctx.lineWidth=1;
      ctx.beginPath(); ctx.moveTo(x,y); ctx.lineTo(x+ux*L2,y+uy*L2); ctx.stroke();
    }
    dot(SPR.bead, x, y, r*(1.5+0.8*pulse), (0.55+0.45*pulse)*k);
  }
  /* СТАТИЧНЫЕ бусины-звёзды (по разметке) */
  const sbeads=BEADS.map(p=>({x:p[0],y:p[1],r:Math.max(2,p[2]), ph:Math.random()*6.283, sp:1.0+Math.random()*2.0}));
  /* ВСПЛЫВАЮЩИЕ бусины-звёзды: рождаются, плывут вверх, исчезают */
  const FLO_MAX=16;
  const floaters=[];
  function spawnFloater(){
    return {x:60+Math.random()*(W-120), y:H*(0.55+Math.random()*0.5),
      r:2+Math.random()*2.5, ph:Math.random()*6.283, sp:1.0+Math.random()*2.0,
      vy:14+Math.random()*22, life:0, max:3.0+Math.random()*3.0};
  }
  function drawBeads(t,dt){
    ctx.lineCap='round';
    // статичные
    for(const b of sbeads) drawStar(b.x,b.y,b.r,0.5+0.5*Math.sin(t*b.sp+b.ph),1);
    // всплывающие: пополнять пул
    if(floaters.length<FLO_MAX && Math.random()<dt*4) floaters.push(spawnFloater());
    for(let i=floaters.length-1;i>=0;i--){
      const f=floaters[i]; f.life+=dt; f.y-=f.vy*dt;
      if(f.life>=f.max || f.y<-20){ floaters.splice(i,1); continue; }
      const p=f.life/f.max;
      const env=Math.min(1,p/0.15)*(1-Math.max(0,(p-0.7)/0.3));   // плавное появление → затухание
      drawStar(f.x,f.y,f.r,0.5+0.5*Math.sin(t*f.sp+f.ph),env);
    }
  }
  function render(t,dt){
    ctx.clearRect(0,0,W,H);                     // фон-картинка в CSS — canvas прозрачный
    ctx.globalCompositeOperation='lighter';
    /* ── мерцание частиц картинки: цвет по яркости (синий→циан→белый) ── */
    for(const p of tws){
      const a=Math.max(0,Math.sin(t*p.sp+p.ph));
      const al=CFG.twinkle.alpha*p.v*a*a;
      if(al<0.03) continue;
      const spr=p.v>0.8?SPR.white:(p.v>0.5?SPR.cyan:SPR.deep);
      dot(spr,p.x,p.y,p.s,al);
    }
    /* ── вращение вихря: орбитеры ── */
    for(const o of orbs){
      o.a+=o.w*dt;
      const x=CX+Math.cos(o.a)*o.r, y=CY+Math.sin(o.a)*o.r*AR;
      if(x<0||x>W||y<0||y>H) continue;
      const al=CFG.orbit.alpha*(0.3+0.7*o.v)*(0.55+0.45*Math.sin(t*1.3+o.ph));
      dot(o.v>0.7?SPR.cyan:SPR.deep,x,y,o.s,al);
    }
    /* ── КРУГИ ОТ ЗВЕЗДЫ: бусины с разным шагом/размером/яркостью (белое ядро +
          неон-контур), по кольцу ПО ЧАСОВОЙ бежит пульс. Дальше — бледнее/светлее ── */
    const pulseSpan=CFG.circles.pulse*6.283;
    for(const c of circruns){
      c.a+=c.w*dt;                                  // угол пульса растёт = по часовой
      const near=1-c.r/cMaxR;                       // 0 дальний … 1 ближний к звезде
      const bri=0.32+0.85*near;                     // ближе — ярче; дальше — тусклее/светлее
      for(const b of c.beads){
        const x=CX+Math.cos(b.an)*c.r, y=CY+Math.sin(b.an)*c.r*AR;
        if(x<-6||x>W+6||y<-6||y>H+6) continue;
        let g=0.42;                                 // базовое свечение бусины
        let d=(c.a-b.an)%6.283; if(d<0)d+=6.283;    // насколько бусина ПОЗАДИ головы пульса
        if(d<pulseSpan) g=1-(d/pulseSpan)*0.62;     // возле головы — ярче (пульс)
        const tw=0.82+0.18*Math.sin(t*2+b.tw);      // лёгкое мерцание
        const al=CFG.circles.alpha*bri*b.br*(0.30+0.70*g)*tw;
        if(al<0.03) continue;
        const sz=CFG.circles.dot*b.sz*(0.7+0.5*near)*(0.82+0.4*g);
        dot(SPR.bead,x,y,sz,al);
      }
    }
    /* ── светлячки по гребням волн и доп. линиям (голова + хвост) ── */
    for(const r of runners){
      r.pos+=r.sp*dt/2*CFG.waves.speed;
      if(r.pos>=r.tr.length-1){ respawn(r); continue; }
      for(let k=0;k<CFG.waves.tail;k++){
        const i=Math.floor(r.pos)-k;
        if(i<0) break;
        const p=r.tr[i], al=CFG.waves.alpha*(1-k/CFG.waves.tail);
        dot(k===0?SPR.white:SPR.cyan,p[0],p[1],k===0?CFG.waves.size:CFG.waves.size*0.62,al);
      }
    }
    /* ── ЛУЧИ ЗВЕЗДЫ: неоновый луч света, СВЕТИТ ВСЕГДА; по нему проходит
          МЯГКАЯ плавная волна яркости (как солнечный луч, без «выстрелов») ── */
    ctx.lineCap='round';
    for(const r of rayruns){
      const dx=r.x2-r.x1, dy=r.y2-r.y1;
      const nx=-dy/r.L, ny=dx/r.L;                            // нормаль (перпендикуляр) к лучу
      // 1) мягкое ядро линии БЕЗ контура; ПУЛЬС свечения: цвет дышит от текущего к неону
      ctx.globalAlpha=1; ctx.shadowBlur=0;                    // сброс — иначе stroke берёт alpha от dot()
      const glow=(0.5+0.5*Math.sin(t*CFG.rays.glowSpeed+r.ph))*CFG.rays.glowAmt;  // 0..glowAmt
      const SEGC=20;
      for(let s=0;s<SEGC;s++){
        const a0=s/SEGC, a1=(s+1)/SEGC, m=(a0+a1)/2;
        const fade=1-m*0.7;                                   // к концу тускнеет
        const al=CFG.rays.alpha*fade;
        if(al<0.02) continue;
        const k=1-m*0.35;                                     // у центра светлее, к концу насыщеннее
        // базовый цвет — уже неоново-синий; по фазе glow уходит в ЧИСТЫЙ неон (30,110,255)
        const bR=70+70*k, bG=140+70*k;                        // база: сине-неоновая
        const R=bR+(30-bR)*glow, G=bG+(110-bG)*glow;
        ctx.strokeStyle='rgba('+(R|0)+','+(G|0)+',255,'+al.toFixed(3)+')';
        ctx.lineWidth=CFG.rays.coreW;
        ctx.beginPath(); ctx.moveTo(r.x1+dx*a0,r.y1+dy*a0); ctx.lineTo(r.x1+dx*a1,r.y1+dy*a1); ctx.stroke();
      }
      // 2) РАССЕИВАНИЕ: точки с разбросом по нормали, разброс РАСТЁТ к концу луча
      for(const p of r.scat){
        const q=p.q;
        const off=p.off*CFG.rays.spread*q;                    // к концу — шире разброс
        const x=r.x1+dx*q+nx*off, y=r.y1+dy*q+ny*off;
        const tw=0.55+0.45*Math.sin(t*p.sp+p.tw);             // мягкое мерцание точки
        const al=CFG.rays.alpha*(1-q*0.35)*(1-Math.abs(p.off)*0.5)*tw*0.7;
        if(al<0.03) continue;
        dot(SPR.deep,x,y,CFG.rays.dotSize*p.s,al);
      }
    }
    ctx.globalAlpha=1;
    drawBeads(t,dt);                             // бусины-звёзды: статичные + всплывающие
    /* ── пульс звезды ── */
    const pu=CFG.star.base+CFG.star.amp*Math.sin(t*1.8)+CFG.star.amp*0.5*Math.sin(t*4.7);
    const g=ctx.createRadialGradient(CX,CY,0,CX,CY,H*0.30);
    g.addColorStop(0,'rgba(235,248,255,'+(pu*1.15).toFixed(3)+')');   // мягче — не засвечивает лучи
    g.addColorStop(.28,'rgba(120,185,250,'+(pu*0.5).toFixed(3)+')');
    g.addColorStop(1,'rgba(40,90,180,0)');
    ctx.fillStyle=g; ctx.beginPath(); ctx.arc(CX,CY,H*0.34,0,6.283); ctx.fill();
    ctx.globalAlpha=1;
    ctx.globalCompositeOperation='source-over';
  }
  let last=null,tt=0;
  function frame(ts){
    if(!ccRunning) return;
    if(last===null)last=ts; const dt=Math.min(.05,(ts-last)/1000); last=ts; tt+=dt;
    render(tt,dt);
    requestAnimationFrame(frame);
  }
  requestAnimationFrame(frame);
})();"""

html = io.open('presentation/index.html', encoding='utf-8').read()
start = html.index('(function(){\n  const W=2172')
end = html.index('/* уход с canvas-титула')
tail = html.rindex('})();', start, end)
html = html[:start] + ENGINE + html[tail + 5:]
io.open('presentation/index.html', 'w', encoding='utf-8').write(html)
print('index.html patched OK')
