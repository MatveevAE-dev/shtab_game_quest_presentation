# Референсы стилей оформления — титульный слайд (5 вариантов)

Дата: 2026-06-09
Назначение: по одному референсу титульного слайда на каждый стиль. Руководитель выбирает один.
Генератор картинок: GPT/DALL-E/Sora · Соотношение: 16:9 · Слайд: только Титул (Слайд 0).
Сцена титула (общая для всех): один герой-предприниматель + 6 ключевых объектов на изометрической карте Москвы.

## Общие требования к КАЖДОМУ промпту (соблюдать во всех 5)
- **Герой:** один и тот же предприниматель (молодой, тёмные короткие волосы, лёгкая футболка), стоит на светящейся стартовой площадке слева-внизу. Единственный выделенный человек.
- **6 объектов на карте** (каждый узнаваем, мягко подсвечен, чтобы поверх повесить маркер):
  1) Даниловский рынок (крытый рынок с арочными стеклянными крышами);
  2) Кафе (небольшое уличное кафе с летней террасой);
  3) Кластер «Ломоносов» (современный стеклянный техно-кампус / научный парк);
  4) ТЦ ГУМ (исторический торговый пассаж у Красной площади);
  5) Москва-Сити (кластер стеклянных небоскрёбов на горизонте);
  6) Красный Октябрь (краснокирпичная фабрика-лофт, креативный квартал у реки).
- **БЕЗ текста и значков:** никакого текста, букв, цифр, логотипов, UI/HUD, иконок и маркеров-пинов. Это чистый арт-фон — весь текст и игровые значки накладываем сами в вёрстке.
- **Формат:** 16:9, без оружия/милитари/насилия.

## Разрешение и качество (экран концертного зала)
Картинку покажут на очень большом экране (LED-стена / проектор концертного зала) — нужна максимальная чёткость.
- **Целевое разрешение финала:** минимум **4K = 3840×2160**, лучше **8K = 7680×4320**, строго 16:9.
- **Реальность генераторов:** нативно выдают меньше (DALL-E 3 ~1792×1024, Midjourney ~до 2048, Sora/новые — выше). Поэтому: генерировать на максимально доступном размере 16:9 → затем **AI-апскейл до 4K/8K** (Topaz Gigapixel, Magnific, Upscayl).
- **В каждый промпт добавлять хвост качества:** `ultra-high resolution, 8K, extremely sharp, crisp fine detail, high-DPI, clean, made for a giant LED concert-hall screen`.
- При генерации ставить максимальное качество (Midjourney: `--quality 2`, `--ar 16:9`, затем Upscale → внешний апскейл до 4K/8K).

---

## Архетипы объектов (единый каркас для всех миров)

В каждом мире **6 объектов = 6 бизнес-архетипов**. Берём объект, характерный для лора
конкретного мира, но **сохраняем его бизнес-роль, порядок и узнаваемую функцию**. Герой,
маршрут и смысл уровней едины во всех стилях — меняется только «оболочка» объекта.

| # | Бизнес-архетип | Базовый объект (наш мир) | Бизнес-смысл уровня |
|---|----------------|--------------------------|---------------------|
| 1 | **Рынок** (продуктовый) | Даниловский рынок | точка входа, первые продажи |
| 2 | **Питание** (малое, кафе) | Кафе | малый бизнес, сервис |
| 3 | **Исследования и инновации** | Кластер «Ломоносов» | R&D, гранты, технологии |
| 4 | **Производство** | Красный Октябрь | масштабирование, выпуск продукта |
| 5 | **Торговля** (ритейл) | ТЦ ГУМ | поток клиентов, бренд |
| 6 | **Престиж / статус** | Москва-Сити | вершина, статусный бизнес |

**Правило адаптации:** при смене мира заменяем визуальную оболочку объекта на характерную для
сеттинга (футуристичный рынок, космо-лаборатория, дрон-завод и т.п.), но **архетип, его номер и
бизнес-функцию не трогаем**. Каждый объект остаётся узнаваем и как «этот мир», и как «этот тип бизнеса».

**Атрибуты предпринимателя** тоже адаптируем под мир: базовые навыки (Идея / Мотивация / Бизнес-план)
сохраняют смысл, но получают тематические названия и образ снаряжения героя — при этом **лицо и
личность героя неизменны во всех стилях** (один и тот же узнаваемый персонаж).

---

## Стиль 1 — «Летняя Москва · золотой час» (наш стиль, день)

Свет: золотой час. Акцент: тёплый летний (зелень + золото + небесно-голубой). HUD: смягчённый day-HUD. Город: зелёная цветущая Москва.

