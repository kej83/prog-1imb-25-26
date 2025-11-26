# OPPGAVE 1ima: Arbeid med array
### Klasseliste og poeng-statistikk for en turnering

**Du kan bruke alle hjelpemidler.**

Du skal lage JavaScript-kode til en ferdig webside for å holde orden på:

1. En **klasseliste** (navn på elever)
2. En liste med **poeng** (tall) fra en liten turnering

HTML og CSS er ferdig. Du skal **kun jobbe i `script.js`**.

### Det du skal få til med JavaScript

I `script.js` får du utlevert to arrays:

* `students` – en liste med navn (tekst)
* `scores` – en liste med poeng (tall)

Du skal:

1. **Skrive ut klasselista på siden**

   * Når siden lastes, skal navnene vises i boksen "Klasseliste".
   * Vis også hvor mange elever det er (`length`).

2. **Legge til og fjerne elever (students-array)**

   * Når du skriver inn et navn i feltet "Nytt navn" og trykker **"Legg til elev"**:

     * Legg navnet til i `students` med `push()`.
     * Oppdater visningen.
   * Når du trykker **"Fjern siste elev"**:

     * Fjern siste elev med `pop()`.
     * Oppdater visningen.

3. **Sortere og snu rekkefølgen på elever**

   * Når du trykker **"Sorter navn (A–Å)"**:

     * Lag en **ny** sortert liste av navn (f.eks. med `toSorted()` eller `slice().sort()`).
     * Vis den sorterte lista (du skal ikke ødelegge originalen hvis du bruker `toSorted()`).
   * Når du trykker **"Snu rekkefølgen"**:

     * Lag en **ny** liste med navn i omvendt rekkefølge (f.eks. `toReversed()` eller `slice().reverse()`).

4. **Søk etter navn**

   * Når du skriver et navn (eller deler av et navn) i feltet "Søk etter navn" og trykker **"Søk"**:

     * Bruk `includes()` på `students` for å sjekke om navnet finnes.
     * Vis en melding: enten at navnet finnes, eller at det ikke finnes.
     * (Bonus: gjør søket ikke-sensitivt på store/små bokstaver.)

5. **Jobbe med poeng (scores-array)**

   * Når du trykker **"Vis poengliste"**:

     * Vis alle tallene i `scores` i boksen "Poengliste".
   * Når du trykker **"Legg til tilfeldig poeng"**:

     * Lag et tilfeldig tall mellom f.eks. 0 og 20.
     * Legg tallet til i `scores` med `push()`.
     * Oppdater visningen.
   * Når du trykker **"Vis sum"**:

     * Bruk `reduce()` til å regne ut summen av alle poeng.
     * Vis summen i "Statistikk"-boksen.
   * Når du trykker **"Vis gjennomsnitt"**:

     * Bruk `reduce()` til å regne sum, del på `scores.length`.
     * Vis gjennomsnittet (gjerne avrundet med `toFixed(1)`).
   * Når du trykker **"Er det noen under 5 poeng?"**:

     * Bruk `some()` til å sjekke om minst ett poeng er under 5.
     * Vis en passende melding:

       * f.eks. "Ja, minst én har under 5 poeng 😬" ellers
       * "Ingen har under 5 poeng 💪".

6. **Litt personlighet med tekst**

   * Fyll inn et tomt HTML-element med en setning om deg selv, f.eks.
     "Hei, jeg heter ____ og jeg skal bli en ekte programmerings-nerd!"
   * Fyll inn et annet element med en positiv tekst, f.eks.
     "Jeg er et superflott menneske med gode verdier!"

---

## Ferdig HTML – `index.html`

Gi denne fila til elevene (eller la dem kopiere den). Bildet kan du bytte til noe du har tilgjengelig (bare behold `alt`-teksten).

```html
<!DOCTYPE html>
<html lang="nb">
<head>
  <meta charset="UTF-8" />
  <title>Klasseliste og poeng – Turnering</title>
  <link rel="stylesheet" href="style.css" />
  <script src="script.js" defer></script>
</head>
<body>
  <header>
    <h1>Turnering – Klasseliste og poeng</h1>
    <p>
      Denne siden brukes til å holde oversikt over hvem som er med i turneringen,
      og hvor mange poeng de har fått. Du skal programmere all logikk i JavaScript.
    </p>
    <img src="classroom.jpg" alt="Elever som jobber ved PC-er i et klasserom" class="hero-image" />
  </header>

  <main>
    <section class="panel">
      <h2>Klasseliste</h2>
      <p id="intro-text"></p>

      <div class="flex-row">
        <label for="new-student">Nytt navn:</label>
        <input type="text" id="new-student" placeholder="Skriv inn navn" />
        <button id="add-student-btn">Legg til elev</button>
        <button id="remove-last-student-btn">Fjern siste elev</button>
      </div>

      <div class="flex-row">
        <button id="sort-students-btn">Sorter navn (A–Å)</button>
        <button id="reverse-students-btn">Snu rekkefølgen</button>
      </div>

      <div class="flex-row">
        <label for="search-name">Søk etter navn:</label>
        <input type="text" id="search-name" placeholder="F.eks. Nora" />
        <button id="search-name-btn">Søk</button>
      </div>

      <p id="student-count"></p>
      <div id="student-list-output" class="output-box"></div>
      <p id="student-message" class="message"></p>
    </section>

    <section class="panel">
      <h2>Poeng og statistikk</h2>
      <p id="positive-text"></p>

      <div class="flex-row">
        <button id="show-scores-btn">Vis poengliste</button>
        <button id="add-random-score-btn">Legg til tilfeldig poeng</button>
      </div>

      <div class="flex-row">
        <button id="show-sum-btn">Vis sum</button>
        <button id="show-average-btn">Vis gjennomsnitt</button>
        <button id="check-failing-btn">Er det noen under 5 poeng?</button>
      </div>

      <div id="scores-output" class="output-box"></div>
      <div id="stats-output" class="output-box"></div>
    </section>
  </main>

  <footer>
    <p>Lagets super-nerder: <span id="footer-nerds"></span></p>
  </footer>
</body>
</html>
```

