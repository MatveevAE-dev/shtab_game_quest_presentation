# Промпт фоновой картинки — «Масштабирование ресторанного бизнеса» (LED 7680×2592)

Вариант фон-арта на ту же сцену «Дневная летняя Москва», но с **сюжетом роста ресторанного
бизнеса**: путь предпринимателя от кофейной точки до фабрики-кухни. Все прежние объекты
сохраняются, плюс добавлена линейка общепита по возрастанию масштаба.

- **Стиль:** «Дневная летняя Москва» (та же база, что у `prompt_fon_dnevnaya_moskva.md`).
- **Размер:** **7680×2592 px (2,96:1)** — сверхширокая панорама, НЕ 16:9.
- **Идея:** сюжет роста бизнеса задают **типы объектов** (не размер): кофе на вынос (мобильный
  киоск) → кафе → сеть кафе (разбросана по углам города) → завод по производству еды (за
  городом). Размеры не важны — объекты должны **гармонично** вписываться в кадр.
- **Вид:** сверху (с высоты здания), объекты на разных улицах/кварталах.
- **Без вывесок** — никаких табличек/бордов; названия подведов накладываем в HTML.
- **ДПИР** — центральный городской хаб экосистемы (по центру района).
- **Референсы:** к промпту прикрепляем 4 скрина реальных зданий (Фабрика Подарков,
  Москва-Сити, мэрия-Штаб, кластер Ломоносов) — в промпте ссылаемся на них по номеру.

## Какие картинки прикрепить (по порядку)

1. **Фабрика Подарков** — стеклянный павильон-оранжерея с зелёным каркасом и аркой-куполом.
2. **Москва-Сити** — небоскрёбы.
3. **Мэрия Москвы** (красное здание, Тверская 13) = Штаб.
4. **Кластер «Ломоносов»** — современный научный кластер.

---

## Готовый промпт (вставлять в генератор)

