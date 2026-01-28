# ComfyUI Txt2Img Lab (Z-Image Turbo) — Workflow-basert

Når comfyui kjører, drag and drop `z_image_turbo_example.json` på comfyui.

---

## Levering

Lag **én Word-fil (.docx)** med:

* skjermklipp/bilder fra hver oppgave
* kort tekst: *hva du endret* (1 setning holder)
* for hvert bilde: skriv ned **Seed, Steps, CFG, Sampler, Scheduler, Resolution**, og evt. **Negative prompt**

---

# Oppgave 1: Queue (vis at du kan kjøre kø)

1. Bruk baseline.
2. Trykk **Queue Prompt** 3 ganger på rad.

**I Word:** 1 skjermklipp som viser at du har flere jobber i kø.

---

# Oppgave 2: Sampling steps (1, 3, 6, 9)

**Hold seed og prompt fast (baseline seed = fixed).**

Kjør 4 bilder:

* Steps = **1**
* Steps = **3**
* Steps = **6**
* Steps = **9** (baseline)

**I Word:** 4 bilder + én setning: “Jeg endret steps.”

---

# Oppgave 3: Seed + små endringer i lang prompt (fixed seed)

**Her skal seed fortsatt være fixed (baseline seed).**

1. Lag **prompt A** (gjerne lang, 25+ ord).
2. Generer bilde A.
3. Endre **kun én liten detalj** i prompten → generer bilde B.
4. Endre **kun én liten detalj** igjen → generer bilde C.

**I Word:** 3 bilder (A/B/C) + vis hvilken liten endring du gjorde (f.eks. fet tekst).

---

# Oppgave 4: Sampler + Scheduler (prompt og seed fixed)

**Hold prompt og seed fast. Bytt bare sampler/scheduler.**

Lag 3 bilder:

1. Baseline: **euler + simple**
2. Bytt **sampler** til en annen (f.eks. `euler_a`, `dpmpp_2m`, osv. det dere har i lista) — scheduler fortsatt `simple`
3. Velg en **annen scheduler** (det dere har tilgjengelig) + sampler (valgfritt om du vil beholde #2 sampler)

**I Word:** 3 bilder + noter sampler/scheduler under hvert.

---

# Oppgave 5: Resolution (prompt og seed fixed)

**Hold prompt, seed, steps, cfg, sampler/scheduler fast. Endre bare resolution.**

Lag 3 bilder med samme fixed seed og prompt, men med ulike oppløsninger (velg tre som blant disse som er anbefalt):

1024 x 1024
1152 x 896
896 x 1152
1216 x 832
832 x 1216
1344 x 768
768 x 1344
1536 x 640
640 x 1536

**I Word:** 3 bilder + resolution under hvert.

---

# Oppgave 6: CFG + Negative prompt (Z-Image Turbo)

Baseline CFG er **1**. Her tester du litt høyere.

## 6A — CFG test (samme prompt + fixed seed)

Lag 3 bilder:

* CFG **1.0** (baseline)
* CFG **1.5**
* CFG **2.0**

## 6B — Negative prompt test (samme seed + samme CFG)

Velg CFG **1.5** eller **2.0**, lag 2 bilder:

* Negative prompt = tom
* Negative prompt = fylt inn

Forslag negative prompt (kopier):
`blurry, low quality, watermark, text, logo, deformed, extra fingers, bad anatomy, noisy, artifacts`

**I Word:** 5 bilder totalt + noter CFG og negative prompt.

---

## Minstekrav (må være med)

* Oppgave 1: 1 skjermklipp
* Oppgave 2: 4 bilder
* Oppgave 3: 3 bilder
* Oppgave 4: 3 bilder
* Oppgave 5: 3 bilder
* Oppgave 6: 5 bilder
  **Totalt: minst 19 bilder/skjermklipp**
