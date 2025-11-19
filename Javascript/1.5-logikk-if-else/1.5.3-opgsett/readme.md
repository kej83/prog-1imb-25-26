## Oppgave 1: 💡 Lommetyv-alarm (Lett)

**Fokus:** Bruk av `Math.random()` og én logisk operator (**`&&`**).

### HTML og JavaScript (Må fylles ut)

```html
<!DOCTYPE html>
<html lang="no">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Oppgave 1: Lommetyv-alarm</title>
</head>
<body>
    <h1>Lommetyv-alarm</h1>
    <p>Trykk på knappen for å simulere sensoravlesninger og sjekke om alarmen går av.</p>
    <p>Alarmen skal utløses **HVIS** Bevegelse er større enn 0.5 **OG** Lys er mindre enn 0.3.</p>
    
    <button onclick="sjekkAlarm()">Simuler Sjekk</button>
    
    <h3>Sensorverdier (0.00 til 1.00):</h3>
    <p id="verdier">Lys: - | Bevegelse: -</p>
    
    <h3>Alarmstatus:</h3>
    <p id="status">Ventet på sjekk...</p>

    <script>
        function sjekkAlarm() {
            // 1. ELEV OPPGAVE: Generer tilfeldige verdier mellom 0 og 1 for lys og bevegelse (Math.random())
            let lys; 
            let bevegelse;
            
            let verdiUt = document.getElementById("verdier");
            let statusUt = document.getElementById("status");

            // ELEV OPPGAVE: Vis de genererte verdiene her (juster hvis du endrer variabelnavn)
            // verdiUt.textContent = `Lys: ${lys.toFixed(2)} | Bevegelse: ${bevegelse.toFixed(2)}`;

            // 2. ELEV OPPGAVE: SKRIV LOGIKKEN HER!
            // Bruk IF-setning og den logiske operatoren && (AND).
        }
    </script>
</body>
</html>
```

-----

## Oppgave 2: 🏷️ Pakketilbud (Medium)

**Fokus:** Bruk av **input** og kombinasjon av de logiske operatorene **`&&`** og **`||`** i ett komplekst uttrykk.

### HTML og JavaScript (Må fylles ut)

```html
<!DOCTYPE html>
<html lang="no">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Oppgave 2: Pakketilbud</title>
</head>
<body>
    <h1>Sjekk for spesialtilbud</h1>
    <p>Kunden får tilbud hvis ett av disse hovedkriteriene er sanne:</p>
    <ul>
        <li>**Kriterium A:** Totalbeløp er over 1000 kr **OG** kunden er medlem.</li>
        <li>**Kriterium B:** Kunden er ny kunde **ELLER** kunden har brukt en rabattkode.</li>
    </ul>

    <label for="inpBelop">Totalbeløp (kr):</label>
    <input type="number" id="inpBelop" value="0"><br><br>

    <input type="checkbox" id="chkMedlem">
    <label for="chkMedlem"> Er medlem/registrert</label><br>

    <input type="checkbox" id="chkNyKunde">
    <label for="chkNyKunde"> Er ny kunde</label><br>

    <input type="checkbox" id="chkRabattkode">
    <label for="chkRabattkode"> Rabattkode brukt</label><br><br>

    <button onclick="sjekkTilbud()">Sjekk Tilbud</button>
    <p id="resultat">Fyll inn verdier og sjekk!</p>

    <script>
        function sjekkTilbud() {
            // 1. Les inn input
            let belop = Number(document.getElementById("inpBelop").value);
            let erMedlem = document.getElementById("chkMedlem").checked;
            let erNyKunde = document.getElementById("chkNyKunde").checked;
            let harRabattkode = document.getElementById("chkRabattkode").checked;
            
            let ut = document.getElementById("resultat");
            
            // 2. ELEV OPPGAVE: SKRIV LOGIKKEN HER!
            // Bruk IF-setning, parenteser, && og || for å sjekke om kunden kvalifiserer for tilbudet basert på reglene ovenfor.
            // Strukturen skal være: if ( (Kriterium A) || (Kriterium B) )
        }
    </script>
</body>
</html>
```

-----

## Oppgave 3: ✈️ Reiseklarering (Vanskelig)

**Fokus:** Bruk av **input**, **`&&`**, **`||`** og **`else if`** for å håndtere flere logiske nivåer.

### HTML og JavaScript (Må fylles ut)

```html
<!DOCTYPE html>
<html lang="no">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Oppgave 3: Reiseklarering</title>
</head>
<body>
    <h1>Sjekk for Reiseklarering</h1>
    <h3>Krav for klarering:</h3>
    <ul>
        <li>**Rød Sone (Strengest):** Klarering krever at personen er **over 25 år** **OG** har **gyldig visum**.</li>
        <li>**Gul Sone (Medium):** Klarering krever at personen (**over 18 år** **OG** **gyldig visum**) **ELLER** at personen er (**under 18 år** **OG** **gyldig visum**).</li>
        <li>**Grønn Sone (Enklest):** Klarering krever at personen er **over 16 år** **ELLER** har **gyldig visum**.</li>
    </ul>

    <label for="inpAlder">Alder:</label>
    <input type="number" id="inpAlder" value="18"><br><br>

    <label for="selSone">Velg Reisemålssone:</label>
    <select id="selSone">
        <option value="Grønn">Grønn Sone (Lett)</option>
        <option value="Gul">Gul Sone (Medium)</option>
        <option value="Rød">Rød Sone (Streng)</option>
    </select><br><br>

    <input type="checkbox" id="chkVisa">
    <label for="chkVisa"> Har gyldig visum</label><br><br>

    <button onclick="sjekkKlarering()">Klarer for reise</button>
    <p id="resultat">Velg sone og fyll inn informasjon.</p>

    <script>
        function sjekkKlarering() {
            // 1. Les inn input
            let alder = Number(document.getElementById("inpAlder").value);
            let sone = document.getElementById("selSone").value;
            let harVisa = document.getElementById("chkVisa").checked;
            
            let ut = document.getElementById("resultat");
            
            // 2. ELEV OPPGAVE: SKRIV LOGIKKEN HER!
            // Bruk IF og ELSE IF-strukturen for å sjekke de tre sonene i tur og orden.
            // Implementer reglene definert i oppgaveteksten ved hjelp av && og ||.
        }
    </script>
</body>
</html>