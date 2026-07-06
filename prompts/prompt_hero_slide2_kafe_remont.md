# Промпт: герой для слайда 2 «Ремонт кафе» — в каске, с планом в руках (cutout, прозрачный фон)

## Как использовать
- Генерим **отдельного героя** (в кадре сцены его нет), потом накладываем в HTML на слайд 2.
- **Приложи референс героя** `presentation/assets/img/objects/hero-cutout.png` — та же личность,
  та же одежда, тот же тёплый боковой свет (чтобы cutout лёг в тот же дневной кадр).
- Нужен **полный рост, прозрачный фон (PNG, alpha)**, чистый край силуэта.
- Поза под сцену: герой на объекте, **в строительной каске**, **с планом/чертежом в руках**,
  осматривает ход ремонта своего кафе.

## Промпт (EN)
```
Photorealistic full-body cutout of a young man, ISOLATED on a fully TRANSPARENT background
(alpha PNG), no ground, no shadow on the floor, nothing behind him — a clean people-cutout ready to
be composited onto a scene. Top-tier photoreal rendering, sharp detail, natural skin, cinematic
quality.

SAME PERSON as the reference image (keep him perfectly consistent): a slim, athletic man in his
mid-to-late 20s, fair skin with a light mixed-European look, short dark tousled hair, light stubble,
friendly relatable everyday face. Same body proportions and same warm late-afternoon SIDE/RIM
LIGHTING as the reference (soft golden sunlight catching one side of him, gentle warm tone), so this
cutout blends with the same daylight scene.

POSE — he is INSPECTING the renovation of his cafe, a confident "let's see how the work is going"
moment:
  - he wears a construction HARD HAT (helmet) on his head — a simple modern safety helmet
    (white or yellow), sitting naturally over his hair;
  - he holds an OPEN unrolled PLAN / blueprint / drawing in BOTH hands in front of him at chest
    level, looking down at it or glancing off toward the works — as if checking the layout against
    the site;
  - engaged, focused but positive expression, slight confident half-smile;
  - standing, weight relaxed on one leg, full body visible head to shoes.

CLOTHING — casual smart-casual under the helmet (SAME wardrobe as the reference):
  - an OPEN (unbuttoned) BLUE casual SHIRT worn over a plain WHITE T-SHIRT underneath (white tee
    visible on the chest, blue shirt hanging open, sleeves can be slightly rolled);
  - blue JEANS (denim) and clean WHITE SNEAKERS.

FRAMING: entire figure from the top of the helmet to below the shoes inside the frame, centered,
upright, feet flat as if standing on ground (so it can be placed into the scene later). Full body,
no cropping of hands, head or feet.

OUTPUT: high-resolution, transparent background (PNG, alpha), figure only.

avoid: any background, floor, wall, cast shadow on ground; other people; text, logos, watermarks,
UI; binoculars, headphones, coffee cup, phone (this pose has ONLY the hard hat + the plan in hands);
changing his face or age or build (must stay the SAME person as the reference); no hard hat / no
plan; dark or night palette; flat cartoon; low detail; blurry hands or extra fingers.
```

## Заметки
- **Реквизит именно этот:** каска + развёрнутый план в руках. Ничего лишнего (без наушников,
  бинокля, кофе, телефона — они у героя в других сценах).
- Одежда/лицо — как `hero-cutout.png` (единый персонаж во всех слайдах).
- Свет — тёплый дневной боковой, под сцену `cafe-1.png` (чтобы cutout не выбивался).
- Прозрачный фон, полный рост, ноги «стоят» — чтобы поставить перед кафе в HTML.
