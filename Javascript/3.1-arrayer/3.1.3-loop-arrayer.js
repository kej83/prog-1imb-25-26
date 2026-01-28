let biler = ["saab", "volvo", "bmw", "audi"];
// Uten løkke
console.log(biler[0]);  // saab
console.log(biler[1]);  // volvo
console.log(biler[2]);
console.log(biler[3]);

// Med while-løkke
console.log("---Med while-løkke---")
let indeks = 0;
while (indeks < 4) {
    console.log(biler[indeks]);
    indeks++;  // øker med 1
}
// Med for-løkke
console.log("---Med for-løkke---")
for(let i = 0; i < 4; i++) {
    console.log(biler[i]);
}