### Промпт картинки (титул)
> ВАЖНО: на картинке НЕТ текста, надписей, букв, цифр, логотипов и UI-иконок/HUD —
> это чистый арт-фон. Весь текст и игровые значки накладываются поверх в вёрстке.
```
Cinematic AAA video-game key art, top-tier rendering quality, friendly hi-tech strategy-game
aesthetic (a strategic city-map for business — NO weapons, NO military, NO violence).
Isometric 3D strategy-map of a lively SUMMER daytime Moscow at GOLDEN HOUR: lush green parks,
tree-lined boulevards, fountains, people, blue sky with warm low sun and long soft shadows.
Warm summer palette — fresh green, warm gold and sky-blue accents over bright daylight.
Volumetric warm sunlight, light summer haze, shallow depth of field.
CLEAN PLATE — IMPORTANT: absolutely NO text, NO letters, NO numbers, NO captions, NO logos,
NO UI, NO HUD, NO icons and NO map pins/markers anywhere in the image; pure background art only.
Wide 16:9 widescreen composition.
HERO: ONE recurring character — a young male entrepreneur, short dark hair, light casual
t-shirt, friendly determined face — standing on a glowing round start platform in the
lower-left foreground, looking out over the city. He is the only person highlighted.
SIX KEY LOCATIONS spread across the isometric map, each clearly readable as a distinct place,
softly glowing so a marker can be placed on top later:
  1) Danilovsky Market — a large covered market hall with arched glass roofs;
  2) a small cozy street cafe with summer terrace and umbrellas;
  3) "Lomonosov" innovation cluster — a modern glass tech-campus / science park;
  4) GUM department store — the historic ornate shopping arcade by Red Square;
  5) Moscow-City — a cluster of tall glass-and-steel skyscrapers on the horizon;
  6) Krasny Oktyabr (Red October) — a red-brick former chocolate factory, creative quarter
     by the river.
Arrange them at varied distances across a sunny green Moscow stretching to the horizon.
MOOD: optimistic, warm, alive, summer.
QUALITY: ultra-high resolution, 8K, extremely sharp, crisp fine detail, high-DPI, clean,
made for a giant LED concert-hall screen. --ar 16:9 --quality 2
```
avoid: ANY text, letters, numbers, captions, logos, UI, HUD, icons, map pins/markers;
weapons, guns, soldiers, war, night, cold blue-only palette, flat 2D cartoon, low detail,
extra random people competing with the hero, different character face.

### Дизайн-система презентации (HTML)
- **Вайб:** дружелюбный летний хайтек, светлый, «город помогает бизнесу».
- **Палитра:**
  - Фон: светлый небесно-кремовый градиент (`#eaf4ee → #d8ecf5`).
  - Акцент-1 (основной): свежая зелень `#2FAF6E`.
  - Акцент-2: тёплое золото `#F4B740`.
  - Акцент-3: небесно-голубой `#6CC0E5`.
  - Текст: тёмный сланец `#1b2a23` (на светлом).
  - Панели: матовое стекло `rgba(255,255,255,.55)` + лёгкое размытие.
- **Шрифты:** заголовки — Orbitron (700, чуть легче, без жёсткого «милитари»); тело — Rajdhani. (Совместимо с текущей вёрсткой — лёгкая замена.)
- **UI/HUD:** скруглённые углы 8–12px, мягкие тени, полупрозрачные светлые панели; угловые скобки тоньше или убрать; скан-линии выключить (день, чисто).
- **Карта/маршрут/объекты:** линии и контуры — зелёно-золотые (`#2FAF6E`/`#F4B740`) вместо неон-циан; свечение мягкое, тёплое.
- **Достижения:** золото `#F4B740` (как сейчас) — отлично ложится в летнюю палитру.

---

## Стиль 2 — «Алиса · Сто лет тому вперёд» (яркий кино-сайфай)

Вселенная: новый фильм «Сто лет тому вперёд» (2024), Алиса Селезнёва. Тон: яркий контрастный блокбастер-сайфай.

### Объекты мира (6 архетипов в сеттинге «Сто лет тому вперёд»)

Те же 6 бизнес-архетипов, переосмысленные в светлом будущем Москвы ~2124 г. Узнаваемый силуэт
исходного места сохраняем, оболочку — футуризируем (бело-хром, неон, голограммы, флипы, космос).

| # | Архетип | Объект в мире «Алисы» |
|---|---------|------------------------|
| 1 | Рынок (продуктовый) | **Даниловский рынок** — крытый космо-фуд-маркет: те же арочные крыши, но хром-стекло, парящие торговые ряды, голо-ценники, био-купола с экзотическими «звёздными» фруктами |
| 2 | Питание (кафе) | **Кафе** — уличное кафе будущего с голо-террасой, антиграв-столиками, светящимися напитками и роботом-официантом |
| 3 | Исследования и инновации | **Кластер «Ломоносов»** — сияющий научно-космический кампус: бело-хром лаборатории, орбитальные купола, стартовая ферма-антенна, голо-проекции R&D |
| 4 | Торговля (ритейл) | **ТЦ ГУМ** — исторический пассаж, отреставрированный в хром-стекле: левитирующие торговые галереи, голо-витрины, премиальный променад будущего |
| 5 | Престиж / статус | **Москва-Сити** — кластер сверх-небоскрёбов будущего с небесными мостами и шпилем-доком для флипов, штаб-квартиры корпораций |
| 6 | Производство | **Красный Октябрь** — узнаваемая краснокирпичная фабрика у реки, ставшая хайтек-производством: роботизированные линии, сборка дронов и антиграв-каров, светящиеся мастерские |

### Атрибуты предпринимателя (под сеттинг «Алисы»)

Лицо и личность героя **неизменны** (тот же молодой предприниматель, тёмные короткие волосы),
но снаряжение и навыки — из мира будущего.

- **Навыки (панель игрока), базовый смысл сохранён:**
  - Идея → **«Видение будущего»** (vision) — иконка звезда/лампа;
  - Мотивация → **«Космо-драйв»** (энергия, запал) — иконка молния/комета;
  - Бизнес-план → **«Голо-бизнес-план»** — иконка голограмма/планшет.