---

## Ferdig CSS – `style.css`

Enkel styling slik at alt ser ryddig ut. Elevene trenger ikke røre denne hvis du ikke vil.

```css
/* Enkel, ren stil slik at elevene kan fokusere på JavaScript */

* {
  box-sizing: border-box;
}

body {
  margin: 0;
  font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  background: #f4f4f8;
  color: #222;
}

header {
  background: #1f3b73;
  color: #fff;
  padding: 1.5rem 1rem 2rem;
  text-align: center;
}

header h1 {
  margin-top: 0;
  margin-bottom: 0.5rem;
}

header p {
  margin-top: 0;
  max-width: 700px;
  margin-left: auto;
  margin-right: auto;
}

.hero-image {
  margin-top: 1rem;
  max-width: 260px;
  width: 60%;
  border-radius: 12px;
  display: block;
  margin-left: auto;
  margin-right: auto;
}

main {
  max-width: 900px;
  margin: -1rem auto 2rem;
  padding: 0 1rem;
  display: grid;
  grid-template-columns: 1fr;
  gap: 1.5rem;
}

@media (min-width: 800px) {
  main {
    grid-template-columns: 1fr 1fr;
  }
}

.panel {
  background: #ffffff;
  border-radius: 16px;
  padding: 1.25rem;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
}

.panel h2 {
  margin-top: 0;
  margin-bottom: 0.75rem;
}

.flex-row {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
  align-items: center;
  margin-bottom: 0.75rem;
}

label {
  font-size: 0.9rem;
  font-weight: 600;
}

input {
  padding: 0.4rem 0.6rem;
  border-radius: 6px;
  border: 1px solid #ccc;
  min-width: 0;
  flex: 1 1 120px;
}

button {
  padding: 0.45rem 0.8rem;
  border-radius: 8px;
  border: none;
  cursor: pointer;
  background: #1f3b73;
  color: #fff;
  font-size: 0.9rem;
  transition: transform 0.05s ease, box-shadow 0.05s ease, background 0.1s ease;
}

button:hover {
  background: #25468f;
  box-shadow: 0 2px 6px rgba(0, 0, 0, 0.2);
  transform: translateY(-1px);
}

button:active {
  transform: translateY(0);
  box-shadow: none;
}

.output-box {
  min-height: 3rem;
  border-radius: 8px;
  border: 1px solid #ddd;
  padding: 0.6rem;
  background: #fafafa;
  font-family: "SF Mono", "Consolas", "Menlo", monospace;
  font-size: 0.9rem;
  white-space: pre-wrap;
}

.message {
  font-size: 0.9rem;
  font-weight: 600;
  margin-top: 0.4rem;
}

footer {
  text-align: center;
  padding: 1rem 0 1.5rem;
  font-size: 0.85rem;
  color: #555;
}
```

---

## Startkode for JavaScript – `script.js` (elevene fyller inn)

Her er et forslag til **startfil** der alle arrays er enkle datatyper, og alt arbeid skjer i JS. Du kan gi dem denne med oppgavekommentarer, eller fjerne noen kommentarer hvis du vil at de skal tenke mer selv.

