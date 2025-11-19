# 🧠 Prøve MED LØSNING – HTML & JavaScript
*(variabler, random, if/else, button, input)*

## POENG:
* 1p per riktig svar på del 1
* 2p per riktig svar på del 2
* 5p for riktig svar på del 3


---

# 🧩 Del 1 – Flervalg (med løsninger og forklaringer)

1. Hva gjør `Math.random()`?

   * A) Tilfeldig heltall 1–10
   * ✅ B) Tilfeldig tall 0–1 (1 ikke med)
   * C) Alltid 0 eller 1
   * D) Tilfeldig tall 1–6
     **Forklaring:** `Math.random()` gir et desimaltall mellom 0 (inkludert) og 1 (ikke inkludert).

---

2. Hvilken kode gir et heltall mellom 1 og 6?

   * A) `Math.floor(Math.random()*6)`
   * B) `Math.ceil(Math.random()*6)`
   * ✅ C) `Math.floor(Math.random()*6)+1`
   * D) `Math.round(Math.random()*6)+1`
     **Forklaring:** `Math.floor()` runder ned. Ved å legge til `+1` får du tall 1–6.

---

3. Hvordan leser du tallet fra `<input id="alder" type="number">`?

   * A) `document.querySelector("#alder").textContent`
   * ✅ B) `Number(document.getElementById("alder").value)`
   * C) `document.getElementById("alder").innerHTML`
   * D) `Number(document.querySelector("alder").value)`
     **Forklaring:** Bruk `.value` for å hente verdien fra et input-felt og `Number()` for å gjøre det om til tall.

---

4. Hva gjør `document.querySelector("h2")`?

   * A) Lager et nytt h2-element
   * ✅ B) Finner første `<h2>`
   * C) Finner alle `<h2>`
   * D) Fjerner `<h2>`
     **Forklaring:** `querySelector()` finner **første** element som passer CSS-selektoren.

---

5. Hvilken egenskap skriver tekst ut i et element?

   * A) `value`
   * B) `innerStyle`
   * ✅ C) `textContent`
   * D) `nodeValue`
     **Forklaring:** `textContent` endrer teksten som vises på nettsiden.

---

6. Hvilken kode knytter en knapp til en funksjon?

   * A) `<button run="min()">Klikk</button>`
   * B) `<button call="min()">Klikk</button>`
   * ✅ C) `<button onclick="min()">Klikk</button>`
   * D) `<button onpress="min()">Klikk</button>`
     **Forklaring:** `onclick` brukes for å kjøre funksjonen når knappen trykkes.

---

7. Hvilken linje oppretter en variabel som kan endres?

   * ✅ A) `let poeng = 0;`
   * B) `const poeng;`
   * C) `var poeng? 0;`
   * D) `int poeng = 0;`
     **Forklaring:** `let` brukes for variabler som kan endres i JavaScript.

---

8. Hva blir resultatet av denne koden?

   ```js
   let x = 5;
   if (x > 7) { x = 10; } else { x = 2; }
   ```

   * A) 5
   * B) 7
   * C) 10
   * ✅ D) 2
     **Forklaring:** `x` er ikke større enn 7, så else-delen kjører.

---

