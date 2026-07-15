# Промпт фоновой картинки — «Кафе: пожилая пара с меню Брайля» (крупный план)

Второй фон для кафе-сцены «Больше чем бизнес». Тот же интерьер и та же пара, что на
`presentation/assets/img/bg/cafe - interior.png`, но **камера ближе**: крупный план пожилой
пары за столиком у окна. Пожилой мужчина держит **меню со шрифтом Брайля** — тактильные точки
чётко видны, читает пальцами. К ним подошёл **официант с бионическим протезом** и принимает
заказ. Это «инклюзивная» сцена: доступная среда + сотрудник с протезом.

- **Стиль:** 1-в-1 как у прикреплённого `cafe - interior.png` — тёплый кинематографичный
  фотореализм, золотой час, дерево + кирпич + большие окна, подвесные лампы. Референс =
  эталон по палитре/материалам/свету и по внешности пары и официанта.
- **Размер:** **~2,95:1** (как референс — 2155×730; можно 2560×868). Сверхширокий, НЕ 16:9 —
  ложится в ту же сцену `.co-stage` (viewBox 2172×724).
- **Кадр:** ближе и левее, чем на референсе — пожилая пара крупно (поясной план), стол в кадре.
  Семья с детьми и стойка уходят в мягкое боке на фоне.
- **Ключевые детали:** (1) меню с Брайлем — крупно, точки-пупырышки читаются, палец на строке;
  (2) официант с ОДНИМ протезом — **только правая рука** бионическая, левая — обычная живая;
  протез чётко виден, официант держит блокнот/планшет, принимает заказ.
- **Clean plate:** ни надписей, ни UI, ни логотипов. Брайль (рельефные точки) — МОЖНО и НУЖНО,
  но без читаемых печатных слов на меню/вывесках.

## Что прикрепить к генератору

1. `cafe - interior.png` — эталон сцены (интерьер, свет, пара, официант, протез).
   Ссылаемся: «reproduce the SAME elderly couple and the SAME waiter as in the attached image,
   just closer». **Важно:** на референсе у официанта ошибочно ДВА протеза — в промпте явно
   правим: протез ОДИН, на правой руке; левая рука обычная.

---

## Готовый промпт (вставлять в генератор)

