# Промпт: аватар-помощник «Байков С.Н.» — стиль презентации «На одной волне»

## Как использовать
- **Режим:** image-to-image / «по референсу лица». Вход — реальное фото
  `presentation/assets/img/objects/Байков С.Н..jpg` (блондин, тёмный костюм, синий галстук).
- Промпт задаёт **только стиль**; лицо берём с фото (сходство обязательно).
- Настройки: сходство/likeness — **высокое** (denoise ~0.35–0.5 для SD; в Midjourney — `--cref <фото> --cw 100`; в GPT-image/Sora — «сохрани черты лица с фото, стилизуй только рендер»).
- **Без рамки, без гекса, без свечения** — их добавим кодом. Нужен чистый бюст на **прозрачном фоне**.

---

## Промпт (RU)

Стилизованный игровой аватар-портрет реального мужчины с фото-референса. **Точно сохранить
черты лица и сходство**: светлые (русо-блонд) волосы, гладко зачёсанные назад, гладко выбритое
лицо (без бороды), прямые брови, спокойные внимательные глаза, серьёзное, собранное деловое
выражение. Кадр — **бюст до плеч, анфас, по центру**.

Одежда: тёмно-серый/тёмно-синий деловой костюм, белая рубашка, синий галстук — стилизованно,
чистыми плоскостями. Стиль рисовки: **полу-мультяшный digital-арт / cel-shaded игровой
портрет**, плавные формы, мягкие плоские тени, чистые края, лёгкая «помультяшенность», но лицо
остаётся узнаваемым. Настроение — футуристический бизнес-квест «неоновая Москва».

Свет и цвет: **холодный цвето-грейд под деку** — тёмно-сине-бирюзовые тени, прохладная среда,
тёплый мягкий ключевой свет на лице для естественной кожи. **Без неон-свечения/rim-light по
контуру фигуры** (обводку и неон добавим отдельно кодом) — край силуэта чистый, ровный.
Аккуратная, читаемая графика.

Фон: **полностью прозрачный (PNG, alpha)**, фигура изолирована, чёткий силуэт по контуру.

## Prompt (EN, для Midjourney/SD)

Stylized game-avatar portrait of a real man from reference photo, **keep exact facial likeness**:
light blond hair combed straight back, clean-shaven face (no beard), straight eyebrows, calm
attentive eyes, serious composed business expression. Framing: **bust, head-and-shoulders, front
view, centered**. Wearing dark grey/navy business suit, white shirt, blue tie, stylized in clean
flat shapes. Art style: **semi-cartoon digital art / cel-shaded game portrait**, smooth forms,
soft flat shading, crisp clean edges, lightly toon-shaded yet recognizable. Mood: futuristic
business quest, neon Moscow. Lighting: **cool color grade** — dark teal-navy shadows, cool
ambient, warm soft key on the face for natural skin. **No neon glow / no rim-light on the figure
edge** (outline and neon are added separately in code) — keep the silhouette edge clean and even.
Background: **fully transparent (PNG alpha)**, isolated figure, clean silhouette edge. High
resolution.

## Негатив (что НЕ нужно)
- Другой человек / искажённое лицо / изменённая личность.
- Борода/щетина (он гладко выбрит). Взъерошенные волосы (у него гладко зачёсаны назад).
- Рамка, гексагон, круг, подпись, текст, логотип — **не добавлять** (сделаем в коде).
- Запечённое свечение/ореол/неон-rim-light по краю фигуры — **не добавлять** (контур/пульс — в коде).
- Фон (город, студия, цвет) — только прозрачный.
- Пере-реалистичные поры/фотореализм; засвет; размытие краёв.

## Выход
- Соотношение: квадрат 1:1 (или 3:4), высокое разрешение.
- Формат: **PNG с прозрачностью**, чистый край силуэта (важно для авто-контура).
- Имя файла: `presentation/assets/img/objects/avatar-baykov.png`.

---

## Дальше (делаем кодом, как у героя)
1. Тугой кроп по alpha → генерим неон-контур PNG (дилатация наружу, цвет `--neon`).
2. Гексагон-рамка (CSS, в стиле октаэдров карты) + портрет внутри (маска-clip).
3. Появление: **прилёт с искрами** → **скан-прорисовка контура сверху вниз** (как `heroDraw`)
   → лицо проступает из расфокуса (deblur+fade).
4. Idle: **бумеранг** — лёгкий ping-pong (дыхание/качание, `animation-direction:alternate`)
   + пульс контура (`heroGlow`).
