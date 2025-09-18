# Prøve i HTML og CSS – Løsningsforslag
**Vurdering:**

* Del 1 – Flervalgsoppgaver (20 spm × 1 p) = **20 p**
* Del 2 – Fyll inn manglende kode (7 oppg × 5 p) = **35 p**
* Del 3 – Frie kodeoppgaver (3 oppg × 15 p) = **45 p**

**Sum:** 100 p

## Instruks - egenvurdering:
Gi deg selv poeng. Lever rettet prøve til læreren.

## Del 1 – Multiple Choice

1. B `<h1>`
2. B `<p>`
3. B `<ol>`
4. A `<li>`
5. C `src`
6. C `<tr>`
7. A `<td>`
8. D `<th>`
9. A `<figure>` og `<figcaption>`
10. C `p`
11. C `#bigText`
12. A `.blue`
13. C `color: red;`
14. B `font-size`
15. B (link + `font-family: 'Inter', sans-serif;`)
16. C Avstand **utenfor** boksen
17. A Avstand **inni** boksen
18. B `border`
19. A `text-align: center;`
20. C `margin: 0 auto;`

---

## Del 2 – Fyll inn manglende kode

**Oppgave 1**

```html
<h1>Velkommen til kurset</h1>
<p>Dette er første avsnitt.</p>
<p>Dette er andre avsnitt.</p>
```

**Oppgave 2**

```html
<li>CSS</li>
<li>JavaScript</li>
```

**Oppgave 3**

```html
<img src="logo.png" alt="Skolelogo">
```

**Oppgave 4**

```css
#warning {
  color: red;
}
```

**Oppgave 5**

```css
.blue {
  color: blue;
  font-weight: 600;
}
```

**Oppgave 6**

```html
<link href="https://fonts.googleapis.com/css2?family=Inter&display=swap" rel="stylesheet">
```

```css
font-family: 'Inter', sans-serif;
```

**Oppgave 7**

```html
<th>Navn</th>
<th>Alder</th>
<td>Ada</td>
<td>18</td>
```

---

## Del 3 – Frie kodeoppgaver

**Oppgave 8: Kort med bilde og bildetekst**

```html
<figure>
  <img src="cat.jpg" alt="Kurskatt">
  <figcaption>Kurskatt</figcaption>
</figure>

<style>
figure img {
  border: 2px solid gray;
  padding: 10px;
  margin: 12px;
}
figcaption {
  text-align: center;
}
</style>
```

**Oppgave 9: Sentralisert innholdsboks**

```html
<div class="boks">
  <h2>Tittel</h2>
  <p>Dette er litt tekst inni boksen.</p>
</div>

<style>
.boks {
  width: 400px;
  margin: 24px auto 0 auto;
  padding: 16px;
  border: 1px solid black;
  background-color: #f5f5f5;
}
</style>
```

**Oppgave 10: Tabell med overskrifter og kantlinjer**

```html
<table>
  <tr>
    <th>Navn</th>
    <th>Fag</th>
    <th>Karakter</th>
  </tr>
  <tr>
    <td>Ada</td>
    <td>Matematikk</td>
    <td>5</td>
  </tr>
  <tr>
    <td>Bjørn</td>
    <td>Naturfag</td>
    <td>4</td>
  </tr>
  <tr>
    <td>Clara</td>
    <td>Historie</td>
    <td>3</td>
  </tr>
</table>

<style>
table {
  width: 100%;
  border-collapse: collapse;
}
th, td {
  border: 1px solid black;
  padding: 8px;
}
th {
  text-align: center;
}
</style>
```
