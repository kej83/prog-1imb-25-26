// Gjett tallet – script.js

// 0. Lag det hemmelige tallet når siden åpnes.
// Allerede gjort for dere:
const secretNumber = Math.floor(Math.random() * 100) + 1;
console.log("DEBUG – hemmelig tall:", secretNumber); // kan fjernes senere

// 1. Hent ut elementene fra HTML (input, knapp, melding, forsøk-teller)
const inpTall = document.getElementById("inpTall");
const btnGjett = document.getElementById("btnGjett");
const melding = document.getElementById("melding");
const forsok = document.getElementById("forsok");

// 2. Lag en variabel som teller hvor mange ganger eleven har gjettet.
let antallForsok = 0;

// 3. Lag en funksjon som skal kjøre når vi klikker på "Gjett"-knappen.
function sjekkGjett() {
  // 3.1 Les inn tallet fra input-feltet (inpTall.value)
  let gjett = inpTall.value;
  // 3.2 Konverter fra tekst til tall (Number(...) eller parseInt(...))
  gjett = Number(gjett)
  // 3.3 Øk antall forsøk med 1 og vis det i <p id="forsok">.
  // 3.4 Sammenlign tallet med secretNumber:
  //     - hvis tallet er lavere → skriv "For lavt 👇"
  //     - hvis tallet er høyere → skriv "For høyt ☝️"
  //     - hvis tallet er likt → skriv "Riktig! 🎉" og gjerne lås input eller vis gratulasjon
  // Meldingen skrives ut i <p id="melding"> feltet.
  // 3.5 Tøm input-feltet etterpå og sett fokus tilbake på det.
}

// 4. Koble knappen til funksjonen
btnGjett.addEventListener("click", sjekkGjett);

// 5. (Valgfritt) – gjør at eleven kan trykke ENTER i input for å gjette
// inpTall.addEventListener("keyup", function (event) {
//   if (event.key === "Enter") {
//     sjekkGjett();
//   }
// });
