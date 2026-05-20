# Arbeidshefte – HTML og JavaScript
### Arrays · Løkker · If-else · Variabler · Funksjoner

> **Slik jobber du:**
> - Oppgave 1–3: Kopier startkoden inn i en ny `.html`-fil og fyll inn der det står `// TODO`.
> - Oppgave 4–6: Lag en helt ny `.html`-fil for hver oppgave og bygg nettsiden fra bunnen av.
> - Test alltid i nettleseren underveis!

---

## Oppgave 1 – Min spilliste 🎵

Du skal lage en nettside som viser og administrerer en musikksplilliste.

**Startkode – kopier denne og fyll inn der det står `// TODO`:**

```html
<!DOCTYPE html>
<html lang="no">
<head>
    <meta charset="UTF-8">
    <title>Min spilliste</title>
</head>
<body>
    <h1>🎵 Min spilliste</h1>
    <input type="text" id="inpSang" placeholder="Sangnavn">
    <br><br>
    <button onclick="visSanger()">Vis spilliste</button>
    <button onclick="leggTilSang()">Legg til sang</button>

    <div id="txtUt"></div>

    <script>
        let spilliste = ["Blinding Lights", "APT.", "luther", "BIRDS OF A FEATHER"];

        let txtUt = document.getElementById("txtUt");

        function visSanger() {
            txtUt.innerHTML = "<h2>Spillisten min</h2><ul>";
            for (let i = 0; i < spilliste.length; i++) {
                // TODO: Legg til hvert sangnavn som et <li>-element
                // Bruk spilliste[i] og += på txtUt.innerHTML

            }
            // TODO: Avslutt ul-taggen

        }

        function leggTilSang() {
            // TODO: Les inn sangnavn fra input-feltet med id "inpSang"
            let sang = "";

            // TODO: Legg til sangen i spilliste-arrayet

            // TODO: Vis en bekreftelsesmelding i txtUt, f.eks. "Lagt til: [sangnavn]"

        }
    </script>
</body>
</html>
```

**Når du er ferdig skal du kunne:**
- Klikke «Vis spilliste» og se alle sangene som en liste
- Skrive inn en sang og klikke «Legg til sang» – sangen skal dukke opp i listen

---

## Oppgave 2 – Alderssjekk for konsert 🎤

En konsertarrangør trenger en nettside som sjekker om besøkende er gamle nok til å komme inn.

**Startkode – kopier og fyll inn:**

```html
<!DOCTYPE html>
<html lang="no">
<head>
    <meta charset="UTF-8">
    <title>Konsertsjekk</title>
</head>
<body>
    <h1>🎤 Konsertsjekk</h1>
    <p>Skriv inn alderen din for å sjekke om du kommer inn.</p>

    <input type="number" id="inpAlder" placeholder="Din alder">
    <br><br>
    <button onclick="sjekkAlder()">Sjekk</button>

    <div id="txtUt"></div>

    <script>
        let txtUt = document.getElementById("txtUt");

        function sjekkAlder() {
            // TODO: Les inn alder fra input-feltet og konverter til tall med Number()
            let alder = 0;

            // TODO: Sjekk alderen med if-else og vis riktig melding i txtUt:
            // - Under 13: "Du er for ung til å gå på konsert alene."
            // - 13–17: "Du kan komme inn med foresatte."
            // - 18 eller eldre: "Velkommen inn! God konsert!"

        }
    </script>
</body>
</html>
```

**Krav:**
- Tre ulike meldinger basert på alder (se kommentarene i koden)
- Testen skal fungere for alle gyldige tall

---

## Oppgave 3 – Karakter­kalkulator 📊 *(litt vanskeligere)*

Du skal lage en nettside der læreren kan legge inn karakterer for en klasse, og nettsiden regner ut gjennomsnittet og viser hvem som stryk.

**Startkode – kopier og fyll inn:**

```html
<!DOCTYPE html>
<html lang="no">
<head>
    <meta charset="UTF-8">
    <title>Karakterkalkulator</title>
</head>
<body>
    <h1>📊 Karakterkalkulator</h1>
    <input type="number" id="inpKarakter" placeholder="Karakter (1–6)" min="1" max="6">
    <input type="text" id="inpNavn" placeholder="Elevens navn">
    <br><br>
    <button onclick="leggTilElev()">Legg til elev</button>
    <button onclick="visResultater()">Vis resultater</button>

    <div id="txtUt"></div>

    <script>
        let elever = [];       // Hvert element: { navn: "...", karakter: ... }
        let txtUt = document.getElementById("txtUt");

        function leggTilElev() {
            let navn = document.getElementById("inpNavn").value;
            // TODO: Les inn karakter fra inpKarakter og konverter til tall med Number()
            let karakter = 0;

            // TODO: Sjekk at karakter er mellom 1 og 6 (if-else).
            // Hvis ugyldig: vis feilmelding og avslutt funksjonen med return.

            // TODO: Legg til et objekt { navn: navn, karakter: karakter }
            // i elever-arrayet med push()

            // TODO: Vis bekreftelse: f.eks. "Lagt til: [navn] med karakter [karakter]"

        }

        function visResultater() {
            if (elever.length === 0) {
                txtUt.innerHTML = "<p>Ingen elever lagt til ennå.</p>";
                return;
            }

            // TODO: Regn ut gjennomsnittet av alle karakterene
            // Tips: summer alle karakterer i en løkke, del på elever.length
            let sum = 0;

            // Sett inn løkke her:

            let gjennomsnitt = 0; // TODO: Beregn gjennomsnitt fra sum

            // TODO: Bygg opp en HTML-tabell eller liste som viser:
            // - Navn og karakter for hver elev
            // - Marker elever med karakter 1 eller 2 som "Stryk ⚠️"
            // - Gjennomsnittskarakteren på slutten (bruk toFixed(1) for én desimal)
            txtUt.innerHTML = "<h2>Resultater</h2>";

            // Sett inn kode her:

        }
    </script>
</body>
</html>
```