```
Cinematic AAA video-game key art, ultra-wide panoramic city vista, aspect ratio 2.96:1
(7680×2592), 8K. HIGH ELEVATED AERIAL view AS SEEN FROM A ROOFTOP where the hero stands: the
camera looks OUT and DOWN over the whole district (oblique bird's-eye, like a drone shot from
building height), NOT a flat top-down map and NOT a street-level view. The HORIZON and the SKY
are clearly visible across the TOP of the frame (blue summer sky with soft clouds). All
buildings sit on walkable ground at a realistic, consistent scale (route between objects will
be drawn later in code — DO NOT draw any path, line, arrow, pin or marker).

REFERENCE IMAGES — 4 photos are attached. They are the GROUND TRUTH for these 4 buildings.
Reproduce each building EXACTLY as in its photo — same silhouette, proportions, number of
floors, roof shape, materials and colors. Do NOT redesign, stylize or invent details, and do
NOT rely on the short text labels (they only tell you WHICH building is which). Where the text
and the photo differ, ALWAYS FOLLOW THE PHOTO. Only adapt lighting/angle to fit this aerial
summer scene; keep the architecture faithful.
  image 1 = Gift Factory,  image 2 = Moscow City,  image 3 = City Hall / Штаб,
  image 4 = Lomonosov cluster.
For the best likeness, draw these 4 buildings prominently enough (not tiny) and roughly
front-facing, so their recognizable features from the photos are clearly readable.

SETTING: lively SUMMER daytime Moscow at golden hour — lush green parks, tree-lined
boulevards, squares, fountains, warm low sun, long dramatic shadows, vivid blue sky with soft
clouds. BRIGHT, CONTRASTY, SATURATED summer palette: fresh green (#2FAF6E), warm gold (#F4B740),
sky-blue (#6CC0E5) — punchy colors, high contrast, cinematic and eye-catching, not flat or dull.

STORY — the TYPES of the food businesses (NOT their size) tell the story of a growing business:
it starts with a mobile coffee-to-go kiosk, then a small cafe, then a chain of identical cafes
spread across different corners of the city, and finally a food-production factory on the
outskirts. Sizes do NOT need to grow — every object should sit HARMONIOUSLY and naturally in
the frame, well integrated into the city, not forced or oversized.

OBJECTS — there are 15 TARGET objects listed below. IMPORTANT: keep them at a REALISTIC,
NATURAL scale — they are normal buildings, NOT oversized giants, NOT a toy/diorama. They must
match the size of real buildings around them. The way to make them readable is NOT by enlarging
them but by REDUCING THE NUMBER of other buildings: keep the surrounding city sparse — fewer
background buildings, more greenery, parks and open space between the targets. Just enough city
to feel real, not a dense crowded skyline. Scatter the targets across the frame at different
depths and on different streets. DO NOT cluster them, DO NOT line them up in a row, DO NOT pack
them on one plaza. This list is ONLY a description for you — do NOT write or draw any of these
numbers/labels in the image (the list uses dashes on purpose). Objects, in rough left→right
reading order (NOT a row):
- HERO: one young male entrepreneur (dark short hair, light casual t-shirt, friendly),
  shown FULL BODY (head to feet), standing ON A ROOFTOP TERRACE / balcony in the BOTTOM-LEFT
  corner of the frame, looking OUT over the city (this rooftop is the camera's vantage point).
  He must be FULLY INSIDE the frame, NOT cropped by the edges — leave a small margin around
  him. NO platform, NO podium, NO glowing circle — just a person on the rooftop holding a
  coffee cup.
- COFFEE-TO-GO — a MOBILE coffee-to-go kiosk / coffee cart with a bright colored awning,
  standing on the sidewalk RIGHT NEXT TO THE HERO in the foreground. Make it clearly visible
  and identifiable (the hero holds a coffee cup — this is his first business).
- CAFE — a cafe with a small OUTDOOR TERRACE: a few tables and just a FEW (2-3) colored
  umbrellas — NOT crowded with umbrellas. A colored awning over the entrance. In the
  FOREGROUND / near the hero.
- CAFE CHAIN — THREE IDENTICAL cafes with the SAME recognizable look (same colored awning,
  small terrace with only a couple of umbrellas), each placed in a DIFFERENT CORNER of the
  frame (one cafe per corner, 3 separate corners, far apart, NOT next to each other) — the
  same brand repeated across the city, each clearly visible.
- FOOD FACTORY (завод по производству еды) — a food-production plant with loading docks,
  placed on the OUTSKIRTS / edge of the city, OUTSIDE the dense built-up area (in an
  industrial zone / open land at the border of the frame) — this reads more logically.
- DPIIR CITY HUB (Департамент / ДПИР) — a prominent modern civic / digital HUB building, the
  control center of the city's entrepreneurship ecosystem, standing roughly in the MIDDLE of
  the district as a landmark.
- OFFICE BUSINESS CENTER (МБМ) — modern mid-rise office building.
- BEAUTY SALON — typical ground-floor shopfront.
- BANK BUILDING (ФСК) — separate classic bank with columns/portico.
- SHOP / STORE — typical ground-floor retail with a display window.
- OFFICE BUILDING (ФПСП) — typical office block.
- LOMONOSOV CLUSTER — reproduce EXACTLY from the Lomonosov reference photo (no text guessing).
- CITY HALL / Штаб — reproduce EXACTLY from the City Hall reference photo (no text guessing).
- GIFT FACTORY — reproduce EXACTLY from the Gift Factory reference photo (no text guessing).
- MOSCOW CITY — reproduce EXACTLY from the Moscow City reference photo; place it in the
  FAR-RIGHT corner as the tallest point, with the MOSCOW RIVER curving in front of it.

REAL landmarks (Lomonosov cluster, City Hall, Gift Factory, Moscow City) must match their
ATTACHED REFERENCE IMAGES — standalone, recognizable buildings. The TYPICAL objects (coffee
kiosk, cafe, cafe chain, office center, beauty salon, shop, ФПСП office) are logically built
into ordinary Moscow city blocks. The bank (ФСК) is a separate building, and the food factory
sits on the city outskirts.

CLEAN PLATE — absolutely NO text, NO captions, NO letters, NO NUMBERS, NO numbered markers or
badges, NO callouts, NO labels, NO UI, NO HUD, NO icons, NO route lines, NO pins, NO map
markers, NO sign boards. Do NOT annotate or number the buildings. Buildings recognizable by
ARCHITECTURE only.

IMPORTANT — FOOD BUSINESSES MUST BE VISIBLE: the coffee-to-go kiosk, the cafe and the 3 cafes
of the chain are KEY focal points of the story. Do NOT let them get lost or hidden among the
big buildings. Place the kiosk and the first cafe LARGE and clearly readable in the FOREGROUND
near the hero (lower part of the frame), and give every cafe a colored awning and a small
terrace with only a FEW umbrellas (not a sea of umbrellas) so they read clearly from above.
The 3 chain cafes must be findable in different corners.

AVOID: a toy / diorama / miniature look; oversized giant target buildings out of scale with
their surroundings; a showroom row of buildings; targets packed side by side. ALSO AVOID an
over-crowded skyline that drowns the targets — instead reduce the COUNT of background buildings.
AVOID a flat top-down map with no sky. AVOID too many umbrellas / a "sea of parasols" on the
cafe terraces — only a few per cafe. Do not hide the small food businesses — keep them visible
at a natural scale.

Render: highly CINEMATIC — dramatic golden-hour light, strong sun rays, rich contrast, deep
shadows and bright highlights, vivid saturated colors (lush greens, warm gold, vibrant sky-blue
water and sky), cinematic color grading, atmospheric depth/haze, lens-flare and god-rays,
glossy highlights on glass. High detail, AAA game key art quality, 8K. Bold, punchy, eye-catching.
```

