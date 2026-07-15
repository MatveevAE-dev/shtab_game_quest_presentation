# Промпт — «Пожилая пара заходит в кафе» (спрайт на зелёном фоне, под вырезку)

Спрайт-объект для кафе-сцены: **та же пожилая пара** (что на `cafe - interior.png` и в
`prompt_fon_kafe_para_braille.md`) идёт ко входу в кафе. По аналогии со слайдом 14, где женщина
с коляской подходит к кафе (`woman-stroller.png`) и движется по точкам. Пара нужна **без фона** —
генерим на **ярко-зелёном хромакее**, потом фон удаляем → прозрачный PNG в `objects/`.

- **Стиль:** та же пара, что на референсе кафе (седой мужчина в тёмных очках — слабовидящий;
  седая женщина). Фотореализм, тёплый дневной свет — чтобы спрайт лёг в кафе-сцену.
- **Поза:** **идут вместе**, в движении (шаг), **ВИД СО СПИНЫ** (3/4 сзади) — уходят ОТ камеры
  вглубь, влево, как `woman-stroller.png` (её видно со спины, лиц не видно). **Во весь рост,
  голова-до-ног**, ничего не обрезано.
- **Инклюзия:** мужчина с **белой тростью** + жена ведёт его **под руку** (слабовидящий —
  мотив тот же, что Брайль-меню внутри). Тепло, с заботой.
- **Фон:** ЧИСТЫЙ ярко-зелёный хромакей `#00FF00`, равномерный, **без теней** и без зелёных
  отсветов на одежде/коже — для чистой вырезки.
- **Размер:** портрет/квадрат, вся фигура с полями (НЕ сверхширокий — это объект, не фон).

## Что прикрепить к генератору

1. `cafe - interior.png` — эталон внешности пары (седина, одежда мужчины/женщины).
2. `woman-stroller.png` — эталон РАКУРСА И НАПРАВЛЕНИЯ: со спины, уходит от камеры влево.
   Ссылаемся: «SAME couple as image 1, SAME back-view walking angle/direction as image 2».

---

## Готовый промпт (вставлять в генератор)

```
Full-body photorealistic cutout of an ELDERLY COUPLE walking together, shot on a solid BRIGHT
CHROMA-KEY GREEN screen (#00FF00), studio product-shot style for easy background removal.
Portrait / near-square frame, the WHOLE pair visible HEAD TO FEET with clear margin on all
sides — nothing cropped by the edges.

They are the SAME elderly couple as in attached image 1 (the cafe): keep hair and clothing
consistent. The camera angle and walking direction must MATCH attached image 2
(`woman-stroller.png`) — seen FROM BEHIND, walking AWAY from the camera.
  ELDERLY MAN: silver-grey hair, warm knit cardigan/sweater in soft neutral tones, comfortable
  trousers and shoes. He walks holding a WHITE CANE (long guide cane for the blind) in his
  outer hand, sweeping slightly ahead.
  ELDERLY WOMAN: silver/white hair, warm blouse or light cardigan and trousers. She walks
  ARM-IN-ARM beside him, gently GUIDING him — one hand on his arm.

POSE — CRITICAL: they are seen FROM BEHIND (back / three-quarter-back view), WALKING AWAY from
the camera INTO the scene, moving toward the LEFT — EXACTLY like the woman in image 2 (we see her
BACK, her face hidden, she walks away to the left). We see the couple's BACKS and the backs of
their heads; their faces are NOT visible (at most a tiny sliver of profile). Mid-stride, natural
walk-cycle silhouette, tender and unhurried. This is NOT a front view and they do NOT face the
camera.

LIGHTING: soft, even, natural DAYLIGHT matching a warm cafe interior — gentle key from the front,
no harsh shadows, no colored rim. Lighting must be neutral/warm enough to composite seamlessly
into a warm daytime cafe scene later.

BACKGROUND: a perfectly FLAT, EVEN, saturated CHROMA GREEN (#00FF00) filling the entire frame.
NO floor, NO cast shadow on the ground, NO gradient, NO props, NO scenery — ONLY the two people
on pure green. Keep green AWAY from their skin, hair and clothes (no green spill / no green
reflections), and avoid green or lime tones in their outfits so the key is clean.

RENDER: high-detail photoreal, sharp focus on the whole couple (no depth-of-field blur — they
must be crisp edge-to-edge for cutout), realistic skin, hair and fabric, 8K.

CLEAN PLATE: NO text, NO captions, NO logos, NO UI, NO watermark, NO extra people, NO furniture,
NO cafe in the background — just the elderly couple on flat green.

AVOID: a FRONT view / facing the camera / visible faces (they MUST be seen from BEHIND, walking
away — like image 2); cropping the feet or head; a seated pose (they must be WALKING, standing);
green spill on skin/clothes; cast shadows or a floor; motion blur; more than one white cane;
extra or malformed hands/fingers; changing the couple's identity from image 1; a wide cinematic
background (this is an isolated object, not a scene).
```

---

## После генерации — удалить зелёный фон (хромакей → прозрачный PNG)

Тот же приём, что для `woman-stroller.png` / `hero-ramp.png`:

1. Ключ по «зелёности» `greenness = g − max(r, b)`; мягкая матовая маска (LO→HI), чтобы края не
   рвались.
2. **Деспилл** — убрать зелёный ореол по контуру (зажать `g ≤ max(r, b)` в полупрозрачных пикселях).
3. Тугая обрезка по альфа-боксу (bbox непрозрачных пикселей) + небольшое поле.
4. Сохранить `assets/img/objects/para-cafe.png` (RGBA). Проверить: остаточный фон = 0, ноги/голова
   не срезаны.

> После вырезки — вставляем как объект в кафе-сцену и двигаем по точкам (механика женщины с
> коляской на слайде 14: `NC_WOMAN_ANCHORS` / WAAPI-ходьба).

## Чек-лист перед приёмкой картинки

- [ ] Та же пара, что на референсе кафе (седой мужчина + седая женщина).
- [ ] Идут ВМЕСТЕ, в шаге, **ВИД СО СПИНЫ**, уходят ОТ камеры влево — как `woman-stroller.png` (лиц НЕ видно, НЕ анфас).
- [ ] Во весь рост, голова-до-ног, НИЧЕГО не обрезано, есть поля.
- [ ] Мужчина с БЕЛОЙ ТРОСТЬЮ; жена ведёт под руку (одна трость, руки без лишних пальцев).
- [ ] Фон — чистый ярко-зелёный `#00FF00`, равномерный, БЕЗ теней и БЕЗ пола.
- [ ] Нет зелёных отсветов на коже/одежде; в одежде нет зелёного/лаймового.
- [ ] Резко по всей фигуре (без размытия ГРИП) — под чистую вырезку.
- [ ] Никаких надписей/UI/мебели/кафе на фоне — только пара на зелёном.
- [ ] После вырезки: остаточный фон = 0, тугой альфа-бокс, PNG RGBA в `objects/`.
