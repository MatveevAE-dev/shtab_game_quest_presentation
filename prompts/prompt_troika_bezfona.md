# Промпт — тройка «Кавказская пленница» без фона (PNG прозрачный)

Цель: вырезать **трёх персонажей** (Трус, Балбес, Бывалый — стоят в ряд, держатся за руки,
перегородили дорогу) с исходного кадра и получить **PNG с прозрачным фоном**, как у эскаватора.

## Что прикрепить

1. **image 1 = исходный кадр** — `Downloads/авав.jpg` (три героя на дороге).

## Важно про прозрачность

ChatGPT часто рисует фон заново (серый/шахматка), а не делает настоящую альфу. Поэтому:
- В промпте явно требуем **PNG с настоящим альфа-каналом, фон 100% прозрачный**.
- Если результат пришёл с фоном/шахматкой нарисованной — прогнать файл через **remove.bg**
  (надёжная реальная прозрачность), потом использовать.

---

## Промпт (вставлять в ChatGPT / gpt-image)

```
Take the three men from the attached photo (the comedic trio standing across the road, holding
hands in a chain, in dynamic blocking poses). CUT THEM OUT and return ONLY these three figures
on a FULLY TRANSPARENT background.

REQUIREMENTS:
- Keep all THREE characters exactly as in the photo: same faces, same poses, same clothes,
  same hand-holding chain — do NOT redraw, restyle, slim, or change them. Photoreal, identical.
- Show them FULL BODY, head to feet, nothing cropped. Keep them together as ONE group in their
  current relative positions and spacing.
- REMOVE the entire background completely: the road, asphalt, hills, trees, sky, shadows on the
  ground — all gone. The areas BETWEEN the figures, under their joined arms and between their
  legs must be TRANSPARENT too (real holes, not filled).
- Output a PNG with a REAL ALPHA CHANNEL, background 100% transparent (alpha = 0). Do NOT paint
  a gray, white, or checkerboard background. No ground plane, no drop shadow, no platform.
- Clean anti-aliased edges around hair, fingers and clothing.

NO text, NO captions, NO watermark, NO frame.
```

---

## Чек-лист

- [ ] Все 3 героя целиком, позы/лица/одежда как в оригинале.
- [ ] Фон полностью прозрачный (дорога, холмы, небо, тени убраны).
- [ ] Дырки между фигурами и под руками — прозрачные, не залиты.
- [ ] Это PNG с настоящей альфой (не нарисованная шахматка/серый фон).
- [ ] Если альфа плохая → прогнать через remove.bg.
- [ ] Края чистые, без ореола.
```
