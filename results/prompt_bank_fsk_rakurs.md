# Промпт картинки — Банк «ФСК» (смена ракурса, банк-центричный кадр)

**Идея:** **та же улица и мир, что `cafe-3.png`** (тот же стиль, материалы, свет, площадь,
светлый колонный банк, ЦУМ/ГУМ-здание, Moscow-City справа) — но **другой ракурс**: теперь
**первый левый объект = наш БАНК** (тот самый светлый неоклассический с колоннами, портиком,
фронтоном и зелёной крышей). Кафе и ЦУБ остаются **за левым краем кадра** (камера сместилась
вправо). На банке — **объёмная 3D-вывеска «ФСК рядом»**. Правее банка — **ЦУМ/ГУМ-здание** и
**Moscow-City справа** (как на `cafe-3.png`). Героя в кадре нет.

## ⚙️ Как запускать
- Это **смена ракурса** — маской из `cafe-3.png` не сделать. Генерим **заново (text-to-image)**,
  приложив **`cafe-3.png` как референс стиля/материалов, самого банка и ЦУМ-здания** (чтобы банк и
  ЦУМ были узнаваемы).
- **Размер:** 7680 × 2592 px (≈ 2,96:1), как остальные слайды. `--ar 3:1`, апскейл.
- ⚠️ Буквы «ФСК» — короткая кириллица, но генератор всё равно может исказить. Если поплывут —
  оставить объёмную подложку и поправить буквы в фоторедакторе.

## Полный промпт (text-to-image)
```
Photoreal cinematic key art, top-tier rendering quality, bright clean realistic look, a calm
summer daytime scene in central Moscow. SAME visual style, materials, lighting and color grade as
the reference image (cafe-3.png), and the SAME neoclassical BANK building and the SAME ЦУМ/ГУМ-style
department store as in the reference — keep them recognizable. Ultra-wide cinematic panorama, target
output 7680 x 2592 px (~2.96:1), professional look for a corporate government presentation.

NEW CAMERA ANGLE — BANK-CENTRIC: the camera has moved RIGHT along the street so the CAFE and the
ЦУБ office are now OFF-SCREEN to the LEFT, and the BANK is the FIRST, LEFTMOST object in the frame,
prominent in the LEFT foreground, seen at a three-quarter angle that shows its grand columned
front. The bank is a stately LIGHT sandy-grey stone NEOCLASSICAL building: a full-width PORTICO
with a row of TALL CORINTHIAN COLUMNS, a triangular PEDIMENT above them, a low GREEN (copper/teal)
roof, symmetric wings and grand entrance steps — the exact same bank as in the reference.

BANK SIGN: a modern VOLUMETRIC 3D signboard reading "ФСК рядом" (Cyrillic — "ФСК" in bigger capital
letters, "рядом" as a smaller word next to or below it) placed by the bank — extruded
three-dimensional channel letters with real depth and soft shadow, clean and corporate, mounted on
the facade above the entrance OR as free-standing 3D letters near the entrance steps. The sign must
read clearly as "ФСК рядом". Keep it photoreal and consistent with the building.

COMPOSITION & PERSPECTIVE: strong vanishing perspective — from the bank on the LEFT the wide paved
plaza and the MAIN AVENUE recede into the distance toward the RIGHT. To the RIGHT of the bank, along
the avenue, stands the large ЦУМ/ГУМ-STYLE DEPARTMENT STORE — a long ornate late-19th-century facade
with rich decorative stonework and a glass-vaulted arcade roof (the same building as in the
reference). At the far end on the RIGHT, CLEARLY VISIBLE on the horizon, the MOSCOW-CITY glass
skyscraper cluster in soft haze (readable, not washed out), matching our map where Moscow-City is on
the RIGHT. Small young trees along the pavement, NO cars, NO traffic. Keep the sky and open pavement
clean for later text overlay.

NO hero, NO main character, NO crowd of people — keep the scene empty of people, ready for
characters to be composited in later.

MOOD: bright optimistic summer day, warm daylight, clean and modern.

OUTPUT: ultra-wide 7680 x 2592 px, ~2.96:1. --ar 296:100 (если не примет — --ar 3:1, апскейл).

keep the SAME summer daylight mood and the SAME style as the reference; do NOT switch to night or a
dark palette.

avoid: a different bank (must be the SAME light columned bank as the reference); a dark / heavy /
modern bank; any hero / people crowd; cars, traffic; night or dark palette; flat cartoon; low
detail; Moscow-City on the left; the cafe or the ЦУБ office in frame (they are off-screen to the
LEFT); flat frontal facade view (keep the three-quarter angle and perspective); flat 2D sign (the
"ФСК рядом" sign must be VOLUMETRIC / 3D).
```

## Заметки
- **Ракурс:** банк — первый левый объект, крупно слева, 3/4; камера сместилась вправо, кафе/ЦУБ —
  за левым краем. Дальше площадь/аллея в перспективу, правее — **ЦУМ/ГУМ-здание**, **Moscow-City справа**.
- **Банк** — тот же светлый колонный (как `cafe-3.png` / карта), узнаваемый. **ЦУМ** — тоже как на `cafe-3.png`.
- **Вывеска «ФСК рядом» — объёмная 3D** (extruded буквы; «ФСК» крупнее, «рядом» мельче рядом/ниже),
  на фасаде над входом или отдельно у ступеней.
- **Героя нет** — накладываем отдельно в HTML.
- Размер/стиль/свет — как `cafe-3.png` (7680×2592, тёплый летний день).