9. Hvilken strengsyntaks gjør det lett å sette inn variabler?

   * A) `'Hei ' + navn`
   * B) `"Hei " + navn`
   * ✅ C) `` `Hei ${navn}` ``
   * D) `!Hei {navn}`
     **Forklaring:** Backticks (`` ` ``) gjør det mulig å bruke `${}` for variabler i tekst.

---

10. Hva gjør `Number("42")`?

* A) Lager teksten `"42"`
* B) Kaster feil
* ✅ C) Gjør teksten om til tallet `42`
* D) Gjør tallet om til tekst
  **Forklaring:** `Number()` konverterer tekst til tall når mulig.

---

11. Hva er best for å bytte tekst i en `<p id="ut">`?

* A) `...innerHTML = txt;`
* ✅ B) `...textContent = txt;`
* C) `...text = txt;`
* D) `...value = txt;`
  **Forklaring:** `textContent` brukes til å endre tekst, mens `value` brukes for input-felt.

---

12. Hvilken sammenligning sjekker om to verdier er like?

* A) `=`
* ✅ B) `==`
* C) `===!`
* D) `=>`
  **Forklaring:** `==` sammenligner verdier uten å tilordne.

---

13. Hva gjør denne koden?

```html
<button onclick="spill()">Start</button>
```

* A) Kaller `spill` når siden lastes
* ✅ B) Kaller `spill` når man klikker knappen
* C) Definerer `spill`
* D) Fjerner knappen
  **Forklaring:** `onclick` kjører funksjonen når man trykker på knappen.

---

14. Hvilken rekkefølge er riktig for å lese et tall og vise dobbel verdi?

* ✅ A) Les → Gang → Vis
* B) Vis → Les → Gang
* C) Gang → Vis → Les
* D) Les → Vis → Gang
  **Forklaring:** Først leser du input, regner ut, og viser resultatet.

---

15. Hvilken linje gir et tilfeldig 0 eller 1?

* ✅ A) `Math.round(Math.random())`
* B) `Math.floor(Math.random())`
* C) `Math.ceil(Math.random())`
* D) `Math.random()*1`
  **Forklaring:** `Math.round()` runder 0–0.49 til 0 og 0.5–0.99 til 1.

---

16. Hva mangler i denne koden?

```js
function start() {
  let navn = _____("inpNavn").value;
}
```

* A) `querySelector`
* ✅ B) `document.getElementById`
* C) `getElementByName`
* D) `find`
  **Forklaring:** Du må bruke `document.getElementById("inpNavn")` for å hente feltet.

---

17. Hvilken betingelse er sann når `poeng` er mellom 50 og 100 (inkludert)?

* A) `poeng > 50 && poeng < 100`
* ✅ B) `poeng >= 50 && poeng <= 100`
* C) `poeng >= 50 || poeng <= 100`
* D) `poeng > 50 || poeng < 100`
  **Forklaring:** `>=` og `<=` inkluderer grensene 50 og 100.

---

18. Hvor skal JavaScript-koden stå i denne prøven?

* A) I `<head>`
* B) I ekstern `.js`-fil
* ✅ C) I `<script>` nederst i `<body>`
* D) I `<style>`
  **Forklaring:** Da lastes HTML først, så fungerer koden på elementene.

---

19. Hvilken id-selektor er riktig i `querySelector`?

* ✅ A) `querySelector("#resultat")`
* B) `querySelector(".resultat")`
* C) `querySelector("resultat")`
* D) `querySelector("$resultat")`
  **Forklaring:** `#` brukes for å velge elementer med bestemt id.

---

20. Hva gjør denne koden?

```js
let kast = Math.ceil(Math.random()*6);
if (kast === 6) { txt = "Hurra!"; }
```

* A) Skriver ut 6
* B) Setter `kast` til 0–5
* ✅ C) Lager et terningkast 1–6 og jubler ved 6
* D) Alltid “Hurra!”
  **Forklaring:** `Math.ceil()` gir tall fra 1–6, og if-setningen sjekker om tallet er 6.

---

# 🧠 Del 2 – Fyll inn manglende kode (med løsning)

### 2.1 Summer to tall

```js
let s = x + y;
document.getElementById("ut1").textContent = s;
```

**Forklaring:** Summer tallene og skriv resultatet i `<p>`.

---

### 2.2 Mynt (kron/mynt)

```js
if (t === 1) { txt = "mynt"; }
```

**Forklaring:** Hvis `t` er 1, bytter vi fra “kron” til “mynt”.

---

### 2.3 Eldre enn 18?

```js
if (a < 18) { txt = "Du er ikke myndig"; }
```

**Forklaring:** Bruk if-setning for å endre teksten ved lav alder.

---

### 2.4 Terning med spesialmelding

```js
let k = Math.ceil(Math.random()*6);
if (k === 1) { txt = "Uflaks!"; }
```

**Forklaring:** `Math.ceil` gir tall 1–6, og 1 gir spesialmelding.

---

### 2.5 Rabatt i prosent

```js
let rKr = p * r / 100;
let ny = p - rKr;
```

**Forklaring:** Beregn rabatt i kroner og trekk den fra prisen.

---

# 💻 Del 3 – Gjettespill 1–10 (løsning)

```html
<h2>Gjettespill</h2>
<input id="g" type="number" min="1" max="10" placeholder="1–10">
<button onclick="spill()">Gjett</button>
<p id="resultat"></p>

<script>
function spill() {
  let gjett = Number(document.getElementById("g").value);
  let fasit = Math.floor(Math.random()*10) + 1;
  let txt = "";

  if (gjett === fasit) {
    txt = "Riktig!";
  } else if (gjett < fasit) {
    txt = "For lavt!";
  } else {
    txt = "For høyt!";
  }

  document.getElementById("resultat").textContent =
    `Du gjettet ${gjett}. Fasit var ${fasit}. ${txt}`;
}
</script>
```

**Forklaring:**
Programmet trekker et tilfeldig tall 1–10. Deretter sammenlignes brukerens gjetning med fasit, og en passende melding vises.

---

## ✏️ Svarark LØSNING – Del 1 (Flervalg)


| Nr | A | B | C | D |
| -- | - | - | - | - |
| 1  |   | ✅ |   |   |
| 2  |   |   | ✅ |   |
| 3  |   | ✅ |   |   |
| 4  |   | ✅ |   |   |
| 5  |   |   | ✅ |   |
| 6  |   |   | ✅ |   |
| 7  | ✅ |   |   |   |
| 8  |   |   |   | ✅ |
| 9  |   |   | ✅ |   |
| 10 |   |   | ✅ |   |
| 11 |   | ✅ |   |   |
| 12 |   | ✅ |   |   |
| 13 |   | ✅ |   |   |
| 14 | ✅ |   |   |   |
| 15 | ✅ |   |   |   |
| 16 |   | ✅ |   |   |
| 17 |   | ✅ |   |   |
| 18 |   |   | ✅ |   |
| 19 | ✅ |   |   |   |
| 20 |   |   | ✅ |   |
