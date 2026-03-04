function nyKortStokk() {
    // 2-14, det er 4 av hver verdi, 52 kort
    let kortstokk = [];
    for (let i = 2; i <= 14; i++) {
        for (let j = 0; j < 4; j++) {
            kortstokk.push(i);
        }
    }

    let stokketKort = [];

    for (let i = 0; i < 52; i++) {
        // Vi trekker tilfeldig kort og lager en stokket kortstokk
        let index = Math.floor(Math.random() * kortstokk.length);
        let nyttKort = kortstokk[index];
        stokketKort.push(nyttKort);

        // Før vi trekker et tilfeldig kort til, så må kortet vi trakk fjernes
        kortstokk.splice(index, 1);
    }

    return stokketKort;
}

function trekk() {
    // Spiller trekker, deretter cpu
    let spiller1Kort = kort.pop();
    let cpuKort = kort.pop();

    let txt = `Spiller trakk ${spiller1Kort}. CPU trakk ${cpuKort}. <br>`;

    if (spiller1Kort > cpuKort) {
        txt += "Spilleren vant";
        spillerPoeng++;
    } else if (cpuKort > spiller1Kort) {
        txt += "cpu vant";
        cpuPoeng++;
    } else {
        txt += "uavgjort";
    }
        txt += `<br>POENG: Spiller: ${spillerPoeng}. CPU: ${cpuPoeng}`;
        txtUt.innerHTML = txt;
    if (kort.length < 2) {
        gameOver();
    }
}

function gameOver() {
    txtUt.textContent = `Game OVER! Spiller: ${spillerPoeng} poeng. CPU: ${cpuPoeng}.`;
    if (spillerPoeng > cpuPoeng) {
        txtUt.textContent += "Spiller vant!";
    } else if (cpuPoeng < spillerPoeng) {
        txtUt.textContent += "CPU vant!";
    } else {
        txtUt.textContent += "Uavgjort!";
    }
    btnTrekk.disabled = true;
}
// Stokke kortstokken
let kort = nyKortStokk();
let spillerPoeng = 0;
let cpuPoeng = 0;

// Elementer og events
let txtUt = document.getElementById("txtUt");
let btnTrekk = document.getElementById("btnTrekk");
btnTrekk.addEventListener("click", trekk);

