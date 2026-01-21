let frukt = "eple";
// Array inneholder flere verdier
let frukter = ["eple", "banan", "kiwi"];

// Skrive ut hele arrayet
console.log(frukter);

// Skrive ut én av verdiene
console.log(frukter[1]);  // banan
console.log(frukter[0]);  // eple

// Feil:
console.log(frukter[3]);  // undefined

// Endre verdier
frukter[1] = "pære";
console.log(frukter);

// Array med tall
let tall = [3, 5, -10, 300];
console.log(tall[0] + tall[1]);  // 8
console.log(tall[3] + tall[2]);  // 290
