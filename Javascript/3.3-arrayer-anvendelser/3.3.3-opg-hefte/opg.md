# JavaScript og DOM
## Arbeidshefte – `createElement` og løkker

| Navn | Klasse |
|------|--------|
|      |        |

Dette heftet inneholder tre deler:
- **Del 1 – Avskrift og endringer:** Du skriver av kode og gjør endringer
- **Del 2 – Fullfør koden:** Kodestrukturen er gitt, du fyller inn resten
- **Del 3 – Selvstendig koding:** Du lager nettsidene fra bunnen av

> Du trenger: en teksteditor (f.eks. VS Code) og en nettleser.

---

## Del 1 – Avskrift og endringer

I denne delen skriver du av koden nøyaktig slik den er vist. Kjør nettsiden i nettleseren og sjekk at det fungerer. Deretter gjør du endringene som er beskrevet under.

---

### Oppgave 1.1 – Enkel nettside

Lag en ny fil som heter `nettside.html` og skriv av denne koden:

```html
<!DOCTYPE html>
<html lang="no">
<head>
    <meta charset="UTF-8">
    <title>Min nettside</title>
</head>
<body>
    <h1>Enkel nettside</h1>
    <div id="innhold"></div>

    <script>
        let innhold = document.getElementById("innhold");

        // Lager en h2
        let overskrift = document.createElement("h2");
        overskrift.textContent = "Overskrift h2";
        innhold.appendChild(overskrift);

        // Lager en p
        let tekst = document.createElement("p");
        tekst.textContent = "Kong Harald";
        innhold.appendChild(tekst);

        // Lager et bilde
        let bilde = document.createElement("img");
        bilde.src = "https://picsum.photos/200";
        innhold.appendChild(bilde);
    </script>
</body>
</html>
```

✏️ **Gjør disse tre endringene:**
1. Bytt ut teksten i `p`-elementet fra `"Kong Harald"` til ditt eget navn.
2. Legg til en ny `p` under bildet med teksten `"Mitt favorittfag er: "` + ditt favorittfag.
3. Endre bildet til å vise 300×200 piksler i stedet for 200×200. *(Tips: se på picsum.photos-URL-en)*

---

### Oppgave 1.2 – Liste med byer

Lag en ny fil som heter `byliste.html` og skriv av koden:

```html
<!DOCTYPE html>
<html lang="no">
<head>
    <meta charset="UTF-8">
    <title>Byliste</title>
</head>
<body>
    <h1>Legge til liste</h1>
    <div id="innhold"></div>

    <script>
        let innhold = document.getElementById("innhold");

        let liste = document.createElement("ul");
        let listepunkt1 = document.createElement("li");
        let listepunkt2 = document.createElement("li");

        listepunkt1.textContent = "Oslo";
        listepunkt2.textContent = "Bergen";

        liste.appendChild(listepunkt1);
        liste.appendChild(listepunkt2);

        innhold.appendChild(liste);
    </script>
</body>
</html>
```

✏️ **Gjør disse tre endringene:**
1. Legg til tre nye byer i listen: Trondheim, Stavanger og Tromsø.
2. Endre listen fra `ul` (uordnet) til `ol` (ordnet/nummerert). Hva skjer?
3. Legg til en `h2` over listen med teksten `"Norske byer"`.

---

### Oppgave 1.3 – Løkke med tekst

Lag en ny fil som heter `loekke.html` og skriv av koden:

```html
<!DOCTYPE html>
<html lang="no">
<head>
    <meta charset="UTF-8">
    <title>Løkke med tekst</title>
</head>
<body id="kropp">
    <script>
        let kropp = document.getElementById("kropp");

        for (let i = 0; i < 100; i++) {
            let p = document.createElement("p");
            p.textContent = "Jeg elsker JavaScript! 🎉";
            kropp.appendChild(p);
        }
    </script>
</body>
</html>
```

✏️ **Gjør disse tre endringene:**
1. Endre løkken slik at den lager 50 avsnitt i stedet for 100.
2. Bruk løkkevariabelen `i` til å vise nummeret i teksten, f.eks. `"Linje 1"`, `"Linje 2"`, osv. *(Tips: `p.textContent = "Linje " + i`)*
3. Bruk en `if-else` inne i løkken: hvis `i` er et partall (`i % 2 === 0`), skriv `"Partall: " + i`, ellers skriv `"Oddetall: " + i`.

---

### Oppgave 1.4 – Løkke med bilder

Lag en ny fil som heter `bilder.html` og skriv av koden:

