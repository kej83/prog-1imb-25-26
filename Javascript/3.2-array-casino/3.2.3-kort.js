// 2-14, det er 4 av hver verdi, 52 kort
let kortstokk = [];
for (let i = 2; i <= 14; i++) {
    for (let j = 0; j < 4; j++) {
        kortstokk.push(i);
    }
}

console.log(kortstokk);

// Stokke kortstokken
let stokketKort = [];

for (let i = 0; i < 52; i++) {
    // Vi trekker tilfeldig kort og lager en stokket kortstokk
    let index = Math.floor(Math.random() * kortstokk.length);
    let nyttKort = kortstokk[index];
    stokketKort.push(nyttKort);

    // Før vi trekker et tilfeldig kort til, så må kortet vi trakk fjernes
    kortstokk.splice(index, 1);
}

console.log(stokketKort);

// Eksempel på kortspill: spiller 1 trekker ett kort, deretter trekker spiller 2 ett kort. Den har høyest får ett poeng.
let spiller1Kort = stokketKort.pop();
let spiller2Kort = stokketKort.pop();

console.log(spiller1Kort, spiller2Kort);

if (spiller1Kort > spiller2Kort) {
    console.log("spiller1 vant");
} else if (spiller2Kort > spiller1Kort) {
    console.log("spiller2 vant");
} else {
    console.log("uavgjort");
}

// Oppgave: Lag en enkel nettside som lager en stokket kortstokk. Når spilleren trykker på knappen KRIG, så trekker spilleren ett kort og cpu trekker ett kort. Vinneren får 1 poeng. Dette fortsetter til det ikke er flere kort igjen, da kåres vinneren.
