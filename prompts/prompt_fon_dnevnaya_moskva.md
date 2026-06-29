# Промпт фоновой картинки — «Дневная Москва» (LED 7680×2592)

Фон-арт для экрана мероприятия «На одной волне – 2026». Единый clean-plate для всех
презентаций подведов блока МСП. Поверх в HTML накладываются 3 зоны и текст; при показе
PDF фон блюрится. Поэтому в самой картинке **нет ни текста, ни UI, ни маршрутов**.

- **Стиль:** только один — «Дневная летняя Москва» (база — `generate_styled_presentation.md`).
- **Размер:** **7680×2592 px (соотношение 2,96:1)** — сверхширокая панорама, НЕ 16:9.
- **Без вывесок** — никаких табличек/бордов; названия подведов накладываем в HTML.
- **ДПИР** — центральный городской хаб экосистемы (по центру района).

---

## Готовый промпт (вставлять в генератор)

```
Cinematic AAA video-game key art, ultra-wide panoramic city map, aspect ratio 2.96:1
(7680×2592), 8K. HIGH BIRD'S-EYE VIEW — camera looks DOWN onto the city from rooftop height
(elevated aerial, top-down-ish), NOT a street-level view. A whole CITY DISTRICT with several
streets, squares and blocks visible below, so every building sits on walkable ground (route
between objects will be drawn later in code — DO NOT draw any path, line, arrow, pin or marker).

SETTING: lively SUMMER daytime Moscow at golden hour — lush green parks, tree-lined
boulevards, squares, fountains, warm low sun, long soft shadows, clear blue sky. Warm summer
palette: fresh green (#2FAF6E), warm gold (#F4B740), sky-blue (#6CC0E5), light airy background.

OBJECTS — spread across DIFFERENT streets and blocks of the district (NOT lined up on one
street, NOT in a row). Each on its own street/corner/square, but all reachable on foot.
Rough left→right reading order:
1. HERO: one young male entrepreneur (dark short hair, light casual t-shirt, friendly),
   standing on a city square / rooftop terrace in the BOTTOM-LEFT (NO platform, NO podium,
   NO glowing circle — just a person standing in the urban scene).
2. CAFE — typical small business in the ground floor of a residential building, summer terrace.
3. DPIIR CITY HUB (Департамент / ДПИР) — a prominent modern civic / digital HUB building, the
   control center of the city's entrepreneurship ecosystem, standing roughly in the MIDDLE of
   the district as a landmark.
4. OFFICE BUSINESS CENTER (МБМ) — modern mid-rise office building.
5. BEAUTY SALON — typical ground-floor shopfront.
6. BANK BUILDING (ФСК) — separate classic bank with columns/portico.
7. SHOP / STORE — typical ground-floor retail with a display window.
8. OFFICE BUILDING (ФПСП) — typical office block.
9. PRODUCTION — small typical workshop / mini-factory with a chimney.
10. GUM — REAL recognizable historic Moscow trade arcade facade (long glass-roof galleries).
11. LOMONOSOV CLUSTER — REAL recognizable modern Moscow science/innovation cluster building.
12. CITY HALL of Moscow (Tverskaya 13) — REAL recognizable red classical government building.
13. GIFT FACTORY — REAL recognizable distinctive factory landmark.
14. MOSCOW CITY — REAL recognizable cluster of glass skyscrapers in the FAR-RIGHT corner,
    the visual climax / tallest point, with the MOSCOW RIVER curving in front of it
    (embankment, bridges, water reflecting the sky).

REAL landmarks (GUM, Lomonosov cluster, City Hall, Gift Factory, Moscow City) must look like
their real-world originals — standalone, recognizable buildings. The TYPICAL objects (cafe,
office center, beauty salon, shop, ФПСП office, production) are logically built into ordinary
Moscow city blocks. The bank (ФСК) is a separate building.

CLEAN PLATE — absolutely NO text, NO captions, NO letters, NO UI, NO HUD, NO icons, NO route
lines, NO pins, NO map markers, NO sign boards. Buildings recognizable by ARCHITECTURE only.

Render: cinematic lighting, soft warm shadows, high detail, AAA game key art quality, 8K.
```

---

## Что изменено относительно старого промпта

- **Вид сверху** (с высоты здания, аэро-ракурс вниз), а не с улицы.
- Объекты **на разных улицах и кварталах**, не в один ряд по одной улице.
- Герой — **без игровой платформы/подиума/свечения**: просто молодой предприниматель в сцене.
- **Москва-река** перед Москва-Сити (набережная, мосты, отражение неба).
- Герой — **внизу слева**; **Москва-Сити в правом углу**, кульминация.
- **13 объектов новой линейки**; сверхширокий **2,96:1 (7680×2592)**, не 16:9.

## Чек-лист перед приёмкой картинки

- [ ] Вид сверху (с высоты), не уличный.
- [ ] Объекты разнесены по разным улицам/кварталам, не в один ряд.
- [ ] Герой без платформы/свечения — обычный человек в городе, внизу слева.
- [ ] Москва-река у Москва-Сити (правый угол).
- [ ] Нет ни одной читаемой буквы/надписи; нет вывесок/табличек вообще.
- [ ] Нет маршрутов, пинов, маркеров, UI/HUD.
- [ ] 13 объектов присутствуют; реальные (ГУМ, Ломоносов, мэрия, Фабрика Подарков, Сити) узнаваемы.
- [ ] Формат 2,96:1, объекты стоят на земле (не парят).
