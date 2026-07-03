# -*- coding: utf-8 -*-
"""Патчер gen_cover_anim.py: конфиг CFG (размеры ×3 по просьбе), стиль частиц —
   круглые точки с мягким свечением (спрайты), цвет синий→циан→белый."""
import io

src = io.open('gen_cover_anim.py', encoding='utf-8').read()

OLD_HEAD = """ENGINE = r\"\"\"(function(){
  const W=2172,H=724; waveCv.width=W; waveCv.height=H;
  const ctx=waveCv.getContext('2d');
  const CX=1749, CY=363, AR=0.42;              // центр звезды (точка из разметки) и наклон вихря
\"\"\""""
NEW_HEAD = """ENGINE = r\"\"\"(function(){
  const W=2172,H=724; waveCv.width=W; waveCv.height=H;
  const ctx=waveCv.getContext('2d');
  const CX=1749, CY=363, AR=0.42;              // центр звезды (точка из разметки) и наклон вихря
  /* ═══ КОНФИГ ЧАСТИЦ — размеры/количество/цвет/стиль крутить ЗДЕСЬ ═══ */
  const CFG={
    tw:  {size:[3.3,7.8], alpha:0.8,  speed:[0.5,2.3]},    // мерцание точек картинки
    orb: {size:[2.7,6.6], alpha:0.62, speed:1.0},           // орбитеры вихря
    ring:{count:3, period:5.2, maxR:760, jit:28, alpha:0.5, size:6.0},  // расходящиеся волны
    run: {size:7.8, tail:10, alpha:0.6, speed:1.0},         // светлячки по волнам
    ray: {size:7.2, tail:8,  alpha:0.65, speed:1.0},        // светлячки по лучам
    pulse:{base:0.16, amp:0.10},                             // пульс звезды
    sparks:{rate:7, size:5.1}                                // искры вверх
  };
  /* стиль частиц: круглая точка с мягким свечением (спрайты 3 цветов) */
  function mkSpr(color){ const c=document.createElement('canvas'); c.width=c.height=32;
    const g=c.getContext('2d'); const gr=g.createRadialGradient(16,16,0,16,16,16);
    gr.addColorStop(0,'rgba(255,255,255,1)'); gr.addColorStop(0.28,color); gr.addColorStop(1,'rgba(0,0,0,0)');
    g.fillStyle=gr; g.fillRect(0,0,32,32); return c; }
  const SPR={ deep:mkSpr('rgba(90,150,245,0.55)'),          // глубокий синий
              cyan:mkSpr('rgba(140,210,255,0.6)'),          // циан
              white:mkSpr('rgba(225,242,255,0.72)') };      // почти белый
  function dot(spr,x,y,s,al){ ctx.globalAlpha=Math.min(1,al); ctx.drawImage(spr,x-s,y-s,s*2,s*2); }
\"\"\""""
assert OLD_HEAD in src, 'HEAD not found'
src = src.replace(OLD_HEAD, NEW_HEAD)

def rep(old, new):
    global src
    assert old in src, 'NOT FOUND: ' + old[:60]
    src = src.replace(old, new)

# twinkle: слой → спрайты, цвет по яркости
rep("""    /* ── мерцание частиц картинки ── */
    for(const p of tws){
      const a=Math.max(0,Math.sin(t*p.sp+p.ph));
      const al=0.75*p.v*a*a;
      if(al<0.03) continue;
      ctx.fillStyle='rgba(190,225,255,'+al.toFixed(3)+')';
      ctx.fillRect(p.x-p.s/2,p.y-p.s/2,p.s,p.s);
    }""",
"""    /* ── мерцание частиц картинки: цвет по яркости (синий→циан→белый) ── */
    for(const p of tws){
      const a=Math.max(0,Math.sin(t*p.sp+p.ph));
      const al=CFG.tw.alpha*p.v*a*a;
      if(al<0.03) continue;
      const spr=p.v>0.8?SPR.white:(p.v>0.5?SPR.cyan:SPR.deep);
      dot(spr,p.x,p.y,p.s,al);
    }""")

# twinkle init: размер/скорость из CFG
rep("sp:0.5+Math.random()*1.8, s:0.9+Math.random()*1.7}));",
    "sp:CFG.tw.speed[0]+Math.random()*(CFG.tw.speed[1]-CFG.tw.speed[0]), s:CFG.tw.size[0]+Math.random()*(CFG.tw.size[1]-CFG.tw.size[0])}));")

# орбитеры: init + слой
rep("w:0.04+0.22*(1-p[0]/640), ph:Math.random()*6.28, s:0.8+Math.random()*1.6}));",
    "w:(0.04+0.22*(1-p[0]/640))*CFG.orb.speed, ph:Math.random()*6.28, s:CFG.orb.size[0]+Math.random()*(CFG.orb.size[1]-CFG.orb.size[0])}));")
rep("""      const al=(0.16+0.4*o.v)*(0.55+0.45*Math.sin(t*1.3+o.ph));
      ctx.fillStyle='rgba(150,205,255,'+al.toFixed(3)+')';
      ctx.fillRect(x-o.s/2,y-o.s/2,o.s,o.s);
    }""",
"""      const al=CFG.orb.alpha*(0.3+0.7*o.v)*(0.55+0.45*Math.sin(t*1.3+o.ph));
      dot(o.v>0.7?SPR.cyan:SPR.deep,x,y,o.s,al);
    }""")

