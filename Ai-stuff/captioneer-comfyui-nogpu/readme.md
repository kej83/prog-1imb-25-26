# Comfyui image captioneer moondream2

Her er en steg-for-steg guide til hvordan dere installerer og setter opp ComfyUI på Windows-maskiner uten dedikert grafikkort (GPU). Siden PC-ene skal bruke prosessoren (CPU), velger vi **Moondream2**, som er en ekstremt lettvektig "Vision LLM" som er perfekt for bildebeskrivelser (captioning).

## 1. Nedlasting og Installasjon

Siden skole-PC-er ofte har begrensninger, bruker vi den "portable" versjonen. Den krever ingen tradisjonell installasjon.

1. Gå til [ComfyUI sin GitHub-side](https://github.com/comfyanonymous/ComfyUI/releases).
2. Finn den øverste "Release"-posten og last ned filen som heter **`ComfyUI_windows_portable_nvidia_or_cpu.7z`**.
3. Pakk ut filen (høyreklikk -> pakk ut alle) til et sted elevene har skrivetilgang, for eksempel på skrivebordet eller i en egen mappe i "Dokumenter".

---

## 2. Oppstart i CPU-modus

Fordi PC-ene ikke har GPU, må ComfyUI tvinges til å bruke prosessoren.

1. Åpne mappen du nettopp pakket ut.
2. Finn filen som heter **`run_cpu.bat`**.
3. Dobbeltklikk på denne. Et svart vindu (terminal) vil åpne seg, og etter litt tid vil ComfyUI starte i nettleseren din (vanligvis på adressen `http://127.0.0.1:8188`).

---

## 3. Installer ComfyUI Manager

For å enkelt kunne legge til LLM-funksjonalitet, trenger vi "Manageren".

1. Gå inn i mappen `ComfyUI_windows_portable > ComfyUI > custom_nodes`.
2. Hold inne **Shift** og **høyreklikk** i et tomt område i mappen, og velg "Åpne i Terminal" (eller PowerShell).
3. Skriv inn følgende kommando og trykk Enter:
`git clone https://github.com/ltdrdata/ComfyUI-Manager.git`
*(Hvis PC-en mangler Git, kan du laste ned Manageren som en ZIP-fil fra lenken over og pakke den ut i denne mappen manuelt).*
4. **Start ComfyUI på nytt** ved å lukke terminalvinduet og kjøre `run_cpu.bat` igjen.

---

## 4. Legg til Moondream (Den lokale LLM-en)

Nå skal vi installere nodene som lar oss bruke en liten språkmodell.

1. Klikk på den nye **Manager**-knappen i ComfyUI-menyen til høyre.
2. Klikk på **Custom Nodes Manager**.
3. Søk etter "Moondream" og klikk **Install** på `ComfyUI-moondream`.
4. Når installasjonen er ferdig, klikk **Restart** (eller lukk og start `run_cpu.bat` på nytt).

---

## 5. Lag arbeidsflyten (Workflow)

Nå skal vi bygge det "minimale eksempelet". Slett alt som ligger på skjermen fra før (velg alt med musa og trykk Delete).

### Steg for steg oppsett:

1. **Høyreklikk på bakgrunnen** -> `Add Node` -> `image` -> `Load Image`. (Her laster elevene opp bildet sitt).
2. **Høyreklikk** -> `Add Node` -> `moondream2` -> `Moondream Model Loader`. (Dette laster selve "hjernen").
3. **Høyreklikk** -> `Add Node` -> `moondream2` -> `Moondream Caption`. (Dette er noden som gjør jobben).
4. **Koble dem sammen:**
* Dra en linje fra **IMAGE** på *Load Image* til **md2_image** på *Moondream Caption*.
* Dra en linje fra **MODEL** på *Model Loader* til **model** på *Moondream Caption*.


5. **Vis resultatet:**
* Høyreklikk -> `Add Node` -> `utils` -> `Show Text`. (Hvis denne ikke finnes, kan du dra en linje fra **STRING**-utgangen på Moondream Caption og slippe den i tomme lufta, velg så "Show Text").



---

## 6. Test arbeidsflyten

1. Last opp et enkelt bilde i **Load Image**-noden.
2. Trykk på den grønne knappen **Queue Prompt** i menyen til høyre.
3. Følg med i terminalvinduet (det svarte vinduet). Første gang vil den laste ned modellen (ca. 1-2 GB). Dette tar noen minutter avhengig av nettverket.
4. Når den er ferdig, vil beskrivelsen av bildet dukke opp i **Show Text**-noden!

> **Tips til læreren:** Moondream2 krever kun ca. 4-8 GB RAM og fungerer overraskende raskt på moderne CPU-er. Hvis elevene vil ha mer detaljerte svar, kan de endre `length` i noden fra "short" til "long".

## Ekstra materiale
[Guide til installasjon og bruk av ComfyUI](https://www.youtube.com/watch?v=ZQFqUdIYgdg)

Denne videoen viser hvordan man setter opp ComfyUI på maskiner uten kraftig maskinvare, slik at dere får en visuell forståelse av prosessen.