```html
<!DOCTYPE html>
<html lang="no">
<head>
    <meta charset="UTF-8">
    <title>Bildeløkke</title>
</head>
<body id="kropp">
    <script>
        let kropp = document.getElementById("kropp");

        for (let i = 0; i < 20; i++) {
            let bilde = document.createElement("img");
            bilde.src = "https://picsum.photos/seed/" + i + "/200/200";
            bilde.style.margin = "5px";
            kropp.appendChild(bilde);
        }
    </script>
</body>
</html>
```

> 💡 **Tips – Slik får du ulike bilder fra picsum.photos:**  
> Nettadressen `https://picsum.photos/seed/7/200/200` gir alltid det samme bildet for seed-verdien `7`.  
> Når du bruker `i` fra løkken som seed, får du 20 forskjellige bilder!

✏️ **Gjør disse tre endringene:**
1. Endre størrelsen på bildene til 150×150 piksler.
2. Vis 30 bilder i stedet for 20.
3. Legg til en `h1` øverst på siden (uten JavaScript) med teksten `"Bildegalleri"`.

---

## Del 2 – Fullfør koden

Her er kodestrukturen gitt, men du må fylle inn det som mangler. Skriv inn riktig kode på de merkede stedene.

---

### Oppgave 2.1 – Knapp som legger til tekst

Lag en nettside der brukeren klikker på en knapp, og da legges det til en ny linje med tekst på siden.

```html
<!DOCTYPE html>
<html lang="no">
<head>
    <meta charset="UTF-8">
    <title>Klikk meg</title>
</head>
<body>
    <h1>Klikk for å legge til tekst</h1>
    <button onclick="leggTilTekst()">Klikk meg!</button>
    <div id="innhold"></div>

    <script>
        function leggTilTekst() {
            let innhold = document.getElementById("innhold");
            _______________________________________
            nyTekst.textContent = "Du klikket! 🎉";
            _______________________________________
        }
    </script>
</body>
</html>
```

📝 **Hva skal du fylle inn?**
- **Linje 1:** Lag et nytt `p`-element og lagre det i variabelen `nyTekst`.
- **Linje 2:** Legg til `nyTekst` inne i `innhold`.

---

### Oppgave 2.2 – Teller med knapp

Lag en teller som øker med 1 hver gang brukeren klikker på en knapp.

```html
<!DOCTYPE html>
<html lang="no">
<head>
    <meta charset="UTF-8">
    <title>Teller</title>
</head>
<body>
    <h1>Klikkteller</h1>
    <p id="visning">Antall klikk: 0</p>
    <button onclick="telOpp()">Klikk!</button>

    <script>
        _______________________________________

        function telOpp() {
            _______________________________________
            let visning = document.getElementById("visning");
            _______________________________________
        }
    </script>
</body>
</html>
```

📝 **Hva skal du fylle inn?**
- **Linje 1:** Lag en variabel `antall` og sett den til `0`. *(Husk: utenfor funksjonen!)*
- **Linje 2:** Øk `antall` med 1.
- **Linje 3:** Oppdater teksten i `visning`-elementet til å vise det nye antallet.

---

### Oppgave 2.3 – Input og hilsen

Brukeren skriver inn navnet sitt, og siden sier hei med `if-else`: hyggelig hilsen hvis kortnavn, litt annen melding ellers.

```html
<!DOCTYPE html>
<html lang="no">
<head>
    <meta charset="UTF-8">
    <title>Hilsen</title>
</head>
<body>
    <h1>Skriv inn navnet ditt</h1>
    <input type="text" id="navnFelt" placeholder="Navn her...">
    <button onclick="siHei()">Si hei!</button>
    <p id="melding"></p>

    <script>
        function siHei() {
            let navnFelt = document.getElementById("navnFelt");
            _______________________________________
            let melding = document.getElementById("melding");

            _______________________________________
                melding.textContent = "Hei, " + navn + "! Kort og godt navn! 😄";
            } else {
                _______________________________________
            }
        }
    </script>
</body>
</html>
```

📝 **Hva skal du fylle inn?**
- **Linje 1:** Hent verdien fra input-feltet og lagre det i variabelen `navn`.
- **Linje 2:** Skriv `if`-setningen som sjekker om navnet er 4 tegn eller kortere.
- **Linje 3:** Skriv `textContent`-linjen i `else`-blokken.

---

### Oppgave 2.4 – Bildeløkke med størrelsesvalg

Brukeren velger antall bilder via en input, klikker en knapp, og løkken lager riktig antall bilder.