- **Образ/снаряжение героя (для промпта картинки):** лёгкая смарт-куртка поверх футболки,
  голо-коммуникатор на запястье (проецирует маленький AR-план), AR-визор сдвинут на лоб,
  антиграв-кроссовки со светящейся подошвой; стоит на круглой голографической стартовой платформе.

### Промпт картинки (титул)
> ВАЖНО: на картинке НЕТ текста, надписей, букв, цифр, логотипов и UI-иконок/HUD —
> это чистый арт-фон. Весь текст и игровые значки накладываются поверх в вёрстке.
```
Cinematic sci-fi blockbuster key art in the spirit of a modern Russian space adventure film
("One Hundred Years Ahead" / «Сто лет тому вперёд», 2024). Bright, vivid, high-contrast
optimistic vision of Moscow ~100 years in the future: gleaming white-and-chrome architecture,
sky-bridges, streams of hovering flying cars (flips), a distant cosmoport with a docked starship,
cosmos and a softly glowing planet on the horizon. Saturated electric-blue, violet and
hot-magenta neon over clean white, soft lens flares and god-rays. NO weapons, NO violence.
CLEAN PLATE — IMPORTANT: absolutely NO text, NO letters, NO numbers, NO captions, NO logos,
NO UI, NO HUD, NO icons and NO map pins/markers anywhere in the image; pure background art only.
Wide 16:9 widescreen isometric strategy-map composition.
HERO: ONE recurring character — the SAME young male entrepreneur, short dark hair, friendly
determined face (identical face in every style) — wearing a sleek light smart-jacket over a
casual t-shirt, a glowing holographic wrist-communicator projecting a tiny AR plan, a thin
AR-visor pushed up on his forehead, light-up antigrav sneakers; standing on a glowing round
holographic start platform in the lower-left foreground, looking out over the bright future city.
He is the only person highlighted.
SIX KEY LOCATIONS across the futuristic isometric map — each keeps its recognizable real-world
silhouette but is reimagined in this bright sci-fi future, softly glowing so a marker can be
placed on top later:
  1) FOOD MARKET — Danilovsky Market as a covered space food-market: the same arched glass roofs
     but chrome-and-glass, floating produce stalls, holographic price tags, bio-domes with exotic
     star-grown fruit and greenery;
  2) SMALL CAFE — a cozy future street cafe with a holographic terrace, anti-grav tables and
     stools, glowing drinks and a serving robot;
  3) R&D / INNOVATION — the "Lomonosov" cluster as a gleaming science-and-space research campus:
     white-chrome labs, orbital-tech domes, a small launch gantry / antenna spire, holographic
     research projections;
  4) RETAIL — GUM, the historic ornate arcade restored in chrome-and-glass: levitating shopping
     galleries and holographic storefront displays, a premium future promenade;
  5) PRESTIGE / STATUS — Moscow-City as towering future super-skyscrapers with sky-bridges and a
     flip-docking spire, gleaming corporate headquarters on the horizon;
  6) PRODUCTION — Krasny Oktyabr (Red October), the red-brick riverside factory kept clearly
     recognizable, now a hi-tech production district: robotic assembly lines, drone and
     antigrav-vehicle fabrication, glowing maker-workshops.
Arrange them at varied distances across a dazzling future Moscow stretching to a starry horizon.
MOOD: wonder, optimism, bright cinematic sci-fi, adventure.
QUALITY: ultra-high resolution, 8K, extremely sharp, crisp fine detail, high-DPI, clean,
made for a giant LED concert-hall screen. --ar 16:9 --quality 2
```
avoid: ANY text, letters, numbers, captions, logos, UI, HUD, icons, map pins/markers;
weapons, war, dark dystopia, grime, flat 2D cartoon, low detail, extra random people competing
with the hero, different character face.

### Дизайн-система презентации (HTML)
- **Вайб:** светлое будущее, космос, чудо, блокбастер-сайфай.
- **Палитра:**
  - Фон: глубокий космический сине-фиолетовый градиент (`#0a1230 → #1a1248`).
  - Акцент-1: электрик-синий `#2E7BFF`.
  - Акцент-2: фиолет/виолет `#B14CFF`.
  - Акцент-3: горячая маджента `#FF4FD8`.
  - Свет/блики: чистый белый `#F2F6FF` + лёгкие lens-flare.
  - Текст: белый/светло-голубой `#DCE8FF`.
  - Панели: глянцевое стекло `rgba(20,28,70,.55)` + неоновая кромка.
- **Шрифты:** заголовки — Orbitron (heavy, «космос»); тело — Rajdhani. Можно добавить широкий трекинг для футуризма.
- **UI/HUD:** глянцевые голо-панели, неоновые края, скруглённые формы, мягкое свечение, анимированные блики/голограммы.
- **Карта/маршрут/объекты:** яркие сине-маджентовые голо-линии, свечение сильное.
- **Объекты на карте:** иконка-маркер та же (замочек-гекс), но в неоново-синей/маджентовой подсветке.
- **Достижения:** неоново-розовый/виолет (`#FF4FD8`) или золото — на выбор; в этой палитре ярче смотрится розовый.

---

## Стиль 3 — «Волшебный мир · в духе саги о юном волшебнике» (тёплое фэнтези)

Вселенная: магический мир в духе саги о юном волшебнике (уютное британское фэнтези, dark-academia).
Сцена — **скрытый волшебный квартал Москвы**: те же узнаваемые силуэты, но заколдованные.
Тон: тёплая магия при свете свечей, эпично-сказочно, вечерний туман и искры волшебства.