# кольца: параметры + спрайты
rep("""    for(let k=0;k<3;k++){
      const ph=((t/5.2)+k/3)%1;
      const r=60+ph*760;
      const al=(ph<0.1?ph/0.1:1)*(1-ph)*0.5;
      if(al<0.02) continue;
      const jit=ph*28;""",
"""    for(let k=0;k<CFG.ring.count;k++){
      const ph=((t/CFG.ring.period)+k/CFG.ring.count)%1;
      const r=60+ph*CFG.ring.maxR;
      const al=(ph<0.1?ph/0.1:1)*(1-ph)*CFG.ring.alpha;
      if(al<0.02) continue;
      const jit=ph*CFG.ring.jit;""")
rep("""        const aa=al*(0.4+0.6*f2);
        if(aa<0.02) continue;
        ctx.fillStyle='rgba(170,215,255,'+aa.toFixed(3)+')';
        const s=1+1.4*(1-ph);
        ctx.fillRect(x-s/2,y-s/2,s,s);""",
"""        const aa=al*(0.4+0.6*f2);
        if(aa<0.02) continue;
        dot(SPR.cyan,x,y,CFG.ring.size*(0.6+0.6*(1-ph)),aa);""")

# бегуны по волнам
rep("""      r.pos+=r.sp*dt/2;
      if(r.pos>=r.tr.length-1){ respawn(r); continue; }
      for(let k=0;k<10;k++){
        const i=Math.floor(r.pos)-k;
        if(i<0) break;
        const p=r.tr[i], al=0.55*(1-k/10);
        ctx.fillStyle='rgba(210,238,255,'+al.toFixed(3)+')';
        const s=k===0?2.4:1.6;
        ctx.fillRect(p[0]-s/2,p[1]-s/2,s,s);
      }""",
"""      r.pos+=r.sp*dt/2*CFG.run.speed;
      if(r.pos>=r.tr.length-1){ respawn(r); continue; }
      for(let k=0;k<CFG.run.tail;k++){
        const i=Math.floor(r.pos)-k;
        if(i<0) break;
        const p=r.tr[i], al=CFG.run.alpha*(1-k/CFG.run.tail);
        dot(k===0?SPR.white:SPR.cyan,p[0],p[1],k===0?CFG.run.size:CFG.run.size*0.62,al);
      }""")

# бегуны по лучам
rep("""      r.pos+=r.sp*dt;
      if(r.pos>=1){ r.pos=0; r.sp=(90+Math.random()*130)/r.L; }
      for(let k=0;k<8;k++){
        const q=r.pos-k*0.018;
        if(q<0) break;
        const x=r.x1+(r.x2-r.x1)*q, y=r.y1+(r.y2-r.y1)*q;
        const al=0.6*(1-k/8)*(1-q*0.55);          // хвост + затухание к концу луча
        if(al<0.03) continue;
        ctx.fillStyle='rgba(210,238,255,'+al.toFixed(3)+')';
        const s=k===0?2.2:1.5;
        ctx.fillRect(x-s/2,y-s/2,s,s);
      }""",
"""      r.pos+=r.sp*dt*CFG.ray.speed;
      if(r.pos>=1){ r.pos=0; r.sp=(90+Math.random()*130)/r.L; }
      for(let k=0;k<CFG.ray.tail;k++){
        const q=r.pos-k*0.018;
        if(q<0) break;
        const x=r.x1+(r.x2-r.x1)*q, y=r.y1+(r.y2-r.y1)*q;
        const al=CFG.ray.alpha*(1-k/CFG.ray.tail)*(1-q*0.55);   // хвост + затухание к концу луча
        if(al<0.03) continue;
        dot(k===0?SPR.white:SPR.cyan,x,y,k===0?CFG.ray.size:CFG.ray.size*0.65,al);
      }""")

# пульс
rep("const pu=0.16+0.10*Math.sin(t*1.8)+0.05*Math.sin(t*4.7);",
    "const pu=CFG.pulse.base+CFG.pulse.amp*Math.sin(t*1.8)+CFG.pulse.amp*0.5*Math.sin(t*4.7);")

# искры
rep("if(Math.random()<dt*7 && sparks.length<30){",
    "if(Math.random()<dt*CFG.sparks.rate && sparks.length<30){")
rep("max:1.4+Math.random()*1.4, s:1+Math.random()*1.6});",
    "max:1.4+Math.random()*1.4, s:CFG.sparks.size*(0.6+Math.random()*0.8)});")
rep("""      const q=1-s.life/s.max;
      ctx.fillStyle='rgba(205,235,255,'+(0.8*q).toFixed(3)+')';
      const ss=s.s*(0.5+0.5*q);
      ctx.fillRect(s.x-ss/2,s.y-ss/2,ss,ss);""",
"""      const q=1-s.life/s.max;
      dot(SPR.white,s.x,s.y,s.s*(0.5+0.5*q),0.85*q);""")

# сброс globalAlpha в конце кадра
rep("""    ctx.globalCompositeOperation='source-over';
  }
  let last=null,tt=0;""",
"""    ctx.globalAlpha=1;
    ctx.globalCompositeOperation='source-over';
  }
  let last=null,tt=0;""")

io.open('gen_cover_anim.py', 'w', encoding='utf-8').write(src)
print('generator patched: CFG + sprites + sizes x3')
