# База промпта для редактирования картинки по маске (inpaint / замена объектов)

Задача: на **готовом** изображении «дневная Москва» менять отдельные объекты (нарисовать на
месте выделенной маски другое здание), **не трогая остальную картинку** и **без потери
качества и размера**.

---

## Как это работает (коротко)

- Это **инпейнтинг** (inpainting / «дорисовка по маске»): генератор перерисовывает **только
  область под маской**, остальные пиксели остаются нетронутыми. Поэтому композиция, соседние
  здания, свет и размер кадра не меняются.
- Маска = белая область там, где меняем; чёрная — где не трогаем (в большинстве инструментов
  кистью закрашиваешь объект, который надо заменить).

## Как сохранить качество и размер (главное)

Веб-генераторы часто **ужимают** всю картинку при экспорте — отсюда потеря качества и размера.
Чтобы этого не было:

1. **Photoshop → «Генеративная заливка» (Generative Fill)** — лучший вариант для «без потерь».
   Выделяешь объект → Generative Fill → промпт. Нейросеть рисует **новый слой только в
   выделении**, остальные пиксели файла **остаются 1-в-1**, размер кадра не меняется.
2. **Stable Diffusion (A1111 / ComfyUI) или Flux Fill** — режим Inpaint:
   - `Inpaint area = Only masked` (рисует только маску в полном разрешении),
   - `Mask padding ≈ 32–64 px` (чтобы шов слился),
   - выходной размер = **исходный W×H** (не уменьшать),
   - `Denoising 0.7–0.9` (сильная замена объекта).
3. **Если инструмент не тянет 7680×2592** (а большинство веб-сервисов — нет): **вырежи кусок**
   вокруг объекта с запасом (напр. 1024×1024 или 1536×1536), отредактируй его в полном
   разрешении, **вклей обратно** на то же место. Размер общего кадра не меняется.
4. Не пересохраняй всю панораму через сервисы, которые отдают меньшее разрешение —
   только локально (Photoshop) или по кропу.

---

## База промпта (вставлять в инпейнт; {ОБЪЕКТ} — что нарисовать)

```
Replace ONLY the building inside the masked area with: {ОБЪЕКТ}.
Match the EXISTING image exactly: same SUMMER daytime Moscow golden-hour lighting, same HIGH
bird's-eye top-down perspective and camera angle, same scale and proportions as the
neighbouring buildings, same warm color palette and shadow direction. Seamless photorealistic
blend with the surroundings, consistent ground level and street layout.
Keep everything OUTSIDE the mask unchanged. NO text, NO captions, NO sign boards, NO logos,
NO UI, NO watermark. High detail, sharp, same resolution and quality as the original.
```

**Негатив-промпт (если есть поле):**
```
text, letters, sign board, logo, watermark, blur, low quality, low resolution, distortion,
warped perspective, wrong scale, mismatched lighting, seam, halo around edges
```

---

## Шаблоны под наши объекты ({ОБЪЕКТ})

- **Кофе на вынос:** `a tiny street coffee-to-go kiosk / small takeaway coffee stand`
- **Кафе:** `a small cafe in the ground floor of a building, with a summer terrace`
- **Ресторан:** `a mid-size standalone restaurant with a nice entrance and terrace`
- **Фабрика-кухня:** `a large industrial culinary production building (dark kitchen) with loading docks`
- **ДПИР-хаб:** `a prominent modern civic / digital hub building, ecosystem control center`
- **МБМ:** `a modern mid-rise office business center`
- **ФСК (банк):** `a classic bank building with columns and a portico`
- **ФПСП:** `a calm 6–7 floor office building with colored window accents`
- **Салон красоты:** `a typical ground-floor beauty-salon shopfront`
- **Магазин:** `a typical ground-floor retail store with a display window`

## Чек-лист после правки

- [ ] Размер кадра НЕ изменился (тот же W×H).
- [ ] За пределами маски пиксели не тронуты.
- [ ] Свет, угол, масштаб и палитра нового объекта совпали с окружением.
- [ ] Нет шва/ореола по краю маски.
- [ ] Нет текста/вывесок/логотипов на новом объекте.