> ⚠️ В промпте для генератора НЕ используем торговые имена (Harry Potter, Hogwarts, Diagon Alley и т.п.) —
> их фильтры режут. Пишем «in the spirit of a magical wizarding-school saga» + обобщённые волшебные объекты.

### Объекты мира (6 архетипов в волшебном сеттинге)

Узнаваемый силуэт исходного места сохраняем, оболочку делаем волшебной (чары, свечи, совы, руны, котлы).

| # | Архетип | Объект в волшебном мире |
|---|---------|--------------------------|
| 1 | Рынок (продуктовый) | **Даниловский рынок** — крытый волшебный базар: те же арки, но витражные крыши, парящие лотки, само-взвешивающиеся весы, бочки с магическими ингредиентами, совы под сводами |
| 2 | Питание (кафе) | **Кафе** — уютная волшебная таверна-кофейня: парящие свечи, само-помешивающиеся чашки, котлы-чайники с паром, тёплый свет окон, маленькая терраса |
| 3 | Исследования и инновации | **Кластер «Ломоносов»** — магическая академия/алхимический колледж: шпили-башни, телескопы, светящиеся рунные лаборатории, парящие книги (R&D = волшебные исследования) |
| 4 | Торговля (ритейл) | **ТЦ ГУМ** — заколдованный торговый пассаж: булыжная галерея волшебных лавок, висящие вывески (без текста), парящий товар, та же ажурная фасадная аркада |
| 5 | Престиж / статус | **Москва-Сити** — высокие готические шпили-башни гильдии волшебников с парящими мостами, престижный «адрес» магического мира |
| 6 | Производство | **Красный Октябрь** — узнаваемая краснокирпичная фабрика у реки → волшебный цех-кузница: зачарованная сборка, котлы-плавильни, трубы с цветным дымом, мастерские мётел и палочек |

Лор-фон: вечерний туман, алый паровой экспресс на виадуке, совы в небе, силуэт большого замка-школы на дальнем холме, парящие фонарики, искры магии в воздухе.

### Атрибуты предпринимателя (под волшебный сеттинг)

Лицо и личность героя **неизменны** (тот же молодой предприниматель, тёмные короткие волосы),
но снаряжение и навыки — из волшебного мира.

- **Навыки (панель игрока), базовый смысл сохранён:**
  - Идея → **«Искра волшебства»** — иконка палочка/искра;
  - Мотивация → **«Зов приключений»** — иконка сова/молния;
  - Бизнес-план → **«Магический свиток»** — иконка свиток/гримуар.
- **Образ/снаряжение героя (для промпта картинки):** современно-casual одежда под открытой мантией-плащом,
  светящаяся волшебная палочка (проецирует маленький план-заклинание), кожаный гримуар (бизнес-план)
  под мышкой, сова-компаньон на плече; стоит на светящемся рунном круге-печати (стартовая платформа).

### Промпт картинки (титул)
> ВАЖНО: на картинке НЕТ текста, надписей, букв, цифр, логотипов и UI-иконок/HUD —
> это чистый арт-фон. Весь текст и игровые значки накладываются поверх в вёрстке.
```
Cinematic fantasy key art in the spirit of a cozy magical wizarding-school saga (warm British
dark-academia fantasy, candlelit magic — NOT any trademarked franchise). A hidden magical
wizarding quarter of Moscow at misty evening: enchanted cobblestone streets, warm candle-glow
from windows, floating lanterns, drifting magic sparks, owls in the sky, a great spired
castle-school silhouette on a distant hill, a scarlet steam express crossing a stone viaduct.
Warm amber candlelight with emerald-green magic glow and deep ruby accents over an inky
blue-violet evening; volumetric god-rays, soft magical haze, shallow depth of field.
CLEAN PLATE — IMPORTANT: absolutely NO text, NO letters, NO numbers, NO captions, NO logos,
NO UI, NO HUD, NO icons and NO map pins/markers anywhere in the image; pure background art only.
Wide 16:9 widescreen isometric strategy-map composition.
HERO: ONE recurring character — the SAME young male entrepreneur, short dark hair, friendly
determined face (identical face in every style) — in modern casual clothes under an open wizard
robe/cloak, holding a glowing wand that projects a tiny plan, a leather grimoire under his arm,
a small owl companion on his shoulder; standing on a glowing rune-circle start platform in the
lower-left foreground, looking out over the magical town. He is the only person highlighted.
SIX KEY LOCATIONS across the enchanted isometric map — each keeps its recognizable real-world
silhouette but is reimagined as magical, softly glowing so a marker can be placed on top later:
  1) FOOD MARKET — Danilovsky Market as a covered enchanted bazaar: the same arched roofs but
     stained-glass, floating produce stalls, self-weighing scales, barrels of magical ingredients,
     owls under the vaults;
  2) SMALL CAFE — a cozy magical tavern-cafe with floating candles, self-stirring cups, steaming
     cauldron-kettles, warm glowing windows and a little terrace;
  3) R&D / INNOVATION — the "Lomonosov" cluster as a magical academy / alchemy college: spired
     towers, telescopes, glowing rune-laboratories, floating books;
  4) RETAIL — GUM, an enchanted ornate shopping arcade: a cobblestone gallery of wizarding shops,
     hanging signboards (no text), floating merchandise, the ornate facade kept;
  5) PRESTIGE / STATUS — Moscow-City as tall gothic wizard-guild spires with floating walkways,
     the prestige address of the magical world;
  6) PRODUCTION — Krasny Oktyabr (Red October), the red-brick riverside factory kept clearly
     recognizable, now an enchanted workshop-forge district: magical assembly, cauldron-foundries,
     chimneys with colored smoke, broom-and-wand workshops.
Arrange them at varied distances across a magical Moscow stretching into a misty, starlit horizon.
MOOD: wonder, warmth, cozy magic, adventure, enchantment.
QUALITY: ultra-high resolution, 8K, extremely sharp, crisp fine detail, high-DPI, clean,
made for a giant LED concert-hall screen. --ar 16:9 --quality 2
```
avoid: ANY text, letters, numbers, captions, logos, UI, HUD, icons, map pins/markers;
trademarked franchise logos or named characters; weapons, war, grim horror, flat 2D cartoon,
low detail, extra random people competing with the hero, different character face.

