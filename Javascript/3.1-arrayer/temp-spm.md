15 spørsmål som tester forståelse av **HTML + JavaScript** i handleliste-appen:

1. Hva er hensikten med `script`-taggen nederst i `index.html` (`<script src="script.js"></script>`)?

2. Hvorfor er det lurt at script-taggen ligger helt nederst i `<body>` i dette prosjektet?

3. Hvilke HTML-elementer må finnes i `index.html` for at denne linjen skal fungere?

```js
let inpVare = document.getElementById("inpVare");
```

4. Hva betyr det at vi bruker `id="ulVarer"` i HTML, og hva brukes det til i JavaScript?

5. Forklar hva `varer`-arrayen inneholder helt i starten av programmet.

6. Hva skjer i programmet når `visHandleliste()` blir kalt første gang (på slutten av scriptet)?

7. Hvorfor har vi disse to linjene inni `visHandleliste()`?

```js
ulVarer.innerHTML = "";
spanAntall.textContent = varer.length;
```

8. Hva er forskjellen på `innerHTML` og `textContent` i dette prosjektet? (Gi et eksempel fra koden.)

9. Hva gjør denne løkka, og hva vil den skrive ut hvis `varer = ["Melk", "Brød"]`?

```js
for (let vare of varer) {
  ulVarer.innerHTML += `<li>${vare}</li>`;
}
```

10. Når du klikker på knappen “Legg til vare”, hvilke 3 steg skjer i JavaScript-koden? (Hint: input → array → skjerm)

11. Hva gjør `varer.push(nyVare)` med arrayen? Hvor legger den den nye varen?

12. Hva gjør `varer.pop()`? Hva skjer hvis arrayen inneholder `["Melk", "Brød", "Egg"]` før du trykker knappen?

13. Hva gjør `varer.indexOf(vareSomSkalBort)`? Hva blir resultatet hvis varen ikke finnes i arrayen?

14. Forklar hvorfor vi sjekker:

```js
if (index !== -1) { ... }
```

Hva kan gå galt hvis vi ikke sjekker dette og bare kjører `splice` uansett?

15. Forklar nøyaktig hva denne linjen gjør:

```js
varer.splice(index, 1);
```

Hva betyr `1` her?
