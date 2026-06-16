# Промпт картинки — Слайд 2 «Ремонт кафе» (edit / inpaint поверх слайда 1)

**Идея:** та же улица и тот же кадр, что на слайде 1, но кафе **в процессе ремонта**:
внутри идут работы, появилась барная стойка и шкафы, фасад кафе стал **свежим** (новые
материалы), вешается вывеска **«Ваш любимый КОФЕ»**. Герой с планом в руках общается
с бригадиром. У входа — стремянка для монтажа вывески, рядом на тротуаре ведро краски
и 2 мешка с цементом.

## ⚙️ Как запускать (edit с маской — иначе перерисует весь кадр и уронит качество)
- Грузишь **картинку слайда 1** в ChatGPT/DALL-E edit (или Midjourney Vary Region / inpaint).
- **Выделяешь маской ТОЛЬКО зону кафе** (центральная витрина + фасад над ней + кусок тротуара
  перед входом). Всё вне маски ИИ не трогает → композиция, свет, левые здания, перспектива
  и качество сохраняются.
- Размер/разрешение остаются как у исходника (edit не меняет размер).
- ⚠️ Кириллица на вывеске «Ваш любимый КОФЕ» у ИИ может поплыть. Самый надёжный путь —
  оставить место под вывеску, а **текст наложить в HTML / фоторедакторе**.

## Полный промпт (edit зоны кафе)
```
Edit ONLY the masked area (the central cafe storefront, its facade strip above it, and the
pavement right in front of its entrance). Keep the ENTIRE rest of the image 100% unchanged —
same composition, same street, same buildings on the left, same perspective, same daylight,
same colors, same resolution and sharpness. Do NOT re-render or restyle anything outside the mask.

Inside the masked cafe area, change the state from "empty / before works" to "RENOVATION IN
PROGRESS, almost a cafe": the FACADE around the storefront is now FRESH and renewed — clean new
cladding, repaired plaster, fresh paint, new window frames (no more dust, peeling or grime). The
big storefront glass is clean; through it you can see the INTERIOR being fitted out: a new BAR
COUNTER, wooden CABINETS / shelving along the wall, some tools, a step-stool, work lights — clearly
a place mid-renovation turning into a cafe.

PEOPLE — exactly TWO: (1) the SAME hero entrepreneur — KEEP HIM IDENTICAL to the previous slide:
same FACE and facial features, same hairstyle and hair colour, same body build / physique, same
height, same skin tone, same age, same casual clothes (light shirt over white t-shirt, blue jeans,
white sneakers). Do NOT redraw, restyle, slim down, age or change his appearance in any way — it
must read as the exact same person. He stands on the pavement holding a rolled-out PLAN / blueprint
in his hands. (2) a FOREMAN / construction supervisor in a work jacket and hard hat standing next
to him, the two talking and pointing at the work. Keep both photoreal and naturally lit by the same
warm daylight.

DETAILS: a step LADDER leaning by the storefront where a new SIGNBOARD is being mounted above the
entrance — the sign reads "Ваш любимый КОФЕ" in clean modern white Cyrillic letters. On the
pavement nearby place a bucket of paint and TWO bags of cement. Keep everything photoreal, subtle
and consistent with the existing scene. No other changes outside the mask.
```

## Текст — надёжнее в HTML (не в картинку)
- **Вывеска кафе:** «Ваш любимый КОФЕ» — если ИИ исказит кириллицу, оставить пустую табличку
  и наложить текст/логотип в HTML.
- Вывески соседей («Мой бизнес», «Московский гарантийный фонд») — НЕ трогаем (вне маски).

## Заметки (слайд 2)
- **Состояние кафе: «ремонт»** — переход между слайдом 1 («до») и будущим слайдом («готовое кафе»).
  Важен контраст состояний одного и того же помещения.
- **2 человека:** герой (с планом) + бригадир (каска/спецовка). Лицо/одежда героя — как везде.
- **Реквизит ремонта:** стремянка у вывески, ведро краски, 2 мешка цемента, барная стойка и
  шкафы за стеклом.
- Всё вне зоны кафе (левые дома, ФСК справа, небо, тротуар вдали) — **без изменений**.
