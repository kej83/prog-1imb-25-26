function visOversikt() {
    let txt = "<h2>Oversikt</h2>";
    txt += "<ul>";
    // i er romnr
    for (let i=0; i<rom.length; i++) {
        txt += `<li>Romnr ${i}: ${rom[i]} </li>`;
    }
    txt += "</ul>";
    txtUt.innerHTML = txt;
}

function sjekkInn() {
    // 1. Lese inn navn og romnr
    let fornavn = inpNavn.value;
    let romnr = inpRomnr.value;  
    // 2. Sjekk om romnr er ledig
    if (rom[romnr] === "") {
        rom[romnr] = fornavn;
        txtUt.textContent = `${fornavn} ble booket på rom nr ${romnr}`;
    } else {
        txtUt.textContent = "Rommet er opptatt, velg et annet romnr.";
    }
    // 3. Sjekk inn gjesten, eller gi feilmelding dersom rommet var opptatt
}

// Hotellets datastruktur. "" betyr ledig
let rom = ["sara", "", "per", "", ""];

let btnVisOversikt = document.getElementById("btnVisOversikt");
let btnSjekkInn = document.getElementById("btnSjekkInn")
let inpNavn = document.getElementById("inpNavn");
let inpRomnr = document.getElementById("inpRomnr");

let txtUt = document.getElementById("txtUt");

btnVisOversikt.addEventListener("click", visOversikt);
btnSjekkInn.addEventListener("click", sjekkInn);