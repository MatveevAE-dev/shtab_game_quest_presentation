# Инструкция: генерация иллюстраций слайдов в едином стиле (GPT/DALL-E/Sora)

## Как использовать

Скажи Claude Code:
```
Прочитай инструкцию из файла prompts/02_image_prompts.md и собери промпты картинок.
Исходник сцен: Для презы.docx (или results/narrative.md, если сценарий уже собран).
```

Например:
```
Прочитай prompts/02_image_prompts.md и собери промпты иллюстраций под все слайды.
Сохрани в results/image_prompts.md.
```

---

## Инструкция для Claude Code

Ты — арт-директор и промпт-инженер по AI-иллюстрации, работающий с GPT/DALL-E/Sora. Твоя
задача — собрать готовые промпты картинок для всех слайдов так, чтобы они выглядели как кадры
одной игры.

### Ключевой принцип

**Единый STYLE-ANCHOR в КАЖДОМ промпте = консистентность.**

Картинки разваливаются на «разные игры», когда стиль описан по-разному. Поэтому фикс-блок
стиля (палитра, ракурс, освещение, тип персонажа) копируется в каждый промпт дословно, а
меняется только описание сцены.

---

### STYLE-ANCHOR (фикс-блок — копируй дословно в каждый промпт)

> Cinematic AAA video-game key art, Call-of-Duty-grade rendering quality, hi-tech tactical
> command-center aesthetic (a strategic war-room for business, NO weapons, NO violence,
> NO soldiers). Isometric 3D strategy-map of a modern, futuristic Moscow. Glowing holographic
> HUD overlay with game indicators. Dark navy-blue and steel palette with a single neon-cyan
> accent and warm gold highlights. Volumetric dramatic lighting, soft fog, sharp depth of
> field. The SAME recurring hero: a young male entrepreneur, short dark hair, light casual
> outfit (t-shirt), friendly determined face — identical across all images. 16:9 aspect ratio,
> ultra-detailed, clean professional look suitable for a corporate government presentation.

> **Допущение:** промпты пишутся на английском — GPT/DALL-E дают более стабильный game-art
> по англоязычному описанию. Если нужен русский — переведи, но style-anchor держи единым.

### Шаг 0: Изучи входные данные

Прочитай `Для презы.docx` (или `results/narrative.md`). Для каждого слайда извлеки:
- что за сцена (старт / первый бизнес / развилки / командный центр);
- какие объекты на карте (кафе, офис, центр поддержки, Штаб);
- что делает герой;
- какие HUD-элементы и надписи описаны (статусы, индикаторы, названия объектов).

### Шаг 1: Зафиксируй якорь

Скопируй STYLE-ANCHOR без изменений. Он будет началом каждого промпта.

### Шаг 2: Собери промпт под каждый слайд

Для каждого слайда заполни слоты по формуле:

```
[STYLE-ANCHOR] + [SCENE] + [CHARACTER ACTION] + [HUD/UI TEXT] + [LIGHTING/MOOD] + [16:9]
```

- **SCENE** — что в кадре и где (объекты карты, масштаб города).
- **CHARACTER ACTION** — что делает тот же герой (стоит на старте / у своего кафе / у развилки).
- **HUD/UI TEXT** — какие надписи и индикаторы наложены поверх (бери из docx: «Уровень 1»,
  «ИП зарегистрировано ✓», название объекта и т.д.).
- **LIGHTING/MOOD** — настроение света под атмосферу уровня (оптимизм → рассвет; кульминация
  Штаба → драматичный неон).

### Шаг 3: Удержание персонажа и стиля между картинками

Чтобы герой и стиль не «плыли»:
- В каждом промпте повторяй seed-описание героя дословно (та же внешность, та же одежда).
- Сгенерируй слайд 1, затем для слайдов 2–6 проси: «keep the SAME character and SAME art
  style as the previous image, only change the scene».
- При возможности прикладывай первую картинку как референс.
- Помечай в выводе, какой слайд — «эталон стиля» (обычно слайд 4, Штаб — самый эффектный).

### Шаг 4: Проверка единства

Перед выдачей пройди глазами: одинаковая палитра? один ракурс изометрии? один герой? один
тип HUD? Если слайд выбивается — перепиши слот, не трогая anchor.

---

### Шаблоны формулировок

**Структура одного промпта:**
```
[STYLE-ANCHOR дословно].
SCENE: [объекты, масштаб карты, что нового появилось].
CHARACTER: the same hero [действие].
HUD: glowing overlay reading "[надпись 1]", "[надпись 2]", level indicator "[N/5]".
MOOD: [свет/атмосфера]. --ar 16:9
```

**Negative / avoid (добавляй в конце или в negative-поле):**
```
avoid: weapons, guns, soldiers, blood, war, different character faces between images,
flat 2D cartoon, low detail, text errors, changing color palette.
```

---

### Примеры

**✅ Хорошо — измеримо и со слотами:**
```
[STYLE-ANCHOR]. SCENE: isometric futuristic Moscow start-zone, a glowing launch pad labeled
"BUSINESS IDEA", distant locked levels (office towers, factories, cafes) faded in fog.
CHARACTER: the same young entrepreneur standing on the pad, scratching his head, looking at
the route ahead. HUD: holographic panel "Player: Entrepreneur of Moscow / Level 1 / Status:
Start", floating icons idea 💡 motivation ⚡ plan 📋. MOOD: optimistic sunrise glow, soft fog.
--ar 16:9
```

**❌ Плохо — абстракция, стиль развалится:**
```
Нарисуй красивую современную картинку про начало бизнеса в Москве, ярко и технологично.
```

**❌ Плохо — милитари (это бизнес-штаб, не война):**
```
…a military command bunker with soldiers and weapons coordinating an assault… (запрещено)
```

---

### Формат результата

Сохрани результат в файл `results/image_prompts.md` со структурой:

```markdown
# Промпты иллюстраций «Штаб по защите бизнеса» (GPT/DALL-E/Sora)

Дата: [дата]
Генератор: GPT/DALL-E/Sora · Соотношение: 16:9 · Слайдов: [N]

## STYLE-ANCHOR (вставляется в каждый промпт)
> [фикс-блок дословно]

## Эталон стиля: Слайд [N] — генерировать первым

## Слайд 0 — Титул / Loading
```
[полный промпт]
```
avoid: [...]

## Слайд 1 — Старт бизнеса
```
[полный промпт]
```
avoid: [...]

## … (остальные слайды)

## Как держать единый стиль
- [3–4 пункта: seed-описание героя, «same style as previous», референс-картинка]
```

---

### Важные правила

1. **Без милитари** — никаких оружия, солдат, насилия. Штаб = командный центр для бизнеса,
   эстетика тактическая, но мирная.
2. **Не меняй палитру и ракурс между слайдами** — иначе картинки не склеятся в одну игру.
3. **Только измеримые визуальные параметры** — не «красиво/современно», а конкретные объекты,
   цвета, свет, ракурс.
4. **Один и тот же герой** — seed-описание внешности повторяется дословно в каждом промпте.
5. **STYLE-ANCHOR неприкосновенен** — между слайдами меняются только слоты SCENE/CHARACTER/HUD.

### Условие выхода

Готово, когда для каждого слайда собран полный промпт + negative-блок, указан эталон стиля,
и файл сохранён. Закончи фразой: «Промпты картинок собраны — стиль единый, можно генерировать».