```javascript
// ============================
// Startdata – ENKLE ARRAYS
// (Ikke bruk objekter inni arrays)
// ============================

const students = [
  "Ali",
  "Emma",
  "Jonas",
  "Sara",
  "Lukas",
  "Nora",
  "Maja",
  "Kevin"
];

const scores = [12, 7, 4, 9, 15, 2, 6, 11];

// ============================
// Hent HTML-elementer
// ============================

const introTextEl = document.getElementById("intro-text");
const positiveTextEl = document.getElementById("positive-text");
const footerNerdsEl = document.getElementById("footer-nerds");

const newStudentInput = document.getElementById("new-student");
const addStudentBtn = document.getElementById("add-student-btn");
const removeLastStudentBtn = document.getElementById("remove-last-student-btn");

const sortStudentsBtn = document.getElementById("sort-students-btn");
const reverseStudentsBtn = document.getElementById("reverse-students-btn");

const searchNameInput = document.getElementById("search-name");
const searchNameBtn = document.getElementById("search-name-btn");

const studentCountEl = document.getElementById("student-count");
const studentListOutput = document.getElementById("student-list-output");
const studentMessageEl = document.getElementById("student-message");

const showScoresBtn = document.getElementById("show-scores-btn");
const addRandomScoreBtn = document.getElementById("add-random-score-btn");
const showSumBtn = document.getElementById("show-sum-btn");
const showAverageBtn = document.getElementById("show-average-btn");
const checkFailingBtn = document.getElementById("check-failing-btn");

const scoresOutput = document.getElementById("scores-output");
const statsOutput = document.getElementById("stats-output");

// ============================
// 1. Tekst om deg selv
//    - Fyll inn introTextEl og positiveTextEl
// ============================

// TODO: skriv en tekst om deg selv inn i introTextEl med innerText eller innerHTML
// TODO: skriv en positiv tekst om deg selv i positiveTextEl
// TODO: fyll footerNerdsEl med navnene i students-arrayen (f.eks. join(", "))



// ============================
// 2. Funksjon som viser klasselisten
// ============================

// TODO: Lag en funksjon showStudents()
// - skal skrive ut alle navnene i students-arrayen i studentListOutput
// - f.eks. students.join("\n") for å få ett navn per linje
// - skal også oppdatere studentCountEl med antall elever (students.length)



// ============================
// 3. Legg til og fjern elever
// ============================

// TODO: Lag en funksjon addStudent()
// - les verdien fra newStudentInput
// - hvis tom streng: vis en melding i studentMessageEl og return
// - bruk students.push(navn)
// - tøm input-feltet
// - kall showStudents() igjen
// - nullstill studentMessageEl (evt. vis "Elev lagt til!" )

// TODO: Lag en funksjon removeLastStudent()
// - bruk students.pop()
// - kall showStudents()
// - vis en melding om hvilken elev som ble fjernet (husk å lagre return-verdien fra pop())



// ============================
// 4. Sortere og reversere navn
// ============================

// TODO: Lag en funksjon sortStudents()
// - lag en NY sortert liste (ikke ødelegg originalen hvis du vil)
//   f.eks. const sorted = students.toSorted(); eller students.slice().sort();
// - vis sorted-listen i studentListOutput (f.eks. sorted.join("\n"))

// TODO: Lag en funksjon reverseStudents()
// - lag en NY liste i motsatt rekkefølge
//   f.eks. const reversed = students.toReversed(); eller students.slice().reverse();
// - vis reversed-listen i studentListOutput



// ============================
// 5. Søk etter navn
// ============================

// TODO: Lag en funksjon searchStudent()
// - les søketeksten fra searchNameInput
// - bruk students.includes(...) for å sjekke om navnet finnes
// - du kan evt. gjøre students og søk til lowerCase() for å ignorere store/små bokstaver
// - vis resultat i studentMessageEl ("Navnet finnes i lista" / "Fant ikke navnet")



// ============================
// 6. Jobbe med poeng (scores-array)
// ============================

// TODO: Lag en funksjon showScores()
// - vis alle tallene i scores-arrayen i scoresOutput (f.eks. scores.join(", "))

// TODO: Lag en funksjon addRandomScore()
// - lag et tilfeldig tall mellom 0 og 20 (bruk Math.random())
// - bruk scores.push(detTilfeldigeTallet)
// - kall showScores() igjen

// TODO: Lag en funksjon showSum()
// - bruk reduce() til å summere alle tallene i scores
//   f.eks. const sum = scores.reduce((acc, current) => acc + current, 0);
// - vis summen i statsOutput

// TODO: Lag en funksjon showAverage()
// - bruk reduce() til å lage sum
// - del på scores.length
// - vis gjennomsnitt, gjerne avrundet: average.toFixed(1)

// TODO: Lag en funksjon checkFailing()
// - bruk some() til å sjekke om minst ett tall i scores er under 5
// - vis passende tekst i statsOutput



// ============================
// 7. Koble funksjoner til knapper
// ============================

// TODO: Bruk addEventListener for å koble:
// - addStudentBtn -> addStudent
// - removeLastStudentBtn -> removeLastStudent
// - sortStudentsBtn -> sortStudents
// - reverseStudentsBtn -> reverseStudents
// - searchNameBtn -> searchStudent
// - showScoresBtn -> showScores
// - addRandomScoreBtn -> addRandomScore
// - showSumBtn -> showSum
// - showAverageBtn -> showAverage
// - checkFailingBtn -> checkFailing



// ============================
// 8. Kjør start-funksjoner når siden lastes
// ============================

// TODO: når skriptet lastes:
// - kall showStudents()
// - kall showScores()
// - fyll inn intro-tekst, positiv tekst og footer-tekst
```
