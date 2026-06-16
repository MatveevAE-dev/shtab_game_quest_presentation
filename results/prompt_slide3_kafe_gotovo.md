# Промпт картинки — Слайд 3 «Кафе открыто» (edit / inpaint поверх слайда 2)

**Идея:** та же улица и тот же кадр, что на слайдах 1–2, но кафе **полностью готово и работает**:
ремонт окончен, на тротуаре перед входом — **летняя веранда на 3 небольших столика**, внутри
за стеклом видны **пара клиентов**. Вывеска «Ваш любимый КОФЕ» уже висит ровно.

## ⚙️ Как запускать (edit с маской — иначе перерисует весь кадр и уронит качество)
- Грузишь **картинку слайда 2** в ChatGPT/DALL-E edit (или Midjourney Vary Region / inpaint).
- **Выделяешь маской ТОЛЬКО зону кафе** (витрина + фасад над ней + кусок тротуара перед входом
  под веранду). Всё вне маски ИИ не трогает → композиция, свет, левые здания, ФСК, перспектива
  и качество сохраняются.
- Размер/разрешение остаются как у исходника (edit не меняет размер).
- ⚠️ Кириллица на вывеске может поплыть — надёжнее текст вывески наложить в HTML / фоторедакторе.

## Полный промпт (edit зоны кафе)
```
Edit ONLY the masked area (the central cafe storefront, its facade strip above it, and the
pavement right in front of its entrance). Keep the ENTIRE rest of the image 100% unchanged —
same composition, same street, same buildings on the left, same perspective, same daylight,
same colors, same resolution and sharpness. Do NOT re-render or restyle anything outside the mask.

Inside the masked cafe area, change the state from "renovation in progress" to "FINISHED, OPEN
AND IN BUSINESS": the renovation is COMPLETE — no more ladders, tools, paint buckets, cement bags
or construction mess. The facade is clean and finished, the signboard "Ваш любимый КОФЕ" is now
fully mounted and straight above the entrance in clean modern white Cyrillic letters. The PAVEMENT
and street in front are now CLEAN and tidy — no dust, no dirt, no debris, swept and well kept.

OUTDOOR TERRACE: on the pavement in front of the cafe add a small cosy SUMMER TERRACE with exactly
THREE small round cafe tables, each with a couple of chairs and a small cup of coffee on top, and a
low planter or rope divider around it — a welcoming open-air seating area. IMPORTANT: the terrace
must NOT block or cover the cafe ENTRANCE / doorway — leave the door clearly open and accessible,
place the tables to the SIDE of the entrance, not in front of it.
TERRACE FITTINGS: a fabric AWNING (маркиза) over the terrace, a free-standing A-frame chalkboard
sign / sandwich board (штендер) near the tables, a small standing MENU INFORMATION board, and a
tidy TRASH BIN by the edge of the terrace. Keep all of these clean and modern.

INTERIOR: through the clean storefront glass you can see the finished cafe interior with the bar
counter and shelving, warm interior lighting, a visible PAYMENT TERMINAL / card reader on the bar
counter, and a COUPLE OF CUSTOMERS seated inside, relaxed, as if the cafe is open and working.

Keep everything photoreal, bright and consistent with the existing warm daylight scene. If the hero
entrepreneur is still in frame, keep him IDENTICAL to the previous slides (same face, build, hair,
clothes) — do NOT redraw him. No other changes outside the mask.
```

## Текст — надёжнее в HTML (не в картинку)
- **Вывеска кафе:** «Ваш любимый КОФЕ» — если ИИ исказит кириллицу, оставить пустую табличку
  и наложить текст/логотип в HTML.
- Соседние вывески («Мой бизнес», «Московский гарантийный фонд») — вне маски, не трогаем.

## Заметки (слайд 3)
- **Состояние кафе: «готово / открыто»** — финал цепочки: «до» (сл.1) → «ремонт» (сл.2) →
  «работает» (сл.3). Важен контраст состояний одного помещения.
- **Летняя веранда: ровно 3 небольших столика** сбоку от входа (вход НЕ перекрывать), стулья,
  ограждение/кашпо. Фурнитура: маркиза, штендер (раскладная доска-меню), табличка-меню, мусорный бак.
- **Внутри — пара клиентов**, тёплый свет, барная стойка и шкафы из слайда 2, **терминал оплаты** на стойке.
- **Никакого ремонтного реквизита** (стремянка, краска, цемент убраны).
- **Улица после ремонта — чистая, ухоженная**, без грязи и пыли.
- Всё вне зоны кафе (левые дома, ФСК справа, небо, тротуар вдали) — **без изменений**.
