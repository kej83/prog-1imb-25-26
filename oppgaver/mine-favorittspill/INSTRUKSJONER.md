# 📋 Oppgavebeskrivelse – Favorittspill-nettside

---

## 🎯 Læringsmål

Etter å ha fullført oppgaven skal du kunne:

- Bruke **arrays** til å lagre og hente data
- Bruke **DOM-manipulasjon** (`getElementById`, `innerHTML`, `textContent`)
- Bruke **løkker** (`forEach`) til å gå gjennom en liste
- Bruke **betingelser** (`if/else`) for å sjekke input
- Bruke innebygde array-metoder: `.push()`, `.splice()`, `.filter()`, `.sort()`, `.includes()`, `.indexOf()`
- Skrive **funksjoner** som løser ett avgrenset problem

---

## 📁 Filstruktur

Du har fått tre filer:

```
favorittspill/
├── index.html   ← ferdig, IKKE endre
├── style.css    ← ferdig, IKKE endre
└── spill.js     ← HER skal du kode!
```

---

## 📌 Regler

1. **Endre kun `spill.js`** – HTML og CSS er ferdig.
2. Ikke endre variabelnavn eller funksjonsnavn.
3. Fyll inn kode der det står `// TODO:`.
4. Test i nettleseren etter hvert steg (åpne `index.html` i Chrome/Firefox).
5. Bruk **F12 → Konsoll** hvis noe ikke fungerer.

---

## 🗂️ Funksjoner du skal fylle inn

| # | Funksjon | Beskrivelse |
|---|----------|-------------|
| 1 | `visAllSpill()` | Viser alle spill i listen |
| 2 | `leggTilSpill()` | Legger til et nytt spill fra inputfeltet |
| 3 | `fjernSpill(navn)` | Fjerner ett spill fra listen |
| 4 | `sokEtterSpill()` | Filtrerer listen mens brukeren skriver |
| 5 | `nullstillSok()` | Tømmer søket og viser alle spill |
| 6 | `sorterListe()` | Sorterer listen alfabetisk (A–Å / Z–A) |
| 7 | `oppdaterStatistikk()` | Oppdaterer statistikk-boksene |
| 8 | `settArstall()` | ⭐ Bonus – viser inneværende år i footeren |

---

## 💡 Nyttige tips

### Hente tekst fra et input-felt:
```javascript
let tekst = document.getElementById("mitt-felt").value.trim();
```

### Legge til i et array:
```javascript
minListe.push("nytt element");
```

### Fjerne ett element på en bestemt plass:
```javascript
minListe.splice(indeks, 1);
```

### Filtrere et array:
```javascript
let resultat = minListe.filter(function(element) {
  return element.includes(sokeord);
});
```

### Sortere et array:
```javascript
minListe.sort(); // A–Å
minListe.reverse(); // Z–A
```

### Vise/skjule feil- og suksessmeldinger:
```javascript
tilbakemeldingEl.textContent = "Spillet ble lagt til!";
tilbakemeldingEl.classList.add("ok");
tilbakemeldingEl.classList.remove("feil");
```

---

## ✅ Egenvurdering

Når du er ferdig, svar på disse spørsmålene i en kommentar øverst i `spill.js`:

1. Hvilken funksjon var vanskeligst? 
2. Hva ville du ha endret på nettsiden hvis du fikk velge?
3. Hva er forskjellen på `.filter()` og `.splice()`?

---

## 🏆 Bonusutfordringer

Prøv disse hvis du blir ferdig tidlig:

- **B1:** Legg til en "Tøm hele listen"-knapp (med bekreftelse).
- **B2:** La brukeren redigere et spillnavn ved å dobbeltklikke på det.
- **B3:** Lagre spill-listen i `localStorage` slik at den huskes etter siden lastes inn på nytt.
- **B4:** Legg til en stjerne (⭐) ved siden av favorittspilet (la brukeren velge).
