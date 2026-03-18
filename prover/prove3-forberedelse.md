# Øvehefte – JavaScript og HTML

## Tema til prøve

* Variabler
* If-else
* Logiske uttrykk (&& og ||)
* Løkker
* Arrayer
* Funksjoner (spesielt koblet til knapper)
* Kobling til HTML (getElementById)
* Knapper og input-felt

**Viktig:** Du må kunne skrive kode for hånd og forklare hva den gjør.

---

# Del 1: Variabler 

1. Hva blir resultatet?

```js
let a = 10;
let b = 3;
let c = a % b;
console.log(c);
```

2. Hva blir skrevet ut?

```js
let x = 5;
x = x + 2;
x = x * 3;
console.log(x);
```

3. Hva er forskjellen på disse?

```js
let a = "10";
let b = 10;
```

4. Hva blir resultatet?

```js
let x = "5";
let y = 2;
console.log(x * y);
```

5. Lag et program som:

* Har to variabler
* Bytter verdiene deres

---

# Del 2: If-else 

6. Hva blir skrevet ut?

```js
let poeng = 75;
if (poeng > 90) {
  console.log("A");
} else if (poeng > 70) {
  console.log("B");
} else {
  console.log("C");
}
```

7. Lag et karakter-system:

* 90+ → A
* 80+ → B
* 60+ → C
* Ellers → D

8. Hva skjer her?

```js
let alder = 18;
if (alder >= 18) {
  if (alder == 18) {
    console.log("Akkurat voksen");
  }
}
```

9. Lag et program som sjekker:

* Om et tall er positivt, negativt eller 0

---

# Del 3: Logiske uttrykk 

10. Hva blir resultatet?

```js
true && true || false
```

11. Hva blir resultatet?

```js
false || false && true
```

12. Lag en if-setning som sjekker:

* alder > 18 OG alder < 30

13. Lag en if-setning som sjekker:

* passord er "1234" ELLER "admin"

14. Lag et program som gir rabatt hvis:

* alder < 18 ELLER alder > 67

---

# Del 4: Løkker 

15. Hva skriver denne ut?

```js
for (let i = 1; i <= 5; i++) {
  console.log(i * 2);
}
```

16. Skriv en løkke som:

* Summerer tallene fra 1 til 10

17. Hva blir resultatet?

```js
let sum = 0;
for (let i = 0; i < 5; i++) {
  sum += i;
}
console.log(sum);
```

18. Lag en løkke som teller ned fra 10 til 0

19. Lag en løkke som:

* Teller hvor mange partall det er fra 1 til 20

20. Hva er feil?

```js
for (let i = 0; i < 5; i++) {
  console.log(i);
}
console.log(i);
```

---

# Del 5: Arrayer

21. Hva blir skrevet ut?

```js
let tall = [2, 4, 6, 8];
console.log(tall[tall.length - 1]);
```

22. Lag en løkke som:

* Regner ut summen av en array

23. Lag en løkke som:

* Finner det største tallet i en array

24. Hva gjør denne?

```js
let sum = 0;
let arr = [1,2,3];
for (let i = 0; i < arr.length; i++) {
  sum += arr[i];
}
```

25. Lag et program som:

* Teller hvor mange tall som er større enn 10 i en array

---

# Del 6: Funksjoner + HTML 

26. Hva gjør denne?

```html
<button onclick="siHei()">Klikk</button>
<script>
function siHei() {
  console.log("Hei!");
}
</script>
```

27. Lag en knapp som:

* Når du klikker → viser "Velkommen"

28. Lag et program:

* Input for alder
* Knapp
* Viser "Voksen" eller "Barn"

29. Lag et program:

* Input for tall
* Knapp
* Viser om tallet er partall eller oddetall

30. Lag et program:

* To input-felt
* Knapp
* Viser summen

---

# Del 7: STØRRE OPPGAVER 

31. Lag et program:

* Input for navn
* Knapp
* Legger navn i en array
* Viser alle navnene

32. Lag et program:

* Input for tall
* Knapp
* Legger til i array
* Viser gjennomsnitt

33. Lag et program:

* Genererer tilfeldig tall 1–10
* Input fra bruker
* Sjekker riktig/feil

34. Lag et program:

* Teller hvor mange ganger knappen trykkes

35. Lag et program:

* Input for temperatur
* Viser:

  * "Kaldt" (< 10)
  * "Passe" (10–20)
  * "Varmt" (> 20)

---

# EKSTRA UTFORDRINGER

36. Lag et program som:

* Finner minste tall i en array

37. Lag et program som:

* Teller hvor mange ganger et bestemt tall finnes i en array

38. Lag et program som:

* Snur en array (baklengs)

39. Lag et program som:

* Fjerner alle tall under 5 fra en array

40. Lag et program som:

* Har input
* Legger til i array
* Viser bare partall fra arrayen

