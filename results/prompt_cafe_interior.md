# Промпт картинки — Интерьер кафе (счастливые гости, официант с киберпротезом)

**Идея:** заходим ВНУТРЬ нашего кафе «Ваш любимый КОФЕ». Тёплая, живая, инклюзивная сцена: все
счастливы. **Официант с киберпротезом** обслуживает гостей, **один ребёнок из многодетной семьи с
любопытством трогает протез**, рядом — **пожилая пара (пенсионеры)**. Атмосфера доброты и
доступности.

**Сохранить интерьер из `cafe-3.png`** (то, что видно за витриной): барная стойка, деревянные
шкафы/полки с чашками и банками, подвесные лампы-споты, тёплый свет, кирпич/плитка, современный
уютный кофе-стиль.

## ⚙️ Как запускать
- **ГЛАВНОЕ — приложи картинки-референсы `cafe-3.png` и `cafe-1.png`** и напиши «match the rendered
  style of these reference images». Это **главный рычаг стиля**: без референса GPT-image по умолчанию
  для «интерьер + люди» уходит в фотореализм, и слова его слабо удерживают. Референс держит наш
  чистый CG-архвиз-лук и узнаваемый интерьер (стойка, полки, лампы, тёплый грейд).
- **Размер:** 7680 × 2592 px (≈ 2,96:1), как остальные слайды. `--ar 3:1`, апскейл.
- Это **полноценная сцена с людьми** (не cutout) — фон нужен. Люди — главный смысл кадра.
- ⚠️ Текст/вывески/меню в картинке НЕ рисуем (кириллица плывёт) — если надо, наложим в HTML.

## Полный промпт (text-to-image)
```
Cinematic AAA video-game KEY ART / high-end ARCHITECTURAL-VISUALIZATION 3D RENDER (think Unreal
Engine / Octane archviz) — match the EXACT same rendered look, finish and color grade as our
reference images (cafe-1.png, cafe-2.png, cafe-3.png): clean, crisp, smooth CG surfaces, polished
even CG lighting, subtly STYLIZED, a slightly "game key art" aesthetic. Rendered image, NOT a
photograph: NO photographic film grain, NO lens bokeh, NO shallow real-camera depth-of-field, NO
stock-photo / documentary snapshot look. Characters and faces are rendered in the SAME clean CG
style as the room (not photographic portraits).
The cozy INTERIOR of a modern coffee shop, a happy welcoming everyday scene (NO weapons, NO
violence). SAME interior style, materials and warm color grade as the reference (cafe-3.png): a
wooden BAR COUNTER, wooden CABINETS / SHELVES with cups and jars, warm PENDANT SPOT LIGHTS, brick
and tile surfaces, big storefront WINDOWS letting soft warm daylight in. Ultra-wide cinematic
interior panorama, target output 7680 x 2592 px (~2.96:1), professional look for a corporate
government presentation.

COMPOSITION: place the MAIN SUBJECTS (the waiter with the prosthetic, the child touching it, the
family, the elderly couple) in the LEFT part of the frame (left ~55-60%). Keep the RIGHT part more
OPEN and calmer — bar counter, shelves, windows, cozy background — so presentation text can be
overlaid there later. Strong but natural interior depth.

THE SCENE — a lively, inclusive, joyful coffee shop full of happy guests:
  - a friendly WAITER with a modern CYBER-PROSTHETIC ARM — a sleek clean bionic forearm and hand
    (matte metal and carbon with subtle soft-glow accents), worn naturally; he is serving coffee,
    smiling, relaxed and confident;
  - a MULTI-CHILD FAMILY (parents + several young children) at a table, cheerful and warm; ONE of
    the CHILDREN reaches out with curiosity and gently TOUCHES the waiter's prosthetic arm, fascinated
    and delighted — a tender, positive "high-tech is friendly" moment; the parents smile warmly;
  - an ELDERLY COUPLE (pensioners) at another table nearby, cups of coffee in front of them, content
    and happy, enjoying the atmosphere;
  - maybe one or two more relaxed guests in the background for life.
EVERYONE is genuinely HAPPY — warm smiles, relaxed body language, an inclusive and caring mood where
people of all ages and abilities feel welcome. Rendered in the same clean CG / key-art style as the
reference deck — NOT a real photo.

LIGHTING & MOOD: warm golden daylight from the big windows plus cozy pendant lights, gentle glow,
inviting and homely, rich but soft. High detail, photoreal, cinematic depth.

NO text, letters, words, numbers, menus with writing, logos or watermarks in the image (keep any
boards/signs blank). Keep the interior recognizable as the same cafe as the reference.

avoid: a real DOCUMENTARY / STOCK-PHOTO / snapshot look, photographic realism, real-camera grain or
heavy photographic bokeh (keep the polished cinematic KEY-ART / 3D-RENDER style of the reference
deck — cafe-1/2/3); a scary / aggressive / dystopian robotic look for the prosthetic (it must look
FRIENDLY, sleek and helpful); any distress, sadness or discomfort (everyone is happy); a cold or
clinical look; weapons, violence; empty lifeless room; different interior style from the reference;
night or dark palette; flat cartoon; low detail; distorted faces or hands or extra fingers;
readable text.
```

## Заметки
- **Люди:** официант с киберпротезом (дружелюбный, обслуживает) + многодетная семья (один ребёнок
  трогает протез) + пожилая пара. Все счастливы, тепло, инклюзивно.
- **Протез:** современный, аккуратный, «добрый» хай-тек (металл/карбон + мягкая подсветка) — НЕ
  агрессивный/дистопичный. Дети с любопытством и радостью касаются его.
- **Интерьер — как `cafe-3.png`:** барная стойка, деревянные полки, подвесные лампы, тёплый свет,
  большие витрины. Узнаваемо то же кафе.
- **Полноценная сцена с людьми** (не cutout) — фон нужен.
- **Стиль — как вся дека (`cafe-1/2/3`): cinematic key art / стилизованный 3D-рендер, НЕ фото.**
  Если ИИ уходит в сток-фото/репортаж — усилить «AAA game key art, stylized CG render like cafe-3.png,
  not a real photograph» и приложить `cafe-1.png`+`cafe-3.png` как референсы стиля.
- **Основные объекты — в левой части** (~55–60%); правая часть спокойнее (стойка/полки/окна) под текст.
- Текст/меню/вывески в картинке НЕ рисуем — при необходимости в HTML.
- Размер 7680×2592, тёплый дневной свет.
