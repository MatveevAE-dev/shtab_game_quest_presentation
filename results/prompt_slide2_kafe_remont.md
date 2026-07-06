# Промпт картинки — Слайд 2 «Ремонт кафе» (edit финального кадра слайда 1)

**База:** финальный кадр слайда 1 — **`presentation/assets/img/bg/cafe-1.png`** («кафе ДО»).
Слайд 2 = **та же картинка**, меняем **ТОЛЬКО кафе**: из пустого/заброшенного → **в РЕМОНТЕ**.
Всё остальное (ЦУБ, банк, площадь, перспектива, деревья, Moscow-City, свет) — **1-в-1**.

## Что есть на базовом кадре (cafe-1.png) — НЕ менять
- Слева: обрезок дома у края → офис **«ЦУБ»** (тёмная вывеска «ЦУБ / Центр услуг для бизнеса»,
  за стеклом — ресепшен, сотрудник + клиент) → **кафе** (большая тёмная грязная витрина, пусто внутри).
- Передний план: широкая **плитка-площадь**.
- Правее: открытая мощёная площадь, на углу — **светлый неоклассический банк** (колонны, портик,
  фронтон, зелёная крыша), в глубину уходит **главная аллея** с рядом деревьев.
- Справа на горизонте — **Moscow-City**. Солнечный летний день, тёплый свет.

## ⚙️ Как запускать
- **Лучший путь — EDIT `cafe-1.png`:** приложить картинку и попросить изменить **только зону кафе**
  (витрина + фасад над ней + кусок тротуара перед входом), сохранив весь остальной кадр без
  изменений. Так сцена гарантированно совпадёт со слайдом 1.
- **Если тул без масок (точечные комментарии):** поставить точку на кафе и дать текст ниже.
- **Размер:** 7680 × 2592 px (≈ 2,96:1) — как слайд 1. Edit размер не меняет.
- ⚠️ Кириллица: вывеску ЦУБ **не трогаем** (она уже есть). У кафе вывески НЕТ.

## Промпт EDIT (менять только кафе)
```
Edit ONLY the cafe unit (its storefront glass, the facade strip above it, and the pavement right in
front of its entrance). Keep the ENTIRE rest of the image 100% unchanged — same ЦУБ office, same
neoclassical columned bank, same paved plaza, same trees, same street, same vanishing perspective,
same Moscow-City on the right, same daylight, same colors, same resolution and sharpness. Do NOT
re-render or restyle anything outside the cafe.

Change the cafe from its empty / derelict "before" state to "RENOVATION IN PROGRESS": the FACADE
around the storefront becomes FRESH and renewed — clean new cladding, repaired plaster, fresh paint,
new window frames (no more grime, dust or peeling). The big storefront GLASS is now clean; through
it the INTERIOR is being fitted out — a new BAR COUNTER, wooden CABINETS / shelving along the wall,
tools, a step-stool, work lights — clearly a place mid-renovation turning into a cafe. A step LADDER
leans by the entrance; on the pavement in front, a bucket of paint and TWO bags of cement.
Optionally ONE worker in a work jacket and hard hat doing repair work. The cafe still has NO
signboard (no text, no logo above the entrance). Keep everything photoreal, subtly lit by the same
warm daylight, consistent with the rest of the scene. No other changes.
```

## Если тул только точечные комментарии (без масок)
Точку — на витрину кафе, текст:
> Преврати это кафе из пустого/заброшенного в состояние ремонта: свежий фасад, чистое стекло,
> внутри идёт отделка — барная стойка, деревянные шкафы, инструменты, рабочий свет; у входа
> стремянка, на тротуаре ведро краски и 2 мешка цемента. Вывески у кафе нет. Всё остальное на
> картинке не меняй.

## Заметки (слайд 2)
- Отличие от слайда 1 — **только кафе** (ремонт вместо пустоты). Улица/банк/ЦУБ/площадь/перспектива/
  Moscow-City — идентичны `cafe-1.png`.
- **У кафе вывески нет** (только ремонт). ЦУБ — уже с вывеской, не трогаем.
- **Героя в кадре нет** — накладываем в HTML. Можно 1 рабочего у стремянки.
- Реквизит ремонта: стремянка, ведро краски, 2 мешка цемента, барная стойка и шкафы за стеклом.