### Дизайн-система презентации (HTML)
- **Вайб:** тёплая магия при свечах, уютное волшебство, эпично-сказочно (dark academia).
- **Палитра:**
  - Фон: тёмный чернильно-сине-фиолетовый градиент (`#0e1320 → #1a1530`).
  - Акцент-1 (основной): тёплое свечное золото-янтарь `#E7B24C`.
  - Акцент-2: изумрудная магия `#2FB675`.
  - Акцент-3: рубин/бордо `#B5384B`.
  - Свет/блики: тёплый кремовый `#F3E7CC` + искры/частицы магии.
  - Текст: кремово-пергаментный `#F3E7CC` (на тёмном).
  - Панели: «пергамент-стекло» `rgba(28,22,16,.6)` + золотая кромка/завитки.
- **Шрифты:** заголовки — декоративный serif с засечками (напр. Cinzel/Marcellus, «магический»);
  тело — Rajdhani/EB Garamond. (Замена шрифта заголовков относительно текущего Orbitron.)
- **UI/HUD:** пергамент-панели, золотые уголки-завитки вместо строгих скобок, свечное свечение,
  парящие искры/частицы, лёгкая «магическая дымка».
- **Карта/маршрут/объекты:** маршрут — золотая светящаяся тропа (как след заклинания); контуры
  объектов — изумрудно-золотое свечение; маркер-замочек можно заменить на печать-сигил или оставить гекс с золотом.
- **Достижения:** золото `#E7B24C` или изумруд `#2FB675` — оба ложатся в палитру.

---

## Стиль 4 — «Мир крошечных тех-помощников» (в духе «Фиксиков», яркий мультяшный хайтек)

Вселенная: в духе детского мультсериала о крошечных человечках-помощниках, которые живут внутри
техники и всё чинят. Тон: яркий дружелюбный мультяшный 3D, позитив, «всё чинится».
Сцена — **Москва глазами крошечного фикси**: город собран из гигантской техники, плат,
шестерёнок и проводов; герой — маленький предприниматель-фикси.

> ⚠️ В промпте для генератора НЕ используем торговое имя «Фиксики»/«Fixies» и имена персонажей —
> фильтры режут. Пишем «in the spirit of a kids' show about tiny tech-helper creatures living inside gadgets».

### Объекты мира (6 архетипов в мире техники)

Узнаваемый силуэт исходного места сохраняем, но собираем его **из техники** (гаджеты, платы, шестерёнки, провода).

| # | Архетип | Объект в мире фиксиков |
|---|---------|------------------------|
| 1 | Рынок (продуктовый) | **Даниловский рынок** — тех-базар запчастей: те же арки, но крыша из плат-витражей, лотки из открытых гаджетов, детальки в ящиках как продукты, катушки и резисторы горками |
| 2 | Питание (кафе) | **Кафе** — уютное кафе на корпусе кофемашины/тостера: пар, тёплые лампочки-индикаторы, «капля» припоя, столики из крышечек |
| 3 | Исследования и инновации | **Кластер «Ломоносов»** — лаборатория-материнка: кампус из микросхем, светящийся процессор, колбы + провода, R&D-стенды (исследования = тех-инновации) |
| 4 | Торговля (ритейл) | **ТЦ ГУМ** — пассаж из рядов гаджетов и экранчиков: ажурный фасад из дорожек платы, витрины-дисплеи, парящий товар-деталька |
| 5 | Престиж / статус | **Москва-Сити** — небоскрёбы из стопок устройств и гигантских процессоров со светящимися окнами-LED — престижный тех-«адрес» |
| 6 | Производство | **Красный Октябрь** — узнаваемая краснокирпичная фабрика → завод гаджетов: шестерёнки, конвейеры, роботы-манипуляторы собирают приборы, кирпич = красная плата |

Лор-фон: гигантские бытовые предметы (огромная лампа = «солнце», большие винты и болты, провода-кабели как дороги/эстакады, ряды LED как огни города, крутящиеся шестерёнки), яркое мультяшное небо.

### Атрибуты предпринимателя (под мир фиксиков)

⚠️ **Важно про героя в этом мире:** фикси — **не человек**, поэтому общее правило «один и тот же
реалистичный человек-предприниматель» здесь НЕ работает (иначе ИИ рисует обычного мальчика, как и вышло).
В мире Фиксиков герой = **существо-фикси**: стилизованная большая голова, **яркие торчащие волосы-антенна**,
большие глаза, **три пальца**, обтягивающий цветной комбинезон с **эмблемой-ладошкой** на груди,
ранец-помогатор; умеет сворачиваться в винтик. Узнаваемость держим через тёмные торчащие волосы и
дружелюбное лицо, а не через фотореалистичную внешность.

