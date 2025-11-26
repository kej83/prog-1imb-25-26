# ⭐ Oppgave: Poengbonus i spillportal

Du skal lage et lite program som beregner hvor mange **bonuspoeng** en bruker får basert på:

* Antall poeng spilleren har fra før
* Om spilleren har **VIP-status**
* Hvilken **rangering** spilleren har i spillet

Bruk HTML-filen under og koble til både `style.css` og `script.js`.

---

# 📁 Mappestruktur (må ligge i samme mappe)

```
spillbonus/
│── index.html
│── style.css
│── script.js
```

---

# 📌 Oppgaveinstruks:

1. Opprett en mappe, f.eks. **spillbonus**.
2. Lag tre filer i mappen:

   * `index.html`
   * `style.css`
   * `script.js`
3. Koble `style.css` til HTML-fila med:

```html
<link rel="stylesheet" href="style.css">
```

4. Koble JavaScript-fila slik i `<head>`:

```html
<script src="script.js" defer></script>
```

5. Elevene skal skrive all koden i **script.js** selv.

---

# 📄 index.html

```html
<!DOCTYPE html>
<html lang="no">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bonuspoeng</title>

    <!-- Koble til CSS -->
    <link rel="stylesheet" href="style.css">

    <!-- Koble til JavaScript med defer -->
    <script src="script.js" defer></script>
</head>
<body>

    <h1>Beregn bonuspoeng</h1>

    <label for="inpPoeng">Dine poeng:</label>
    <input type="number" id="inpPoeng"><br>

    <label>
        VIP-status:
        <input type="checkbox" id="chkVip">
    </label>
    <br>

    <label for="selRang">Rangering:</label>
    <select id="selRang">
        <option value="nybegynner">Nybegynner</option>
        <option value="middels">Middels</option>
        <option value="elite">Elite</option>
        <option value="mester">Mester</option>
    </select>

    <button id="btnBeregn">Beregn bonus</button>

    <p id="resultat"></p>

</body>
</html>
```

---

# 🎨 style.css

```css
body {
    font-family: Arial, sans-serif;
    max-width: 500px;
    margin: 40px auto;
    background-color: #f2f2f2;
    padding: 20px;
    border-radius: 10px;
}

label {
    display: inline-block;
    margin-top: 10px;
}

input, select {
    margin-top: 5px;
}

button {
    margin-top: 15px;
    padding: 8px 14px;
    font-size: 16px;
    cursor: pointer;
}
```

---

# 🧠 Din jobb (elevene):

Skriv koden i **script.js** slik at:

* Du henter inn:

  * poengsummen brukeren har
  * om brukeren er VIP (true/false)
  * hvilken rangering brukeren har
* VIP gir **+20% bonus**
* Rangering gir ekstra bonus:

  * *Nybegynner*: +5%
  * *Middels*: +10%
  * *Elite*: +20%
  * *Mester*: +30%
* Kalkuler:

  * totale bonuspoeng
  * ny poengsum
* Vis resultatet i `<p id="resultat">`.
