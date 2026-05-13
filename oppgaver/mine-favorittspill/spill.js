// ============================================================
//  FAVORITTSPILL – JavaScript-oppgave
//  Navn: ___________________________________
//  Dato: ___________________________________
// ============================================================
//
//  INSTRUKSJONER TIL ELEVEN:
//  -------------------------------------------------
//  HTML og CSS er ferdig laget for deg.
//  Din jobb er å fylle inn koden INNI hver funksjon
//  slik at nettsiden fungerer.
//
//  Regler:
//    1. Du skal IKKE endre noe i index.html eller style.css.
//    2. Du skal IKKE endre funksjonsnavnene eller variablene.
//    3. Fyll inn kode bare der det står "// TODO:" og mellom
//       de tomme klammeparentesene  {  }.
//    4. Test siden i nettleseren etter hvert steg.
//    5. Bruk konsollen (F12) for å feilsøke.
//
//  Steg-for-steg anbefalt rekkefølge:
//    Steg 1 → visAllSpill()         (bare vis, ikke slett)
//    Steg 2 → leggTilSpill()        (legg til nytt spill)
//    Steg 3 → fjernSpill()          (fjern ett spill)
//    Steg 4 → sokEtterSpill()       (filtrer listen)
//    Steg 5 → nullstillSok()        (tøm søk og vis alle)
//    Steg 6 → sorterListe()         (alfabetisk sortering)
//    Steg 7 → oppdaterStatistikk()  (statistikk-bokser)
//    Bonus  → settArstall()         (footer-årstall)
//
// ============================================================


// ------------------------------------------------------------
//  GLOBALE VARIABLER
//  Disse er klare til bruk – du trenger ikke endre dem.
// ------------------------------------------------------------

// Array med tre favorittspill som allerede er lagt inn.
// Du kan endre spillnavnene om du vil, men behold tre stykker.
let spill = [
  "Minecraft",
  "The Legend of Zelda: Breath of the Wild",
  "Stardew Valley"
];

// Holder styr på om listen er sortert eller ikke.
let erSortert = false;

// Referanser til HTML-elementer vi trenger ofte.
// Du kan bruke disse variablene direkte i funksjonene.
const spillisteEl        = document.getElementById("spilliste");
const tomListeMelding    = document.getElementById("tom-liste-melding");
const nyttSpillInput     = document.getElementById("nytt-spill-input");
const sokInput           = document.getElementById("sok-input");
const tilbakemeldingEl   = document.getElementById("tilbakemelding-legg-til");
const sokresultatInfoEl  = document.getElementById("sokresultat-info");
const listeInfoEl        = document.getElementById("liste-info");


// ------------------------------------------------------------
//  HJELPEFUNKSJON – hjelpVisListe(spillArray)
//  Denne er ferdig! Den tar en liste med spill og viser dem
//  i <ul id="spilliste"> på siden.
//  Du TRENGER ikke endre den, men les den gjerne for å forstå.
// ------------------------------------------------------------
function hjelpVisListe(spillArray) {
  // Tøm listen i HTML
  spillisteEl.innerHTML = "";

  if (spillArray.length === 0) {
    // Vis "tom liste"-melding hvis ingen spill finnes
    tomListeMelding.style.display = "block";
    return;
  }

  tomListeMelding.style.display = "none";

  // Loop gjennom spillArray og lag ett <li>-element per spill
  spillArray.forEach(function (navn, indeks) {
    const li = document.createElement("li");

    li.innerHTML = `
      <span class="spill-indeks">#${indeks + 1}</span>
      <span class="spill-navn">${navn}</span>
      <button class="fjern-knapp" onclick="fjernSpill('${navn}')">✕ Fjern</button>
    `;

    spillisteEl.appendChild(li);
  });
}


// ------------------------------------------------------------
//  FUNKSJON 1 – visAllSpill()
//  Kalles når brukeren klikker «Vis alle»-knappen.
// ------------------------------------------------------------
function visAllSpill() {
  // TODO: Kall hjelpVisListe() med hele spill-arrayen
  //       slik at alle spill vises på siden.

  // TODO: Oppdater listeInfoEl.textContent til å vise
  //       hvor mange spill som finnes i listen.
  //       F.eks.: "Viser 3 spill."

  // TODO: Tøm sokInput og sokresultatInfoEl.textContent
  //       slik at søkefeltet nullstilles.
}


// ------------------------------------------------------------
//  FUNKSJON 2 – leggTilSpill()
//  Kalles når brukeren klikker «Legg til»-knappen.
// ------------------------------------------------------------
function leggTilSpill() {
  // TODO: Hent teksten brukeren skrev inn i nyttSpillInput.
  //       Tips: .value og .trim()

  // TODO: Sjekk om input-feltet er tomt.
  //       Hvis tomt → vis en feilmelding i tilbakemeldingEl
  //       (legg til klassen "feil") og avslutt funksjonen.

  // TODO: Sjekk om spillet allerede finnes i spill-arrayen.
  //       Tips: .includes()
  //       Hvis det finnes → vis passende feilmelding og avslutt.

  // TODO: Legg den nye teksten til i spill-arrayen.
  //       Tips: .push()

  // TODO: Vis en suksessmelding i tilbakemeldingEl
  //       (bruk klassen "ok", fjern klassen "feil").

  // TODO: Tøm input-feltet etter at spillet er lagt til.

  // TODO: Kall visAllSpill() for å oppdatere listen på siden.

  // TODO: Kall oppdaterStatistikk() for å oppdatere statistikken.
}


