# Kom igang med bildegenerering

## Google colab

### Oppsett
1. Gå til [google colab](https://colab.google/)
2. Lag bruker eller sign inn med google.
3. Gå til [ngrok](https://ngrok.com/)
4. Lag bruker på ngrok og logg inn.
5. Finn din API-key på ngrok og ta vare på den.

### Colab notebook
1. Lag en ny notebook på google colab.
2. Last ned notebook i denne mappa.
3. Åpne notebook `comfyui_mwe_v2_to_students.ipynb` i google colab.
4. Velg runtime øverst til høyre, og velg `T4 GPU`.
5. Kjør en og en celle.
6. I cella med ngrok, bytt ut KEY med din egen API-key.
7. Når alle cellene er kjørt, åpner du til slutt URLen du får fra cella til ngrok.

### Bruke workflow
1. Last ned `txt2img-sdxl.json` og dra denne oppå COMFYUI.
2. Endre prompt og trykk `RUN`.

### Guide til prompting
1. Last ned guiden `Creating Photorealistic Images With AI.pdf`.
2. Se hvordan du kan strukturere prompts. Forsøk forskjellige stiler, kameraer, vinkler, fotografer osv.

*NB*: Ikke all bildemodeller kjenner alle fotografer osv. Bare å prøve seg frem. 