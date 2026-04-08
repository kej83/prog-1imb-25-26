function loggInn(event) {
    // Spesielt for form
    event.preventDefault();
    let bruker = inpBrukernavn.value;
    let passord = inpPassord.value; 

    if (bruker === fasitBruker && passord === fasitPass) {
         txtUt.textContent = "Du er logget inn!";
    } else {
        txtUt.textContent = "Feil brukernavn og/eller passord."
    }
   
}
// Korrekt bruker
let fasitBruker = "jens";
let fasitPass = "jens321";
// Koblinger til html-elementer
let formLoggInn = document.getElementById("formLoggInn");
let inpBrukernavn = document.getElementById("inpBrukernavn");
let inpPassord = document.getElementById("inpPassord");
let txtUt = document.getElementById("txtUt");

// Events
formLoggInn.addEventListener("submit", loggInn);