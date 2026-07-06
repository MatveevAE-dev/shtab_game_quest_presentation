# Промпт: герой за столиком кафе (слайд «Кафе открыто», `cafe-3.png`) — cutout со столом

## Идея и способ размещения
- Герой **сидит за столиком своего кафе, пьёт кофе и читает газету**, обычная повседневная одежда.
- **Генерим героя ВМЕСТЕ со столом + стулом + чашкой кофе + газетой** — как ОДНУ группу на
  **прозрачном фоне** (PNG, alpha). Фон сцены не нужен — он уже есть в `cafe-3.png`.
- **Ставим группу поверх 2-го столика слева** на веранде `cafe-3.png` (перекрывает старый пустой стол).
- **Почему со столом:** тогда стол стоит ПЕРЕД ногами героя (правильное перекрытие), кофе на столе,
  газета в руках. Если генерить «только героя» — существующий стол окажется позади, и ноги лягут
  поверх стола (выглядит, будто сидит на столе). Со своим столом стыковать пиксель-в-пиксель не надо —
  важно попасть в **перспективу и свет** сцены.

## Как использовать
- **Референс лица/личности:** `presentation/assets/img/objects/hero-cutout.png` (та же личность —
  молодой парень, тёмные короткие волосы, лёгкая щетина). Берём лицо/черты.
- **Референс стиля стола/стульев и света:** приложи `cafe-3.png` — стол должен быть как на веранде
  (круглый деревянный бистро-столик, венские/ротанговые стулья), свет **тёплый, слева** (как в сцене).
- Нужен **прозрачный фон**, вся группа целиком (стол + стул + герой), с ногами/полом — чтобы
  «поставить» на плитку веранды.

## Промпт (EN)
```
Photorealistic cutout of a young man SEATED at a small cafe table, TOGETHER WITH his table and
chair, ISOLATED on a fully TRANSPARENT background (alpha PNG) — no background scene, nothing behind,
just the seated man with his table set. Top-tier photoreal rendering, sharp detail, natural skin,
cinematic quality.

SAME PERSON as the reference image (keep him perfectly consistent): a slim, athletic man in his
mid-to-late 20s, fair skin with a light mixed-European look, short dark tousled hair, light stubble,
friendly relatable everyday face. Same warm daytime SIDE LIGHTING as the reference scene — soft
golden sunlight coming from the LEFT, gentle warm tone — so the cutout blends into the cafe terrace.

WHAT HE IS DOING: he sits relaxed at the table, enjoying a coffee break — he holds an OPEN NEWSPAPER
in both hands, reading it, calm and content; a small CUP OF COFFEE with a saucer sits on the table
in front of him.

THE TABLE SET (part of the cutout, IN FRONT of his legs): a small ROUND wooden BISTRO cafe table and
a BENTWOOD / rattan cafe CHAIR that MATCH the terrace furniture in the reference (cafe-3.png). The
table top is in front of him with the coffee cup on it; he sits on the chair behind the table so the
table naturally overlaps his lap/legs.

POSE & VIEW: seated upright, relaxed, three-quarter view matching an eye-level street camera looking
slightly down onto the terrace (same viewing angle as the reference). The whole group (chair legs,
table legs, his feet) rests on the ground plane, so it can be placed onto the paved terrace later.

FRAMING: the ENTIRE group in frame — the man from head down, plus the full table and chair down to
where their legs meet the floor. No cropping of head, hands, the cup or the furniture legs.

OUTPUT: high-resolution, transparent background (PNG, alpha), the seated man + table + chair only.

avoid: any background, floor texture, wall, other tables; a cast shadow pool on the ground (keep the
alpha clean — a soft contact shadow directly under the table/chair legs is OK, nothing more); other
people; text/letters on the newspaper (blank or blurred newsprint, no readable words), logos,
watermarks; changing his face or age or build (must stay the SAME person as the reference); business
suit (here he is in EVERYDAY CASUAL — light t-shirt / open casual shirt, jeans); headphones,
binoculars, hard hat; night or dark palette; flat cartoon; low detail; blurry hands or extra fingers.
```

## Заметки
- **Одежда:** повседневная (как у героя обычно — светлая футболка / открытая рубашка + джинсы),
  НЕ костюм (костюм — для сцены «в банк»).
- **Реквизит:** открытая газета в руках + чашка кофе на столе. Текст на газете НЕ пишем (плывёт) —
  пустой/размытый газетный набор.
- **Стол/стул — часть cutout** (перед ногами), стиль как на веранде `cafe-3.png`.
- **Свет — тёплый, слева** (как в сцене), иначе группа будет выбиваться.
- **Размещение:** поставить на **2-й столик слева**, перекрыв старый пустой стол. Подогнать масштаб/
  наклон под перспективу веранды. Мягкую контактную тень под ножками можно оставить — поможет «приземлить».
- Прозрачный фон, вся группа целиком (герой + стол + стул).