---

## Чем отличается от базового промпта

- **Сюжет роста задают типы объектов** (не размер): кофе-киоск → кафе → сеть кафе → завод.
- Добавлены объекты: **кофе на вынос (мобильный киоск)**, **сеть кафе**, **завод по производству еды (за городом)**.
- Все прежние объекты сохранены (МБМ, салон, ФСК, магазин, ФПСП, Ломоносов,
  мэрия-Штаб, Фабрика Подарков, Москва-Сити с рекой).

## Чек-лист перед приёмкой картинки

- [ ] Кофе-киоск, кафе и сеть кафе ЧЁТКО ВИДНЫ (яркие тенты/зонтики, столики), не потерялись.
- [ ] Киоск и первое кафе — крупно в переднем плане рядом с героем.
- [ ] Сюжет задают типы объектов: кофе-киоск → кафе → сеть кафе → завод; размеры не важны.
- [ ] Сеть кафе = 3 одинаковых (один фасад), РАЗБРОСАНЫ по разным углам города, не вместе.
- [ ] Завод по производству еды вынесен ЗА город (окраина/промзона), не в центре.
- [ ] Объекты в реалистичном масштабе, НЕ гиганты, не игрушечно/диорамно.
- [ ] Меньше именно КОЛИЧЕСТВА фоновых зданий (зелень/открытое пространство), а не раздувание объектов.
- [ ] Объекты разбросаны по кадру, не в один ряд и не кучей; не тонут в плотной застройке.
- [ ] Ракурс: высокий аэро-вид С КРЫШИ (где стоит герой), смотрим вдаль и вниз; вверху видно небо и горизонт.
- [ ] Герой во весь рост на крыше в левом углу, НЕ обрезан краями, без платформы/свечения.
- [ ] Кинематографично: яркие контрастные насыщенные краски, золотой час, лучи/блики, глубина.
- [ ] Москва-река у Москва-Сити (правый угол).
- [ ] Нет ни одной читаемой буквы/надписи; нет вывесок/табличек вообще.
- [ ] НЕТ цифр/номеров/меток на объектах (ИИ не должен нумеровать здания).
- [ ] Нет маршрутов, пинов, маркеров, UI/HUD.
- [ ] Реальные объекты совпадают с прикреплёнными референсами (4 скрина) и узнаваемы.
- [ ] Формат 2,96:1, объекты стоят на земле (не парят).
