# Промпт — замена центрального здания на кластер «Ломоносов»

Меняем большое золотисто-стеклянное здание в центре-сверху слайда на **кластер «Ломоносов»**
(реальное современное здание с волнообразными ступенчатыми этажами-консолями и стеклянным
фасадом).

## Что прикрепить (по порядку)

1. **image 1 = сцена** — `Downloads/lomonosov_crop.png` (кроп слайда 375×145, аэро-вид сверху,
   золотой час). Это фон, в который встраиваем здание.
2. **image 2 = референс** — `Downloads/image 4.jpg` (кластер «Ломоносов», эталон здания).

## Куда вставлять обратно

Готовый отредактированный кроп вставить в `Слайд 1 изображение.png` в точку **x=760, y=70**
(размер кропа 375×145, не менять). Если нейросеть отдала кроп другого размера — ужать до
**375×145** перед вставкой.

---

## Промпт (вставлять в Nano Banana / GPT-image / Flux Kontext)

```
Two images attached. image 1 is the SCENE (a high aerial bird's-eye view of a summer city
district at golden hour). image 2 is the REFERENCE building — the "Lomonosov" cluster: a modern
glass office building with WAVY, STEPPED CANTILEVERED floor slabs (each upper floor steps out
over the one below in a smooth curved silhouette), full glass curtain-wall facade with thin
white horizontal bands between floors, 6-7 storeys.

TASK: In image 1, REPLACE the large golden-roofed glassy building in the CENTER with the
Lomonosov cluster building from image 2. Keep EVERYTHING ELSE in image 1 exactly the same —
the surrounding streets, smaller houses, trees, park, fountains, roads and the overall layout
and framing must stay identical. Only the one central building changes.

INTEGRATION RULES:
- Match the SCENE: same HIGH AERIAL oblique top-down angle (we look down onto the roof and
  upper facades), same golden-hour summer lighting, same warm low sun direction, same long soft
  shadows, same color grading and atmosphere as image 1.
- Keep the building on the SAME FOOTPRINT / ground plot as the building it replaces — same
  position, same realistic scale relative to neighbours, standing firmly on the ground (not
  floating, not a cutout collage). Blend its base into the existing greenery and plaza.
- Reproduce the reference faithfully: the recognizable WAVY stepped cantilever floors and the
  glass facade must be clearly readable from above. Adapt only the viewing angle and light to
  fit the aerial scene; do NOT redesign the architecture.
- Photorealistic, seamless, consistent resolution and sharpness with image 1 — NO quality drop,
  NO blur, NO visible seams or pasted edges.

CLEAN PLATE: NO text, NO captions, NO letters, NO numbers, NO signs, NO banners, NO billboards,
NO logos, NO UI, NO labels on or around the building. The building is recognizable by its
ARCHITECTURE only. Do NOT add any media-screen text from the reference photo.
```

---

## Чек-лист приёмки

- [ ] На месте центрального здания — кластер «Ломоносов» (волнистые ступенчатые этажи, стекло).
- [ ] Ракурс сверху, золотой час, тени и цвет совпадают с остальной картинкой.
- [ ] Здание стоит на земле на том же участке, масштаб как у соседей, без «коллажного» канта.
- [ ] Всё вокруг (улицы, дома, парк, фонтаны) не изменилось.
- [ ] Нет ни букв, ни вывесок, ни экранов с текстом (рекламный баннер с референса убран).
- [ ] Качество/резкость как у оригинала, без блюра и швов.
- [ ] Кроп вернуть размером 375×145 в точку x=760, y=70.
```
