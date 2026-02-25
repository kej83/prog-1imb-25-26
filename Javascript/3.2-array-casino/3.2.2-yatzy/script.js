function lag6Terninger() {
    let tempKast = [];
    for (let i=0; i<6; i++) {
        let nyttKast = Math.floor(Math.random()*6+1);
        tempKast.push(nyttKast);
    }
    return tempKast;
}

function treLike() {
    let kastene = lag6Terninger();
    // Sjekk tre like for enere, toere, ... 6-ere
    for(let i = 1; i <= 6; i++) {
        let antall = 0;
        for (let kast of kastene) {
            if (kast === i) {
                antall++;
            }
        }
        if (antall >= 3) {
            txtUt.textContent = `${kastene}. 3 like! Hurra!"`;
            return;  // avslutt funksjonen
        }
    }
    txtUt.textContent = `${kastene}. IKKE 3 like, dessverre.`;
}
function enere() {
    // Kast 6 terninger
    let kastene = lag6Terninger();
    // Antall enere
    let antallEnere = 0;
    // Sjekker 1 terning om gangen
    for (let kast of kastene) {
        if (kast === 1) antallEnere++;
    }
    // console.log(kastene);
    // console.log(antallEnere);
    let txt = `Du kastet ${kastene.join(",")}. Dvs. ${antallEnere} enere`;
    txtUt.textContent = txt;
}

let btnEnere = document.getElementById("btnEnere");
let btnTreLike = document.getElementById("btnTreLike");
let txtUt = document.getElementById("txtUt");

// Events
btnEnere.addEventListener("click", enere);
btnTreLike.addEventListener("click", treLike);