**Ekstra utfordringer:**
- Finn og vis hvem som fikk høyest karakter
- Sorter elevene fra høyest til lavest karakter før du viser dem
- Legg til en «Nullstill»-knapp som tømmer elever-arrayet

---

## Oppgave 4 – Treningsdagbok 💪

Lag en **komplett nettside** (ingen startkode!) som lar brukeren holde styr på treningsøkter.

**Nettsiden skal:**

1. Ha et array med noen forhåndslagde treningsøkter, f.eks.:
   ```
   ["Løping 5 km", "Styrketrening", "Svømming 30 min"]
   ```
2. Ha et inputfelt der brukeren kan skrive inn en ny treningsøkt
3. Ha tre knapper:
   - **«Vis treningsøkter»** – viser alle øktene som en nummerert liste (`<ol>`)
   - **«Legg til økt»** – legger til en ny økt og viser en bekreftelse
   - **«Fjern økt»** – fjerner en navngitt økt fra listen (bruk `indexOf` og `splice`). Gi feilmelding hvis økten ikke finnes.
4. Vise antall treningsøkter totalt under listen

**Krav til kode:**
- Minst én funksjon per knapp
- Bruk `for`-løkke til å bygge listen
- Bruk `if-else` i fjern-funksjonen

---

## Oppgave 5 – Quizapp 🧠 *(litt vanskeligere)*

Lag en **komplett quiz-nettside** med minst 5 spørsmål.

**Nettsiden skal:**

1. Lagre spørsmål og svar i et array med objekter:
   ```javascript
   let sporsmal = [
       { sporsmal: "Hva er hovedstaden i Norge?", svar: "Oslo" },
       { sporsmal: "Hva er 7 ganger 8?", svar: "56" },
       // ... flere spørsmål
   ];
   ```
2. Vise ett spørsmål om gangen (start med spørsmål 0)
3. Ha et inputfelt der brukeren skriver svaret sitt
4. Ha en **«Svar»**-knapp som:
   - Sjekker om svaret er riktig (ikke skill mellom store/små bokstaver – tips: `.toLowerCase()`)
   - Viser «Riktig! ✅» eller «Feil ❌ – riktig svar er: [svar]»
   - Går automatisk videre til neste spørsmål
5. Holde styr på poengsummen (én variabel som øker for hvert riktige svar)
6. Vise en avslutningsmelding når alle spørsmål er besvart:
   - Under 3 poeng: «Øv mer!»
   - 3–4 poeng: «Bra jobbet!»
   - 5 poeng: «Perfekt score! 🏆»

**Ekstra utfordring:**
- Legg til en «Start på nytt»-knapp som nullstiller quizen
- Bland rekkefølgen på spørsmålene tilfeldig med `Math.random()`

---

## Oppgave 6 – Spillbutikk 🛒 *(litt vanskeligere)*

Lag en **komplett nettside** som simulerer en enkel spillbutikk med handlekurv.

**Nettsiden skal:**

1. Ha et array med spill (objekter med navn og pris):
   ```javascript
   let spill = [
       { navn: "Minecraft", pris: 249 },
       { navn: "FIFA 25", pris: 699 },
       { navn: "Hogwarts Legacy", pris: 499 },
       { navn: "Fortnite V-Bucks pakke", pris: 149 },
       { navn: "Elden Ring", pris: 599 }
   ];
   ```
2. Vise alle spillene med navn og pris som en liste når siden lastes (kall funksjonen automatisk)
3. Ha et inputfelt der brukeren skriver inn spillnavnet de vil kjøpe
4. Ha en **«Legg i handlekurv»**-knapp som:
   - Sjekker om spillet finnes (bruk løkke og `if`)
   - Legger det til i et eget `handlekurv`-array
   - Viser bekreftelse eller feilmelding
5. Ha en **«Vis handlekurv»**-knapp som:
   - Lister opp alle spill i kurven
   - Viser totalsum nederst
   - Viser «Handlekurven er tom» hvis ingenting er lagt til
6. Ha en **«Tøm kurv»**-knapp som nullstiller handlekurven

**Krav til kode:**
- Bruk løkke for å søke gjennom `spill`-arrayet
- Bruk løkke for å regne ut totalsum
- Bruk `if-else` for å håndtere feil input

**Ekstra utfordring:**
- Hindre at samme spill kan legges til to ganger
- Legg til en «Fjern fra kurv»-funksjon
- Vis antall varer i kurven ved siden av «Vis handlekurv»-knappen

---

## Huskeliste – nyttige JavaScript-triks

| Hva du vil gjøre | Kode |
|---|---|
| Hente tekst fra inputfelt | `document.getElementById("id").value` |
| Konvertere tekst til tall | `Number(verdi)` |
| Vise innhold i et element | `element.innerHTML = "tekst"` |
| Legge til innhold | `element.innerHTML += "mer tekst"` |
| Legge til i array | `array.push(verdi)` |
| Finn indeks i array | `array.indexOf(verdi)` |
| Fjern element fra array | `array.splice(indeks, 1)` |
| Antall elementer | `array.length` |
| Avrund desimaltall | `tall.toFixed(1)` |
| Gjør tekst til lowercase | `tekst.toLowerCase()` |
| Tilfeldig tall 0–1 | `Math.random()` |