```
Cinematic photorealistic interior of a warm, cozy European-style cafe, ultra-wide cinematic
frame, aspect ratio 2.95:1 (about 2560×868), 8K, shallow depth of field. Golden-hour daylight
pours through tall windows on the LEFT; soft warm bokeh, film-like color grade. The MOOD,
lighting, materials and characters must MATCH the ATTACHED REFERENCE IMAGE of this cafe — same
warm palette (cream, honey wood, terracotta brick, soft gold light), same big arched windows
with a blurred classical Moscow building outside, same wooden counter, pendant glass lamps,
plants and espresso machine softly out of focus in the BACKGROUND.

This is a CLOSER, TIGHTER shot of the SAME scene: the camera has moved IN and slightly LEFT to
frame the ELDERLY COUPLE at their table by the window as the MAIN SUBJECT (medium shot, roughly
waist-up, their round wooden table visible in the foreground). The family with children, the
waiter serving coffee elsewhere, the counter and the rest of the room are pushed into a soft,
creamy BOKEH background — present but blurred, so all sharp focus is on the elderly couple and
the waiter taking their order.

ELDERLY MAN (left of the pair, foreground): silver-grey hair, wearing DARK glasses (visually
impaired), a warm knit cardigan/sweater in soft neutral tones — SAME man as in the reference.
He holds an OPEN MENU with both hands, tilted toward the camera so the page is clearly readable.
The menu page is covered with rows of raised BRAILLE DOTS — tactile embossed bumps casting tiny
soft shadows — and ONE of his fingertips rests ON a line of Braille, reading by touch. The
Braille must be the CLEAR FOCAL DETAIL: crisp, well-lit, unmistakably tactile dots (NOT printed
letters, NOT random texture). He has a calm, content expression, slightly turned toward the
waiter.

ELDERLY WOMAN (beside him): silver/white hair, warm blouse or cardigan, gentle warm smile,
looking up toward the waiter — SAME woman as in the reference. A coffee cup and saucer on the
table near her.

WAITER (right side of the frame, leaning in attentively to TAKE THEIR ORDER): a friendly young
man with short dark hair, white shirt and a dark denim apron — SAME waiter as in the reference.
He has EXACTLY ONE bionic prosthetic: his RIGHT arm — a single SLEEK BIONIC PROSTHETIC FOREARM
AND HAND (matte black and brushed steel-blue plating, subtle segmented joints, faint cool-blue
accent glow), same design language as the reference. His OTHER arm (the LEFT) is a completely
NORMAL human arm and hand — plain skin, no plating. (The attached reference mistakenly shows two
prosthetic arms; here there must be ONLY ONE, on the RIGHT.) He holds a small notepad / order pad
in one hand and writes with a SINGLE PEN in the other, taking the order; his single BIONIC RIGHT
HAND is clearly visible and in focus — an elegant, high-tech but natural part of him, not
menacing. Count carefully: ONE prosthetic hand + ONE normal human hand (two hands total), and
exactly ONE pen, held in one hand only.

COMPOSITION: the elderly couple occupy the LEFT and CENTER of the wide frame at the table; the waiter
stands/leans on the RIGHT, slightly bent toward them; the bright window and its warm rim-light
are behind the couple on the left. Keep the round wooden table with a small plant and cups in
the lower foreground. Leave the far RIGHT and the deep background soft and blurred (counter,
lamps, other guests as warm bokeh).

LIGHTING & RENDER: warm cinematic golden-hour light, soft window rim-light on the couple's hair
and the menu, gentle warm bounce fill, cozy inviting atmosphere, rich but soft contrast,
photographic skin, natural fabric detail, shallow depth of field with creamy bokeh, subtle lens
haze and glow. High-end photoreal cinematic still, 8K, AAA quality. The cool steel-blue of the
bionic hand is the only cool accent in an otherwise warm golden scene.

CLEAN PLATE: NO text, NO captions, NO letters, NO printed words, NO numbers, NO logos, NO signs,
NO menu prices, NO UI/HUD, NO watermark. The ONLY exception is the raised BRAILLE DOTS on the
menu (tactile bumps, not readable print) — those are required. Nothing else in the image should
contain readable writing.

AVOID: TWO prosthetic arms (only the RIGHT arm is bionic, the left is a normal human arm); TWO
pens or more than one pen (exactly ONE pen); extra or malformed hands/fingers; printed/typed text
on the menu instead of Braille; Braille that looks like random dotted texture or polka dots; a
horror/menacing robotic arm; the couple looking small or lost; a flat evenly-lit look; changing
the identity of the couple or the waiter from the reference; a narrow 16:9 crop. Keep it warm,
tender, inclusive and cinematic.
```

---

## Чек-лист перед приёмкой картинки

- [ ] Формат ~2,95:1 (сверхширокий), НЕ 16:9 — сядет в `.co-stage`.
- [ ] Пожилая пара — крупно, главный объект (поясной план), стол в переднем плане.
- [ ] Меню с БРАЙЛЕМ читается: рельефные точки с мягкими тенями, палец на строке — НЕ печатный текст.
- [ ] Мужчина в тёмных очках, седой, тёплый кардиган — та же личность, что на референсе.
- [ ] Женщина седая, тёплая улыбка, чашка на столе — та же личность.
- [ ] У официанта РОВНО ОДИН протез — на ПРАВОЙ руке (матовый чёрный + сталь-синий); левая рука обычная живая. НЕ два протеза.
- [ ] Держит РОВНО ОДНУ ручку (не две) + блокнот; принимает заказ. Руки без лишних пальцев.
- [ ] Интерьер/свет/палитра 1-в-1 с референсом: окна, кирпич, дерево, лампы, золотой час.
- [ ] Фон (семья, стойка, гости) — в мягком боке, резкость на паре и официанте.
- [ ] Единственный холодный акцент — сталь-синий протеза; вся сцена тёплая.
- [ ] Clean plate: нет надписей/UI/логотипов/цен; ЕДИНСТВЕННОЕ исключение — точки Брайля.
- [ ] Протез — элегантный, не пугающий; сцена тёплая, инклюзивная.
