# Промпт картинки — Слайд 3 «Кафе открыто» (edit финального кадра слайда 2)

**База:** финальный кадр слайда 2 — **`presentation/assets/img/bg/cafe-2.png`** (кафе в ремонте).
Слайд 3 = **та же картинка**, меняем **ТОЛЬКО кафе**: из «ремонт» → **«готово, открыто, работает»**.
Всё остальное (ЦУБ, банк, площадь, перспектива, деревья, Moscow-City, свет) — **1-в-1**.
**Предпринимателя в кадре НЕТ** (генерим отдельно, накладываем в HTML).

## Что есть на базовом кадре (cafe-2.png) — НЕ менять
- Слева: обрезок дома → офис **«ЦУБ»** (вывеска, ресепшен, сотрудник + клиент) → **кафе** с уже
  висящей вывеской **«ВАШ ЛЮБИМЫЙ КОФЕ»**, внутри — отделка (барная стойка, шкафы), стремянки,
  **рабочий в каске**, ведро.
- Правее: мощёная площадь, **светлый колонный банк**, главная аллея с деревьями, **Moscow-City справа**.
- Солнечный летний день.

## ⚙️ Как запускать
- **Лучший путь — EDIT `cafe-2.png`:** приложить и попросить изменить **только зону кафе** (витрина
  + фасад над ней + кусок тротуара перед входом под веранду), остальное — без изменений.
- **Если тул без масок (точечные комментарии):** точка на кафе + текст ниже.
- **Размер:** 7680 × 2592 px (≈ 2,96:1) — как слайды 1–2. Edit размер не меняет.
- ⚠️ Вывеска «ВАШ ЛЮБИМЫЙ КОФЕ» уже есть — **сохранить как есть**, не переписывать (кириллица плывёт).

## Промпт EDIT (менять только кафе)
```
Edit ONLY the cafe unit (its storefront glass, the facade strip above it, and the pavement right in
front of its entrance). Keep the ENTIRE rest of the image 100% unchanged — same ЦУБ office, same
neoclassical columned bank, same paved plaza, same trees, same street, same vanishing perspective,
same Moscow-City on the right, same daylight, same colors, same resolution and sharpness, and keep
the existing "ВАШ ЛЮБИМЫЙ КОФЕ" signboard exactly as it is. Do NOT re-render or restyle anything
outside the cafe.

Change the cafe from "renovation in progress" to "FINISHED, OPEN AND IN BUSINESS": the renovation is
COMPLETE — REMOVE all ladders, tools, paint buckets, cement bags, construction mess AND the
construction worker inside. The facade and storefront are clean and finished. The PAVEMENT in front
is now CLEAN and tidy — no dust, no dirt, no debris.

INTERIOR: through the clean storefront glass you can see the finished cafe interior — the bar
counter and shelving, warm interior lighting, a visible PAYMENT TERMINAL / card reader on the bar
counter, a barista behind the counter and A COUPLE OF CUSTOMERS seated inside, relaxed, as if the
cafe is open and working.

OUTDOOR TERRACE: on the pavement in front of the cafe add a small cosy SUMMER TERRACE with exactly
THREE small round cafe tables, each with a couple of chairs and a small cup of coffee on top, and a
low planter or rope divider around it. IMPORTANT: the terrace must NOT block or cover the cafe
ENTRANCE / doorway — leave the door clearly open and accessible, place the tables to the SIDE of the
entrance, not in front of it. TERRACE FITTINGS: a fabric AWNING over the terrace, a free-standing
A-frame chalkboard sign (sandwich board) near the tables, a small standing MENU board, and a tidy
TRASH BIN by the edge. Keep all of these clean and modern.

NO entrepreneur / NO hero / NO main character anywhere in the frame — the only people are the
barista and the seated customers inside, and optionally a guest or two at the terrace tables. Keep
everything photoreal, bright and consistent with the existing warm daylight scene. No other changes.
```

## Если тул только точечные комментарии (без масок)
Точку — на витрину кафе, текст:
> Кафе достроено и работает: убери все стремянки, инструменты, ведро и рабочего в каске. Внутри —
> готовый интерьер, бариста за стойкой, терминал оплаты на стойке, пара клиентов за столиками.
> Перед входом сбоку (не перекрывая дверь) — летняя веранда на 3 столика со стульями, маркиза,
> штендер-меню, урна. Тротуар чистый. Вывеску «ВАШ ЛЮБИМЫЙ КОФЕ» не трогай. Остальное на картинке
> не меняй. Предпринимателя в кадр не добавляй.

## Заметки (слайд 3)
- Отличие от слайда 2 — **только кафе** (готово вместо ремонта). Улица/банк/ЦУБ/площадь/перспектива/
  Moscow-City — идентичны `cafe-2.png`.
- **Убрать:** стремянки, инструменты, ведро, рабочего в каске, ремонтный мусор.
- **Внутри:** бариста + пара клиентов, тёплый свет, барная стойка, **терминал оплаты** на стойке.
- **Летняя веранда: ровно 3 столика** сбоку от входа (вход НЕ перекрывать) + маркиза, штендер,
  табличка-меню, урна.
- **Вывеска «ВАШ ЛЮБИМЫЙ КОФЕ»** уже висит — сохранить как есть.
- **Предпринимателя в кадре нет** — накладываем отдельно в HTML.
- Улица после ремонта — чистая, ухоженная.
