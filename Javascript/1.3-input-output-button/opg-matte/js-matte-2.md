# Oppgavesett input output beregninger

## Oppgave 1 – MVA-kalkulator (ferdig HTML, skriv all JS selv)

**Brukeren oppgir pris uten MVA og MVA-prosent. Vis MVA i kroner og pris med MVA.**

**Krav (logikk som elevene lager i JS):**

* Les to tall fra input: pris uten MVA og MVA-prosent.
* Beregn: `mvaKr = pris * prosent / 100` og `prisMed = pris + mvaKr`.
* Vis en tekstlinje med alle tre verdier (pris uten MVA, MVA i kr, pris med MVA).

**Ferdig HTML (JS skal elevene skrive i `<script>`-feltet):**

```html
<!DOCTYPE html>
<html lang="no">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>MVA-kalkulator</title>
</head>
<body>
  <h1>MVA-kalkulator</h1>
  <p>Oppgi pris uten MVA og MVA-prosent. Programmet viser MVA i kroner og pris med MVA.</p>

  <label for="inpPris">Pris uten MVA:</label>
  <input type="number" id="inpPris" step="0.01">

  <label for="inpMva">MVA-prosent (f.eks. 25):</label>
  <input type="number" id="inpMva" value="25" step="0.01">

  <button onclick="beregn()">Beregn</button>
  <p id="txtUt"></p>

  <script>
    function beregn(){
    // Skriv all JavaScript her.
    // Tips: Hent elementer med document.getElementById(...)
    }


  </script>
</body>
</html>
```

---

# Oppgave 2 – Bilde-størrelse (3:4-forhold) (ferdig HTML, skriv all JS selv)

**Brukeren oppgir høyde i piksler. Regn ut bredde for 3:4-forhold og vis “bredde × høyde px”.**

**Krav (logikk som elevene lager i JS):**

* Les høyde som tall.
* Bredde = `høyde * (3/4)`.
* Vis resultatet på formen `Størrelse: bredde × høyde px`.

**Ferdig HTML (JS skal elevene skrive i `<script>`):**

```html
<!DOCTYPE html>
<html lang="no">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Bilde-størrelse 3:4</title>
</head>
<body>
  <h1>Bilde-størrelse (3:4)</h1>
  <p>Oppgi høyde i piksler. Programmet regner ut bredde.</p>

  <label for="inpHoyde">Høyde (px):</label>
  <input type="number" id="inpHoyde" value="1536">

  <button onclick="beregn()">Beregn</button>
  <p id="txtUt"></p>

  <script>
    
    // Skriv all JavaScript her.
    // Tips: Bredde = høyde * 3 / 4
  </script>
</body>
</html>
```

---

# Oppgave 3 – Kinobilletter (skriv all HTML + JS selv)

Lag en side som regner totalpris for kinobilletter.

**Priser**

* Voksen: 140 kr
* Barn: 90 kr
* Student: 120 kr

**Krav**

1. Lag tre antallsfelt (number) for voksen/barn/student og en knapp “Beregn total”.
2. Regn ut total = (voksen×140) + (barn×90) + (student×120).
3. Vis resultatet i en tekstlinje, f.eks. `Totalpris: 470 kr`.

*(Kun regning og visning – ingen if/else.)*

---

# Oppgave 4 – Karakter-snitt (skriv all HTML + JS selv)

Brukeren skriver inn karakterer (1–6) separert med komma, f.eks. `5,4,6,3`. Vis snittet med to desimaler.

**Krav**

1. Ett tekstfelt og en knapp “Beregn snitt”.
2. Del opp strengen på komma (`split`), gjør om til tall (`Number`). Bruk chatgpt el. for å finne ut hvordan.
3. Regn ut gjennomsnitt = sum / antall.
4. Vis `Snitt: 4.50` (to desimaler med `toFixed(2)`).


---

## Ekstraoppgave (frivillig, introduserer if/else – knyttet til Oppgave 4)

Utvid Oppgave 4 slik at programmet også skriver en **vurderingstekst** basert på snittet (her får de bruke `if/else`):

* Snitt ≥ 5.0 → “Svært godt!”
* 4.0–4.99 → “Bra innsats.”
* 3.0–3.99 → “Godkjent, men kan forbedres.”
* < 3.0 → “Trenger mer arbeid.”

Vis til slutt både snitt og vurdering, f.eks.:

```
Snitt: 4.50
Vurdering: Bra innsats.
```

---
