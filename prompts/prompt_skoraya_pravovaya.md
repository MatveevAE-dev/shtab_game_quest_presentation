# Промпт: машина «Скорая правовая помощь» (слайд 15) — cutout в стиле эскаватора

## Идея (слайд 15)
- На **главной дороге** припаркован **эскаватор** (уже есть — `excavator_parked.png`).
- По главной дороге **со стороны Moscow-City** едет **«Скорая правовая помощь»** — машина как
  карета скорой, **едет на нас**: видно **перёд машины**, вверху на лобовом стекле надпись
  **«СКОРАЯ ПРАВОВАЯ ПОМОЩЬ»**.
- Генерим **машину отдельно** (на белом фоне → фон вырезаем потом) и накладываем на дорогу в HTML — как эскаватор.

## Стиль — КАК У ЭСКАВАТОРА (`excavator_parked.png`)
- **Стилизованный полу-мультяшный cel-shaded game-asset:** жирный чистый тёмный контур, гладкие
  плоскости, мягкие cel-блики, чуть «тун», но детально. **НЕ фото.**
- **Фон — сплошной ровный ЦВЕТ (белый), НЕ «прозрачный».** ⚠️ GPT-image/DALL·E не умеет реальный
  alpha — на слово «transparent» рисует **шахматку**. Генерим на белом, фон **вырезаем потом**
  (rembg / remove.bg / Photoshop). Чистый край силуэта, та же обводка/стилизация, что у эскаватора.
  **Приложи `excavator_parked.png` как референс стиля.**

## Промпт (EN)
```
A stylized semi-cartoon CEL-SHADED 3D game asset of an AMBULANCE-style emergency VAN, isolated on a
PLAIN SOLID FLAT background of ONE single uniform colour (pure white), with NO scene and NO pattern —
a clean vehicle asset that will have its background removed afterwards. Do NOT paint a checkerboard
/ transparency-grid pattern; the background must be one flat solid colour only.
Render it in the EXACT same art style as the attached reference excavator asset: bold clean dark
OUTLINES, smooth flat surfaces with soft cel-shaded highlights, slightly toon but detailed, vibrant
and crisp. This is a game asset, NOT a photo — no photographic realism, no film grain, no real
background.

VEHICLE: a modern emergency AMBULANCE VAN, mostly WHITE body with clean BLUE accent stripes, a BLUE
emergency LIGHT BAR on the roof. Instead of a medical cross, a small SCALES-OF-JUSTICE emblem on the
front (it is a LEGAL-aid rapid-response van). Clean headlights, grille, bumper, front license area.

VIEW: FRONT three-quarter view — we see the FRONT of the van as it drives TOWARD the viewer (as if
coming along the road from the right / from the Moscow-City side). The front windshield, hood, grille
and headlights are clearly visible.

WINDSHIELD BANNER: across the TOP of the front windshield, a banner strip reads "СКОРАЯ ПРАВОВАЯ
ПОМОЩЬ" in clean bold white Cyrillic capital letters on a dark strip — readable and straight.
(If the Cyrillic distorts, leave the banner strip BLANK — the text will be added later.)

Isolated on a plain solid flat single-colour background (pure white), clean silhouette edge, same
outline weight and cel shading as the reference excavator. High resolution.

avoid: a painted CHECKERBOARD / transparency-grid pattern as the background; any textured, gradient,
scene or road background (background must be ONE flat solid colour); photographic realism, real
photo, film grain; a different art style from the reference excavator; a medical red cross (use
scales of justice — it is LEGAL help); police markings; text other than the windshield banner;
watermarks, logos; dark / night palette; flat 2D sticker look; low detail; distorted wheels or
melted shapes.
```

## Заметки
- **Стиль строго под `excavator_parked.png`** (cel-shaded game-asset, жирный контур) — приложи его референсом.
- **Вид спереди** (3/4), машина «едет на нас» со стороны Moscow-City (справа).
- **Надпись «СКОРАЯ ПРАВОВАЯ ПОМОЩЬ»** — вверху лобового. ⚠️ Кириллица в cel-стиле поплывёт —
  надёжнее оставить **пустую тёмную плашку** на лобовом и наложить текст в HTML.
- **Тема — правовая, не медицинская:** вместо красного креста — **весы правосудия**; синий проблесковый маячок.
- **Фон вырезаем ПОСЛЕ генерации** (генерим на белом → rembg/remove.bg/Photoshop → чистый PNG alpha),
  затем накладываем на дорогу в HTML рядом с припаркованным эскаватором. Не просить у ИИ «transparent» —
  он рисует шахматку.
- Размещение слайда 15: эскаватор припаркован на главной дороге + эта машина едет по ней со стороны Moscow-City.
