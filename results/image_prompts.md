# Промпты иллюстраций «Штаб по защите бизнеса» (GPT/DALL-E/Sora)

Дата: 2026-06-08
Генератор: GPT/DALL-E/Sora · Соотношение: 16:9 · Слайдов в этом файле: 2 (титул + уровень 1)

---

## STYLE-ANCHOR (вставляется в каждый промпт дословно)

> Cinematic AAA video-game key art, Call-of-Duty-grade rendering quality, hi-tech tactical
> command-center aesthetic (a strategic war-room for business, NO weapons, NO violence,
> NO soldiers). Isometric 3D strategy-map of a modern, futuristic Moscow. Glowing holographic
> HUD overlay with game indicators. Dark navy-blue and steel palette with a single neon-cyan
> accent and warm gold highlights. Volumetric dramatic lighting, soft fog, sharp depth of
> field. The SAME recurring hero: a young male entrepreneur, short dark hair, light casual
> outfit (t-shirt), friendly determined face — identical across all images. 16:9 aspect ratio,
> ultra-detailed, clean professional look suitable for a corporate government presentation.

## Эталон стиля
Слайд 4 (Штаб) — самый эффектный, но генерировать первым лучше **Слайд 1**: он задаёт героя и
палитру. Слайд 0 (титул) подгоняй под уже полученный стиль слайда 1.

---

## Слайд 0 — Титул / Loading

```
Cinematic AAA video-game key art, Call-of-Duty-grade rendering quality, hi-tech tactical
command-center aesthetic (a strategic war-room for business, NO weapons, NO violence, NO
soldiers). Isometric 3D strategy-map of a modern, futuristic Moscow. Glowing holographic HUD
overlay with game indicators. Dark navy-blue and steel palette with a single neon-cyan accent
and warm gold highlights. Volumetric dramatic lighting, soft fog, sharp depth of field. 16:9
aspect ratio, ultra-detailed, clean professional look suitable for a corporate government
presentation.
SCENE: a game start / loading screen. A vast isometric futuristic Moscow skyline emerging from
fog in the background, city districts faintly glowing as locked levels. Centered big cinematic
title.
HUD: large holographic title text "MOSCOW BUSINESS QUEST", a subtitle bar "Loading the
entrepreneur's world...", a neon-cyan loading progress bar at ~90%, small label "Shtab for
Business Protection · DPIiR Moscow".
MOOD: epic, anticipatory, deep night-blue with cyan glow, cinematic intro vibe. --ar 16:9
avoid: weapons, guns, soldiers, blood, war, different character faces between images, flat 2D
cartoon, low detail, garbled text, changing color palette.
```

---

## Слайд 1 — Уровень 1. Старт бизнеса

```
Cinematic AAA video-game key art, Call-of-Duty-grade rendering quality, hi-tech tactical
command-center aesthetic (a strategic war-room for business, NO weapons, NO violence, NO
soldiers). Isometric 3D strategy-map of a modern, futuristic Moscow. Glowing holographic HUD
overlay with game indicators. Dark navy-blue and steel palette with a single neon-cyan accent
and warm gold highlights. Volumetric dramatic lighting, soft fog, sharp depth of field. 16:9
aspect ratio, ultra-detailed, clean professional look suitable for a corporate government
presentation.
SCENE: an isometric futuristic Moscow start-zone. In the foreground a glowing launch pad
labeled "BUSINESS IDEA". Far in the background, faded in fog, locked future levels: office
towers, a factory, a cafe, trade buildings, innovation centers. The path forward lights up
from the pad.
CHARACTER: the same young male entrepreneur (short dark hair, light t-shirt, friendly
determined face) standing on the launch pad, scratching the back of his head, looking ahead
at the route with optimism.
HUD: holographic game panel top-right reading "Player: Entrepreneur of Moscow", "Level 1/5",
"Status: Start of the journey"; floating skill icons above the hero — idea bulb, energy bolt,
clipboard plan; an objective marker "Open a business".
MOOD: optimistic warm sunrise glow mixed with cyan HUD light, soft morning fog, big-opportunity
feeling, start of a great journey. --ar 16:9
avoid: weapons, guns, soldiers, blood, war, different character faces between images, flat 2D
cartoon, low detail, garbled text, changing color palette.
```

---

## Как держать единый стиль
- Генерируй **слайд 1 первым** — он задаёт лицо/одежду героя и палитру. Сохрани картинку.
- Для слайда 0 и следующих добавляй в конце промпта: `keep the SAME character and SAME art
  style as the previous image, only change the scene`.
- По возможности прикладывай картинку слайда 1 как референс-изображение.
- seed-описание героя (`short dark hair, light t-shirt, friendly determined face`) повторяй
  в каждом промпте дословно — не перефразируй.
- HUD-надписи в GPT/DALL-E могут искажаться — если текст «поплыл», добавь надписи в HTML
  поверх картинки, а не в саму генерацию.

Промпты картинок собраны (титул + слайд 1) — стиль единый, можно генерировать.