- **Навыки (панель игрока), базовый смысл сохранён:**
  - Идея → **«Смекалка»** — иконка лампочка/шестерёнка;
  - Мотивация → **«Тыдыщ!»** (фикси-запал) — иконка молния/искра;
  - Бизнес-план → **«Схема»** — иконка чертёж/плата.
- **Образ/снаряжение героя (для промпта картинки):** существо-фикси в обтягивающем цветном комбинезоне
  с эмблемой-ладошкой, ранец-«помогатор», рука-инструмент (отвёртка/ключ); стоит на круглой светящейся
  стартовой платформе-кнопке (как большая кнопка прибора).
- **Арт-стиль (критично):** **плоская 2D cel-рисовка** — как кадр из рисованного 2D-мультсериала
  (матовые плоские цвета, простые формы, жирный контур, минимум градиентов). **НЕ 3D-рендер, не объём,
  не глянец, не Pixar-фотореализм, не реалистичный металл** (как на втором скрине — так НЕ надо;
  как на первом скрине-кадре сериала — так НАДО).

### Промпт картинки (титул)
> ВАЖНО: на картинке НЕТ текста, надписей, букв, цифр, логотипов и UI-иконок/HUD —
> это чистый арт-фон. Весь текст и игровые значки накладываются поверх в вёрстке.
```
Bright friendly FLAT 2D CEL-SHADED TV-CARTOON key art — looks like a frame from a hand-drawn 2D
animated kids series in the spirit of a show about tiny tech-helper creatures who live inside
gadgets and fix machines (NOT any trademarked franchise). STYLE IS CRITICAL: FLAT 2D cartoon,
matte colors, simple clean rounded shapes, THIN CLEAN SOFT OUTLINES (NOT heavy black comic ink),
SOFT cel-shading with subtle gentle gradients, a calm softer palette with a few accent colors
(NOT everything over-saturated), CLEAN UNCLUTTERED composition with breathing space — few simple
readable elements per building, plenty of clean empty grass/ground. Classic gentle 2D TV-animation look.
NOT 3D render, NOT a volumetric/isometric 3D model, NOT glossy, NOT Pixar-realistic, NOT
photorealistic, NO realistic metal/plastic textures, NO realistic reflections, NOT hyper-detailed,
NOT busy/cluttered, NO heavy black outlines.
A cheerful miniature world seen at tiny-helper scale: an isometric city of Moscow rebuilt from
oversized everyday TECHNOLOGY and real household devices — big screws and bolts, gears, glowing
boards, cables and wires used as roads and bridges, LEDs as city lights, a huge desk-lamp glowing
like a warm sun. Saturated primary palette — sky-blue, lime-green, sunny yellow and orange,
playful and optimistic. NO weapons, NO violence.
CLEAN PLATE — IMPORTANT: absolutely NO text, NO letters, NO numbers, NO captions, NO logos,
NO UI, NO HUD, NO icons and NO map pins/markers anywhere in the image; pure background art only.
Wide 16:9 widescreen, drawn as a FLAT 2D map illustration (top-down / gently isometric layout),
NOT a 3D model and NOT a rendered scene.
HERO: ONE recurring character — a small friendly tech-HELPER CREATURE (NOT a realistic human, NOT
a normal human boy): a flat 2D cartoon being with a big rounded head, BRIGHT SPIKY ANTENNA-LIKE
HAIR, big round eyes, a wide friendly smile, three-fingered gloved hands, wearing a colorful
skin-tight one-piece tech-suit with a small HAND-SYMBOL emblem on the chest and a little gadget
backpack; he can curl into a screw/bolt shape. Keep his recurring identity across styles via the
dark spiky hair and the same friendly face. Standing on a glowing round push-button start platform
in the lower-left foreground, looking out over the tech world. He is the only character highlighted.
SIX KEY LOCATIONS across the gadget-world isometric map — each keeps its recognizable real-world
silhouette but is rebuilt from technology, softly glowing so a marker can be placed on top later:
  1) FOOD MARKET — Danilovsky Market as a spare-parts tech-bazaar: the same arched roofs but made
     of board-glass, stalls from opened gadgets, bins of little components sorted like produce;
  2) SMALL CAFE — a cozy cafe built on a coffee-machine/toaster body: steam, warm indicator bulbs,
     a drop of solder, tables from bottle-caps;
  3) R&D / INNOVATION — the "Lomonosov" cluster as a motherboard laboratory campus: microchip
     buildings, a glowing CPU tower, flasks wired to circuits, research benches;
  4) RETAIL — GUM as an arcade built from rows of gadgets and little screens: an ornate facade of
     board-traces, display-window screens, floating component-merchandise;
  5) PRESTIGE / STATUS — Moscow-City as skyscrapers built from stacked devices and giant processors
     with glowing LED windows — the prestige tech address;
  6) PRODUCTION — Krasny Oktyabr (Red October), the red-brick riverside factory kept recognizable,
     now a gadget-assembly plant: gears, conveyor belts, robotic arms building devices, brick = red
     board.
Arrange them at varied distances across a bright cheerful tech-Moscow stretching to the horizon —
keep the layout CLEAN and READABLE, simple shapes, not crowded, with calm empty space between objects.
MOOD: fun, friendly, bright, inventive, optimistic — everything can be fixed.
QUALITY: high-resolution and clean, but keep FLAT 2D CEL-SHADED CARTOON look — flat matte colors,
simple shapes, bold outlines; NOT 3D render, NOT photoreal, NOT glossy, NOT hyper-detailed;
made for a giant LED concert-hall screen. --ar 16:9 --quality 2
```
avoid: ANY text, letters, numbers, captions, logos, UI, HUD, icons, map pins/markers;
trademarked franchise logos or named characters; 3D render, 3D model, isometric 3D, volumetric
rendering, glossy surfaces, realistic reflections/lighting; realistic human, normal human boy,
photorealistic or Pixar-realistic render, realistic metal/plastic textures; heavy black outlines,
comic-book ink, over-saturated everything, busy cluttered hyper-detailed scene; weapons, war,
scary/grim mood, extra random people competing with the hero, different character face.

