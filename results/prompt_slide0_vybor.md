# Промпт картинки — Слайд 0 «Выбор направления»

Стиль: **«Летняя Дневная Москва»** (утверждён) · Генератор: GPT/DALL-E/Sora/Midjourney

## ⚙️ Технические параметры (экран зала)

- LED-экран: **19,2 × 6,48 м**, шаг пикселя 2,5 мм
- Разрешение: **7680 × 2592 px**
- Соотношение сторон: **≈ 2,96:1** (почти 3:1, сверхширокий) — **НЕ 16:9**
- **Картинку генерим сверхширокой** (`--ar 3:1`, ближайшее к 2,96:1), затем апскейл до
  **7680 × 2592** (Topaz / Real-ESRGAN). DALL-E/GPT макс. 1792×1024 — генерить широкую
  «болванку», апскейлить; либо собрать панораму из 2–3 горизонтальных кусков и сшить.
- **Текст, цифры, HUD, рамки, подписи В КАРТИНКЕ НЕ РИСУЕМ** — только чистый арт.
  Все цифры 1·2·3, заголовки, карточки, шкалы навыков, гекс-рамки накладываем в **HTML/коде**.
  В композиции оставить «воздух» (чистые зоны) под HTML-оверлей.

## Содержание кадра

- **3 объекта НА ВЫБОР** (зал голосует) — отрасли из сценария:
  **1) Общепит · 2) Салон красоты · 3) Торговля** — три здания в ряд на переднем плане.
- **Фоновые landmarks (оставляем в скайлайне):**
  **Москва-Сити · Кластер «Ломоносов» · Фабрика подарков** — узнаваемые места города.

---

## STYLE-ANCHOR (дневной — копировать дословно в каждый слайд этого стиля)

> Cinematic AAA video-game key art, top-tier rendering quality, bright clean hi-tech
> strategy-game aesthetic (a peaceful strategic city map for business — NO weapons, NO
> violence, NO soldiers). Slightly isometric 3D view of a modern, sunny, futuristic Moscow
> on a clear summer day: deep blue sky, soft white clouds, the sparkling Moskva river, fresh
> green parks. Vibrant daylight palette (the holographic neon HUD is added later in HTML, NOT
> in the image). Volumetric warm sunlight, gentle summer haze, crisp depth of field,
> ultra-detailed. The SAME recurring hero: a young male entrepreneur, short dark hair, light
> casual t-shirt, friendly determined face — identical across all images. Ultra-wide ~3:1
> panorama framing, clean professional look suitable for a corporate government presentation.

---

## Полный промпт (слайд 0)

```
Cinematic AAA video-game key art, top-tier rendering quality, bright clean hi-tech strategy-game
aesthetic (a peaceful strategic city map for business — NO weapons, NO violence, NO soldiers).
Slightly isometric 3D view of a modern, sunny, futuristic Moscow on a clear summer day: deep blue
sky, soft white clouds, the sparkling Moskva river, fresh green parks. Vibrant daylight palette,
volumetric warm sunlight, gentle summer haze, crisp depth of field, ultra-detailed. Ultra-wide
cinematic panorama, ~3:1 aspect ratio, clean professional look for a corporate government
presentation.

SCENE: a wide sunny panorama of futuristic summer Moscow, the Moskva river curving through the
city. In the BACKGROUND skyline keep three recognizable landmarks, softly glowing as already-known
places spread across the wide horizon: the MOSCOW-CITY glass skyscraper cluster, the modern
"LOMONOSOV" innovation cluster campus, and the red-brick "GIFT FACTORY" creative loft.
In the FOREGROUND, THREE distinct business buildings — the three sectors to choose from — standing
apart in a row across the wide frame, each on a clean empty platform of bare ground (leave the
platform plain — no signs, no symbols):
  (1) a cozy summer street CAFE / small restaurant with an outdoor terrace (food service);
  (2) a bright modern BEAUTY-SALON storefront (no text on the sign);
  (3) a small RETAIL SHOP / market trade pavilion with goods on display.
Keep generous clean sky and empty foreground space around and above the three buildings for later
UI overlay.

CHARACTER: the same young entrepreneur standing at the front crossroads, seen from behind / three-
quarter back, looking at the three buildings, deciding which path to take.

COMPOSITION: balanced ultra-wide layout, the three buildings clearly separated left / center / right,
hero in the lower-center foreground, plenty of negative space in the sky and ground.

MOOD: bright optimistic summer morning, big-opportunity feeling, fresh and modern, warm daylight.
--ar 3:1

keep the SAME character and SAME daytime summer art style across all slides; do NOT switch to a
night or dark palette.

avoid: ANY text, letters, words, numbers, digits, captions, signs with writing, UI, HUD, holographic
panels, icons, frames, watermarks, logos; weapons, guns, soldiers, blood, war; dark night palette,
gloomy heavy fog, different character faces between images, flat 2D cartoon, low detail, changing
color palette.
```

---

## Заметки

- **Никакого текста/цифр/HUD в картинке.** Генератор рисует только город, 3 здания и героя.
  Цифры 1·2·3, гекс-рамки, заголовок «ВЫБОР НАПРАВЛЕНИЯ», карточки отраслей, шкалы навыков
  (Знания / Общественный вклад / Развитие бизнеса) — всё в HTML поверх.
- **3 объекта на выбор = отрасли** (для HTML-тултипов, числа черновые):
  | № | Отрасль | Сложность | Вход | Маржа |
  |---|---------|-----------|------|-------|
  | 1 | Общепит (кафе/ресторан) | ★★★ | помещение, оборудование, персонал | средняя |
  | 2 | Салон красоты | ★★ | помещение, мастера, лицензии | высокая |
  | 3 | Торговля (магазин/рынок) | ★★ | аренда точки, товарный запас | низкая-средняя |
- **Москва-Сити, Ломоносов, фабрика Подарков — это ФОН** (landmarks), не выбор. Держим их
  в скайлайне для узнаваемости.
- **Сверхширокий формат.** Композиция «дышащая» — 3 здания разнесены по ширине, между ними
  и сверху воздух под оверлей. Генерить `--ar 3:1`, апскейл до 7680×2592.
- **Единство стиля.** Anchor неприкосновенен — тот же дневной блок в слайды 1–6, меняется
  только SCENE/CHARACTER/COMPOSITION.

## ⚠️ Открытый вопрос по вёрстке
Текущий каркас и SVG-титул — **16:9** (viewBox 1672×941). Экран зала — **2,96:1** (7680×2592).
Под зал HTML-сцену и титул надо будет переверстать на сверхширокий формат. Отдельная задача.