// ------------------------------------------------------------
//  FUNKSJON 3 – fjernSpill(navn)
//  Kalles når brukeren klikker «✕ Fjern» ved et spill.
//  Parameteren "navn" er spillnavnet som skal fjernes.
// ------------------------------------------------------------
function fjernSpill(navn) {
  // TODO: Bruk confirm() for å spørre brukeren om de er sikre.
  //       Hvis de klikker "Avbryt" → gjør ingenting og avslutt.

  // TODO: Finn indeksen til "navn" i spill-arrayen.
  //       Tips: .indexOf()

  // TODO: Fjern elementet fra spill-arrayen.
  //       Tips: .splice(indeks, 1)

  // TODO: Kall visAllSpill() for å oppdatere listen.

  // TODO: Kall oppdaterStatistikk() for å oppdatere statistikken.
}


// ------------------------------------------------------------
//  FUNKSJON 4 – sokEtterSpill()
//  Kalles automatisk mens brukeren skriver i søkefeltet.
// ------------------------------------------------------------
function sokEtterSpill() {
  // TODO: Hent søketeksten fra sokInput.value og gjør den
  //       til små bokstaver med .toLowerCase()

  // TODO: Filtrer spill-arrayen slik at bare spill som
  //       inneholder søketeksten vises.
  //       Tips: .filter() og .includes() eller .toLowerCase()

  // TODO: Kall hjelpVisListe() med det filtrerte resultatet.

  // TODO: Oppdater sokresultatInfoEl.textContent med info om
  //       hvor mange treff søket ga.
  //       F.eks.: "Fant 2 spill med «mine»."

  // TODO: Hvis søkefeltet er tomt → vis alle spill og tøm infoteksten.
}


// ------------------------------------------------------------
//  FUNKSJON 5 – nullstillSok()
//  Kalles når brukeren klikker «✕ Nullstill»-knappen.
// ------------------------------------------------------------
function nullstillSok() {
  // TODO: Tøm søkefeltet (sokInput.value = "")

  // TODO: Tøm sokresultatInfoEl.textContent

  // TODO: Kall visAllSpill() for å vise hele listen igjen.
}


// ------------------------------------------------------------
//  FUNKSJON 6 – sorterListe()
//  Kalles når brukeren klikker «A–Å sorter»-knappen.
//  Skal veksle mellom sortert og usortert visning.
// ------------------------------------------------------------
function sorterListe() {
  // TODO: Sjekk variabelen erSortert.
  //       Hvis IKKE sortert → sorter spill-arrayen alfabetisk
  //                           med .sort() og sett erSortert = true.
  //       Hvis allerede sortert → sorter i omvendt rekkefølge
  //                              (Z–A) og sett erSortert = false.
  //       Tips: .sort() og .reverse(), eller en sammenligningsfunksjon.

  // TODO: Kall hjelpVisListe() for å oppdatere visningen.

  // TODO: Oppdater listeInfoEl.textContent med en melding
  //       som forteller om listen er sortert A–Å eller Z–A.
}


// ------------------------------------------------------------
//  FUNKSJON 7 – oppdaterStatistikk()
//  Kalles når brukeren klikker «Oppdater statistikk»-knappen,
//  og automatisk etter leggTilSpill() og fjernSpill().
// ------------------------------------------------------------
function oppdaterStatistikk() {
  // TODO: Hent elementet med id="antall-spill" og sett
  //       .textContent til antall spill i listen.

  // TODO: Finn spillnavnet med flest tegn i spill-arrayen.
  //       Tips: løkke eller .reduce()
  //       Sett elementet med id="lengste-navn" til dette navnet.
  //       Hvis listen er tom → vis "–"

  // TODO: Hent det siste spillet som ble lagt til
  //       (det siste elementet i spill-arrayen).
  //       Sett elementet med id="siste-lagt-til" til dette.
  //       Hvis listen er tom → vis "–"
}


// ------------------------------------------------------------
//  FUNKSJON 8 – settArstall()  [BONUS]
//  Viser inneværende år i footeren.
// ------------------------------------------------------------
function settArstall() {
  // TODO: Bruk new Date() og .getFullYear() til å hente
  //       inneværende år.
  //       Sett elementet med id="ar" sitt .textContent til året.
}


// ------------------------------------------------------------
//  OPPSTART
//  Disse to linjene kjøres automatisk når siden lastes.
//  De sørger for at listen og statistikken vises med en gang.
//  Du trenger IKKE endre disse.
// ------------------------------------------------------------
visAllSpill();
oppdaterStatistikk();
settArstall();