### Дизайн-система презентации (HTML)
- **Вайб:** яркий дружелюбный мультяшный хайтек, позитив, «всё чинится» (детский, но не инфантильный).
- **Палитра:**
  - Фон: светлый бирюзово-голубой градиент (`#dff3fb → #c9ecff`).
  - Акцент-1 (основной): голубой `#29B6F6`.
  - Акцент-2: лайм `#8BC34A`.
  - Акцент-3: солнечно-жёлтый `#FFC42B`.
  - Доп-акцент: оранж `#FF6A3D` (кнопки/ачивки).
  - Текст: тёмный графит `#15202B` (на светлом).
  - Панели: яркое матовое «приборное» стекло `rgba(255,255,255,.7)` + толстый цветной контур, винтики по углам.
- **Шрифты:** заголовки — округлый дружелюбный гротеск (напр. Baloo 2 / Fredoka, мультяшный округлый);
  тело — Nunito / Rajdhani. (Замена шрифта заголовков относительно текущего Orbitron.)
- **UI/HUD:** толстые скруглённые контуры, панельки с заклёпками-винтиками и лампочками-индикаторами,
  шестерёнки-декор; всё яркое, округлое, «как приборная панель игрушки».
- **Карта/маршрут/объекты:** маршрут — провод/кабель с бегущими импульсами тока; контуры объектов —
  яркая голубо-жёлтая обводка; маркер-замочек заменить на **винтик/шестерёнку или болт-гекс**.
- **Достижения:** жёлтая звезда-награда `#FFC42B` или оранж `#FF6A3D` — «бейдж фиксика».

---

## Стиль 5 — «Остров сокровищ» (сатирический рисованный 2D пиратский мультфильм)

Вселенная: в духе задорного сатирического рисованного 2D мультфильма про пиратов и поиск клада
(приключение «Остров сокровищ», Р. Л. Стивенсон). Тон: юмор, гротеск-карикатура, жирная чернильная
обводка, плоские яркие гуашевые цвета, морские приключения.
Сцена — **старая пиратская карта сокровищ**: Москва нарисована как портовый пиратский мир,
6 объектов — локации на карте, маршрут — пунктир к «X», вокруг море и тропический остров.

> ⚠️ В промпте для генератора: «Treasure Island» (Стивенсон) — public domain, можно. НЕ используем
> названия студий/торговые марки конкретного мультфильма. Пишем «in the spirit of a satirical
> hand-drawn 2D Soviet-style pirate cartoon».

### Объекты мира (6 архетипов в пиратском сеттинге)

Узнаваемый силуэт исходного места сохраняем, оболочку — пиратскую (порт, таверна, верфь, форт, рынок).

| # | Архетип | Объект в пиратском мире |
|---|---------|--------------------------|
| 1 | Рынок (продуктовый) | **Даниловский рынок** — портовый базар: те же арки как большой парусиновый навес-тент, лотки с экзотикой, бочки, попугаи, мешки и ящики с товаром |
| 2 | Питание (кафе) | **Кафе** — приморский кабак-таверна: бочки рома, фонари, весёлый кок, столики на пристани, чайки |
| 3 | Исследования и инновации | **Кластер «Ломоносов»** — обсерватория навигатора / мастерская корабельного инженера: телескопы, карты, чертежи, чудаковатый профессор-изобретатель (R&D = исследования) |
| 4 | Торговля (ритейл) | **ТЦ ГУМ** — большой торговый дом / колониальная купеческая галерея: ажурный фасад, лавки, вывески (без текста), поток покупателей |
| 5 | Престиж / статус | **Москва-Сити** — губернаторский форт / богатый особняк на холме с мачтами и флагами — престижный «адрес» порта |
| 6 | Производство | **Красный Октябрь** — узнаваемая краснокирпичная фабрика → верфь и доки: строят корабли, льют пушки, бьют бочки, склады (производство) |

Лор-фон: море вокруг, парусник типа «Испаньолы» под парусами, тропический остров-клад на горизонте,
пальмы, роза ветров (компас), пунктирный маршрут к «X», чайки и попугаи, шуточные морские чудища-завитушки.

### Атрибуты предпринимателя (под пиратский сеттинг)

Лицо и личность героя **неизменны** (тот же молодой предприниматель, тёмные короткие волосы),
показан в рисованном 2D-стиле и в образе юнги-искателя.

- **Навыки (панель игрока), базовый смысл сохранён:**
  - Идея → **«Нюх на сокровища»** — иконка компас/самоцвет;
  - Мотивация → **«Жажда приключений»** — иконка парус/ветер;
  - Бизнес-план → **«Карта сокровищ»** — иконка свиток-карта с «X».
