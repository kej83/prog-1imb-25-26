// Lage et terningkast
let kast = Math.floor(Math.random()*6 + 1)
console.log(kast);

// Flere kast
let kastene = [];
let antallKast = 10;

for(let i = 0 ; i < antallKast; i++) {
    let nyttKast = Math.floor(Math.random()*6 + 1);
    kastene.push(nyttKast);
}
console.log(kastene);

