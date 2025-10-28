# OPPGAVE: Sett riktig HTML på en nyhetsartikkel

**Mål:** Formater innholdet under med disse elementene: `h1`, `p`, `q`, `img`, `h2`, `ul`, `ol`, `li`, `a`, `strong`.

**Regler:**

* Bruk én `h1` til tittel.
* Del brødteksten i logiske `p`.
* Bruk `q` til det korte sitatet.
* Legg inn bildet med `img` (bruk både `src` og `alt`).
* Bruk `h2` for mellomoverskrifter (“Fakta”, “Slik skjedde det”).
* Lag punktliste (`ul` + `li`) og nummerert liste (`ol` + `li`).
* Lag to lenker med `a href`.
* Uthev advarselen med `strong`.

---

## Råtekst til artikkelen (sett riktige HTML-elementer på dette)

TITTEL: 15-åring reddet hund fra iskald elv i sentrum

Ingress: Lørdag formiddag dro en 15 år gammel ungdom en liten hund i sikkerhet fra elva Kverna etter at isen brast langs bredden. Redningsaksjonen skjedde under oppsyn av voksne og ble gjennomført uten personskader.


Brødtekst avsnitt 1: Vitner forteller at hunden hadde glidd ut på tynn is nær brua da en sprekk åpnet seg. Ungdommen holdt seg på trygg avstand, ringte nødnummeret og fulgte instruksjoner fra voksne på stedet.

Brødtekst avsnitt 2: Da hunden drev mot kanten, brukte han et langt tau festet i rekkverket og en pinne som forlengelse for å hekte i selen. Etter kort tid fikk de dyret trygt opp av vannet, innpakket i tepper fra forbipasserende.

Sitat (kort): «Jeg gjorde bare det vi øvde på – hold avstand, rop på hjelp og bruk tau», sier 15-åringen.

BILDE:
Filnavn/URL: [https://picsum.photos/id/1025/600/400](https://picsum.photos/id/1025/600/400)
Alternativtekst: Ungdom holder tau mens en våt hund pakkes inn ved elvebredden.


Mellomtittel: Fakta

Fakta punktliste:

* Vær: 1 °C og lett snødryss
* Vannstand: høy etter snøsmelting
* Varsel: tynn is langs elvebredden
* Tilstede: to voksne vitner og en brannkonstabel utenfor tjeneste

Mellomtittel: Slik skjedde det

Nummerert liste (trinn):

1. Ringte 110 og beskrev situasjonen
2. Festet tau i rekkverk og fant en pinne som forlengelse
3. Hev tauet forbi hundens sele
4. Dro rolig inn til kanten uten å gå ut på isen
5. Pakket hunden i tepper og ventet på brannvesenet

Lenker (skriv som klikkbare lenker):
Les om sikker ferdsel ved islagte vann: [https://www.varsom.no](https://www.varsom.no)
Råd for dyrevelferd i kulde: [https://www.dyrevern.no](https://www.dyrevern.no)

Advarsel: Merknad: Bruk alltid tau og hold avstand ved isforhold. Kontakt nødetater først.

Utheving: Sett ordet “Merknad:” i fet skrift.

Kontakt:
Pressekontakt: Nina Aas, frivillig hjelpekorps
E-post: [info@hjelpekorps.no](mailto:info@hjelpekorps.no)
Telefon: 55 55 55 55

---

## Elementer som SKAL brukes (tabell med forklaring og eksempel)

| Element  | Hva brukes det til?                               | Mini-eksempel (bare som tekst)                                          |
| -------- | ------------------------------------------------- | ----------------------------------------------------------------------- |
| `h1`     | Sidens hovedoverskrift (unik).                    | `<h1>15-åring reddet hund fra iskald elv</h1>`                          |
| `p`      | Avsnitt med brødtekst.                            | `<p>Vitner forteller at …</p>`                                          |
| `q`      | Kort sitat inne i et avsnitt (får anførselstegn). | `<p><q>Jeg gjorde bare det vi øvde på</q>, sier 15-åringen.</p>`        |
| `img`    | Viser bilde; bruk `src` og beskrivende `alt`.     | `<img src="https://…/600/400" alt="Ungdom holder tau ved elvebredden">` |
| `h2`     | Mellomoverskrift som deler inn stoffet.           | `<h2>Fakta</h2>`                                                        |
| `ul`     | Punktliste uten rekkefølge.                       | `<ul><li>Vær: 1 °C</li>…</ul>`                                          |
| `ol`     | Nummerert liste med rekkefølge.                   | `<ol><li>Ringte 110</li>…</ol>`                                         |
| `li`     | Ett punkt i en liste (`ul`/`ol`).                 | `<li>Varsel: tynn is</li>`                                              |
| `a`      | Klikkbar lenke (bruk `href`).                     | `<a href="https://www.varsom.no">varsom.no</a>`                         |
| `strong` | Uthever viktig tekst (semantisk viktig).          | `<strong>Merknad:</strong> Hold avstand ved is.`                        |


Vil du at jeg også lager en **løsningsmal** (HTML) du kan dele etter økten?