```html
<!DOCTYPE html>
<html lang="no">
<head>
    <meta charset="UTF-8">
    <title>Velg antall bilder</title>
</head>
<body>
    <h1>Bildegalleri</h1>
    <input type="number" id="antallFelt" value="5" min="1" max="50">
    <button onclick="lagBilder()">Vis bilder</button>
    <div id="galleri"></div>

    <script>
        function lagBilder() {
            let galleri = document.getElementById("galleri");
            galleri.innerHTML = "";

            let antallFelt = document.getElementById("antallFelt");
            _______________________________________

            _______________________________________
                let bilde = document.createElement("img");
                bilde.src = "https://picsum.photos/seed/" + i + "/150/150";
                bilde.style.margin = "5px";
                _______________________________________
            }
        }
    </script>
</body>
</html>
```

📝 **Hva skal du fylle inn?**
- **Linje 1:** Hent verdien fra input-feltet, konverter til tall med `Number(...)`, og lagre i `antall`.
- **Linje 2:** Skriv `for`-løkken som kjører `antall` ganger.
- **Linje 3:** Legg til bildet i `galleri`.

---

## Del 3 – Selvstendig koding

Nå lager du alt fra bunnen! Ingen kode er gitt – bare oppgaveteksten. Bruk det du har lært om `createElement`, løkker, variabler, `if-else`, input og button.

---

### Oppgave 3.1 – Gjettelek

**Oppgave:**  
Lag en nettside med et tall-inputfelt og en "Gjett"-knapp. Programmet velger ett hemmelig tall mellom 1 og 10 (du kan hardkode det, f.eks. `let hemmeligTall = 7`).

Når brukeren klikker, skal det vises en melding:
- Riktig svar → `"Riktig! Gratulerer! 🎉"`
- For lavt → `"For lavt, prøv igjen!"`
- For høyt → `"For høyt, prøv igjen!"`

Meldingen skal vises i et `p`-element som du har laget med `createElement`.

> 💡 **Tips:** Bruk `Number()` til å konvertere inputverdien til tall.

---

### Oppgave 3.2 – Meldingsveggen

**Oppgave:**  
Lag en nettside med:
- Et tekstfelt (`input type="text"`) der brukeren skriver en melding
- En "Legg til"-knapp
- Et område der meldingene vises som en liste (`li`-elementer inni en `ul`)

Hver gang brukeren klikker knappen, legges meldingen til som et nytt listepunkt. Meldingsfeltet skal tømmes etter at meldingen er lagt til.

> ⭐ **Ekstra utfordring:** Hvis meldingsfeltet er tomt, vis en advarsel (`if-else`).

---

### Oppgave 3.3 – Multiplikasjonstabellen

**Oppgave:**  
Lag en nettside der brukeren skriver inn et tall og klikker "Vis tabell". Da skal multiplikasjonstabellen for det tallet vises fra 1 til 10.

**Eksempel:** Brukeren skriver `6` og klikker. Da vises:
- 6 × 1 = 6
- 6 × 2 = 12
- 6 × 3 = 18
- ... og så videre til 6 × 10 = 60

Hvert regnestykke skal vises i et eget `p`-element laget med `createElement` og en `for`-løkke.

---

## ⭐ Ekstraoppgave 3.4 – Quizmaskin ⭐

**Oppgave – Quizmaskin med array:**  
Lag en quizmaskin som stiller spørsmål fra en liste (array). Nettsiden skal:
- Lagre minst 5 spørsmål i et array, hvert spørsmål er et objekt med to felt: spørsmålstekst og riktig svar
- Vise ett spørsmål om gangen med et input-felt og en "Svar"-knapp
- Gi tilbakemelding: riktig/feil, og vis riktig svar hvis feil
- Vise en "Neste spørsmål"-knapp etter svaret
- Vise poengsummen løpende, f.eks. `"3 av 5 riktige"`
- Vise en avslutningsmelding med total poengsum når alle spørsmål er besvart

Slik kan arrayet se ut:

```javascript
let quiz = [
    { sporsmal: "Hva er hovedstaden i Norge?",        svar: "Oslo"                    },
    { sporsmal: "Hva er 7 × 8?",                      svar: "56"                      },
    { sporsmal: "Hvilken planet er størst?",           svar: "Jupiter"                 },
    { sporsmal: "Hva er HTML en forkortelse for?",     svar: "HyperText Markup Language" },
    { sporsmal: "Hvem skreiv Romeo og Julie?",         svar: "Shakespeare"             }
];
```

**Tips og råd:**
- Bruk en variabel som holder styr på hvilket spørsmål vi er på (indeks)
- Bruk en variabel for poengsum
- Sammenlign svaret med `.toLowerCase()` så store/små bokstaver ikke spiller rolle
- Bruk `innerHTML = ""` for å tømme visningsområdet mellom spørsmålene
- Lag en egen funksjon for å vise neste spørsmål

> ⭐ **Ekstra utfordring:** Bland rekkefølgen på spørsmålene med `array.sort(() => Math.random() - 0.5)`