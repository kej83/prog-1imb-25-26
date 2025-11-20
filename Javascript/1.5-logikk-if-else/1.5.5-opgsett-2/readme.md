# Opg-sett 2

## 1. Brukernavn-sjekk (text)

**Input-typer:**

* `text` (brukernavn)
* knapp

**Oppgave:**
Lag et lite skjema der eleven skriver inn et brukernavn.

Regler:

* Hvis brukernavnet er kortere enn 3 tegn → vis melding: `"Brukernavnet er for kort"`.
* Hvis det inneholder mellomrom → `"Brukernavn kan ikke inneholde mellomrom"`.
* Ellers → `"Brukernavn godkjent"`.

---

## 2. Aldersgrense for spill (number)

**Input-typer:**

* `number` (alder)
* `select` (valg av spill: f.eks. PEGI 7, 12, 16, 18)
* knapp

**Oppgave:**
Bruker velger et spill i en `select` (med verdi 7, 12, 16 eller 18) og skriver inn alder i et `number`-felt.

Regler:

* Hvis alder ≥ aldersgrensa til spillet → `"Du kan spille dette spillet"`.
* Ellers → `"Du er for ung for dette spillet"`.

---

## 3. Sjekk passordstyrke (password)

**Input-typer:**

* `password` (passord)
* knapp

**Oppgave:**
Bruker skriver inn passord.

Regler (enkelt nivå):

* Hvis passord-lengde < 6 → `"Svakt passord"`.
* Hvis lengde mellom 6 og 10 → `"Ok passord"`.
* Hvis lengde > 10 → `"Sterkt passord"`.

Ekstra:

* Legg til en sjekk: hvis passordet **inneholder** tallet `"123"` → skriv `"For lett å gjette"`.

---

## 4. Nyhetsbrev og vilkår (checkbox)

**Input-typer:**

* `text` (e-post)
* `checkbox` (godtar vilkår)
* `checkbox` (vil få nyhetsbrev)
* knapp

**Oppgave:**
Bruker fyller inn e-post og huker av for:

* “Jeg godtar vilkår”
* “Jeg vil ha nyhetsbrev” (valgfritt)

Regler:

* Hvis e-post-feltet er tomt → `"Du må skrive inn e-post"`.
* Hvis vilkår **ikke** er huket av → `"Du må godta vilkår"`.
* Hvis vilkår er huket av og nyhetsbrev er huket av → `"Takk, du er meldt på nyhetsbrev"`.
* Hvis vilkår er huket av og nyhetsbrev **ikke** er huket av → `"Konto opprettet uten nyhetsbrev"`.

---

## 5. Discord-lignende rollevalg (select + checkbox)

**Input-typer:**

* `select` (rolle: "member", "mod", "admin")
* `checkbox` (har godtatt server-regler)
* knapp

**Oppgave:**
Bruker velger rolle og huker av for “Jeg har lest og godtatt reglene”.

Regler:

* Hvis ikke huket av for regler → `"Du må godta reglene for å bli med"`.
* Hvis rolle er `member` og regler er godtatt → `"Velkommen som vanlig medlem!"`.
* Hvis rolle er `mod` og regler er godtatt → `"Du får moderator-tilgang"`.
* Hvis rolle er `admin` og regler er godtatt → `"Admin-tilgang er sendt til review"` (som om noen må godkjenne det).

---

## 6. Rabatt i nettbutikk (number + checkbox + select)

**Input-typer:**

* `number` (totalpris i kr)
* `checkbox` (er student)
* `select` (medlemsnivå: "ingen", "bronse", "sølv", "gull")
* knapp

**Oppgave:**
Bruker skriver inn handlekurv-sum og velger om hen er student, samt medlemsnivå.

Regler (du kan la elevene regne rabatten i JS):

* Hvis student → 10 % rabatt.
* Hvis i tillegg `select` er:

  * bronse → +5 % rabatt
  * sølv → +10 % rabatt
  * gull → +15 % rabatt
* Hvis ikke student og medlemsnivå = "ingen" → ingen rabatt.

Vis:

* Opprinnelig pris
* Rabatt i kroner
* Sluttpris

---

## 7. “Safe mode”-innlogging (text + password + checkbox)

**Input-typer:**

* `text` (brukernavn)
* `password` (passord)
* `checkbox` (Safe mode)
* knapp

**Oppgave:**
Bruker prøver å logge inn i et fiktivt system.

Hardkod noen verdier i JS, f.eks.:

```js
const correctUser = "test";
const correctPass = "1234";
```

Regler:

* Hvis brukernavn eller passord er feil → `"Feil brukernavn eller passord"`.
* Hvis riktig innlogging og `Safe mode` er huket av → `"Logget inn i SAFE MODE (begrenset tilgang)"`.
* Hvis riktig innlogging og `Safe mode` ikke er huket av → `"Logget inn med full tilgang"`.

---

## 8. Streaming-plan velger (select + number)

**Input-typer:**

* `select` (plan: "basic", "standard", "premium")
* `number` (antall personer i husholdning)
* knapp

**Oppgave:**
Bruker velger plan og hvor mange som skal bruke kontoen.

Regler (for eksempel):

* basic: maks 1 person
* standard: maks 2 personer
* premium: maks 4 personer

Sjekk:

* Hvis antall personer > maks for valgt plan → `"For mange personer for denne planen"`.
* Ellers → `"Planen passer for husholdningen din"`.

---

## 9. Spill-tid og foreldre-godkjenning (number + checkbox + select)

**Input-typer:**

* `number` (antall timer spill per dag)
* `checkbox` (har lekser gjort)
* `select` (dag i uka: mandag–søndag)
* knapp

**Oppgave:**
Lag et “foreldre-kontroll”-skjema.

Regler:

* Hvis det er **mandag–torsdag** og lekser **ikke** er gjort → `"Du må gjøre lekser før du spiller"`.
* Hvis spilltid > 4 timer → `"For mye spilling i dag"`.
* Hvis dag er **lørdag eller søndag** og lekser er gjort → litt mer liberal melding, f.eks. `"Helg! Godkjent spilletid"` (så lenge det ikke er ekstremt).
* Kombiner `&&` og `||` på en fornuftig måte.

---

## 10. Rolle + kanal-tilgang (text + select + checkbox)

**Input-typer:**

* `text` (kanalnavn, f.eks. `#generelt`, `#staff`)
* `select` (rolle: "guest", "member", "mod", "admin")
* `checkbox` (18+)
* knapp

**Oppgave:**
Sjekk om bruker får tilgang til en kanal.

Regler (du bestemmer, f.eks.):

* Kanal `#18plus` krever at:

  * `checkbox` (18+) er huket av **og**
  * rolle er minst `member`.
* Kanal `#staff` krever at rolle er `mod` eller `admin`.
* `#generelt` er åpen for alle roller.
* Alle andre kanalnavn → `"Kanal finnes ikke"`.

Her må du kombinere:

* Sammenligning av `text`-verdi
* Rolle med `select`
* `checkbox`-verdi
* Flere `if-else if-else`-blokker.