- **Образ/снаряжение героя (для промпта картинки):** юнга/моряк — полосатая тельняшка или жилет, кушак,
  треуголка или матросская шапка, свёрнутая карта-сокровищ (бизнес-план) и компас в руках,
  маленький попугай-компаньон на плече; стоит на «СТАРТЕ» карты — отметке «X» / на причале.

### Промпт картинки (титул)
> ВАЖНО: на картинке НЕТ текста, надписей, букв, цифр, логотипов и UI-иконок/HUD —
> это чистый арт-фон. Весь текст и игровые значки накладываются поверх в вёрстке.
```
Satirical hand-drawn 2D cartoon key art in the spirit of a classic Soviet-style pirate adventure
animation ("Treasure Island" by R. L. Stevenson — public domain; NOT any trademarked studio).
A big old pirate TREASURE MAP: an isometric/top-down hand-drawn map of Moscow reimagined as a
cheerful pirate port-world, drawn with bold black ink outlines and flat bright gouache colors,
exaggerated comic caricature style. Aged parchment-map texture, a sea all around with a sailing
ship (Hispaniola-type) under full sails, a tropical treasure island on the horizon, palm trees,
a compass rose, a dashed treasure route leading to a big "X", seagulls and parrots, playful
sea-monster doodles. Warm sea-adventure mood, sunny. NO real weapons-violence (comic cartoon only).
CLEAN PLATE — IMPORTANT: absolutely NO text, NO letters, NO numbers, NO captions, NO logos,
NO UI, NO HUD, NO icons and NO map pins/markers anywhere in the image; pure background art only.
Wide 16:9 widescreen composition.
HERO: ONE recurring character — the SAME young male entrepreneur, short dark hair, friendly
determined face (identical face in every style), drawn in this 2D cartoon style — as a young
cabin-boy/sailor in a striped shirt or vest with a sash and a sailor cap, holding a rolled
treasure map and a compass, a small parrot companion on his shoulder; standing on the START of
the map (a marked dock / an "X") in the lower-left foreground, looking out over the pirate world.
He is the only person highlighted.
SIX KEY LOCATIONS across the hand-drawn pirate map — each keeps its recognizable real-world
silhouette but is reimagined as a pirate-world place, clearly drawn so a marker can be placed on top later:
  1) FOOD MARKET — Danilovsky Market as a portside bazaar: the same arches as a big canvas awning,
     stalls of exotic goods, barrels, sacks and crates, parrots;
  2) SMALL CAFE — a seaside tavern/kabak: rum barrels, lanterns, a jolly cook, dockside tables, gulls;
  3) R&D / INNOVATION — the "Lomonosov" cluster as a navigator's observatory / ship-engineer
     workshop: telescopes, charts, blueprints, a quirky inventor-professor;
  4) RETAIL — GUM as a grand colonial trading house / merchant gallery: an ornate facade, shop
     stalls, hanging signboards (no text), a flow of customers;
  5) PRESTIGE / STATUS — Moscow-City as the governor's fort / rich mansion on a hill with masts and
     flags — the prestige address of the port;
  6) PRODUCTION — Krasny Oktyabr (Red October), the red-brick riverside factory kept recognizable,
     now a shipyard and docks: ships under construction, forged cannons, barrel-making, warehouses.
Arrange them at varied distances across a hand-drawn pirate Moscow surrounded by sea.
MOOD: fun, adventurous, satirical, warm, treasure-hunt spirit.
QUALITY: ultra-high resolution, 8K, extremely sharp, crisp fine detail, high-DPI, clean,
made for a giant LED concert-hall screen. --ar 16:9 --quality 2
```
avoid: ANY text, letters, numbers, captions, logos, UI, HUD, icons, map pins/markers;
trademarked studio logos or named characters; real gore/violence, photoreal 3D, low detail,
extra random people competing with the hero, different character face.

### Дизайн-система презентации (HTML)
- **Вайб:** задорный сатирический ретро-мультфильм, морские приключения, юмор, «карта сокровищ».
- **Палитра:**
  - Фон: состаренный пергамент-карта (`#f0e2c0 → #e3cfa0`); для неба/моря — морская бирюза.
  - Акцент-1 (основной): морская бирюза/тиал `#1FA6A0`.
  - Акцент-2: золото монет `#E8B73A`.
  - Акцент-3: пиратский алый/бордо `#C0392B`.
  - Контур/обводка: чернильно-чёрный `#20140A` (жирная рисованная линия).
  - Текст: тёмно-коричневые чернила `#2A1B0E` (на пергаменте).
  - Панели: «свиток/пергамент» с рваными краями, чернильная рамка, потёртости, сургучная печать.
- **Шрифты:** заголовки — винтажный/рисованный с засечками (напр. Pirata One / IM Fell English);
  тело — гуманистический (EB Garamond / Rajdhani). (Замена шрифта заголовков относительно Orbitron.)
- **UI/HUD:** панели-свитки и пергамент, сургучные печати, роза ветров как декор, верёвочные рамки,
  чернильные штрихи/кляксы, лёгкая «состаренность» бумаги.
- **Карта/маршрут/объекты:** маршрут — **пунктир сокровищ** с «X» в конце; контуры объектов —
  чернильная обводка + лёгкое золотое свечение; маркер-замочек заменить на **компас / сундучок / печать-череп**.
- **Достижения:** золото монет `#E8B73A` / сундук с сокровищами.
