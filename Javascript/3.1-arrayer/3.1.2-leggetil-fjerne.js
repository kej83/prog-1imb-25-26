let venner = ["per", "pål", "espen", "sara"];
console.log(venner);
// Legge til med push og unshift
venner.push("jens");
console.log(venner);
venner.push("ali baba");
console.log(venner);
// legge til foran
venner.unshift("maria");
console.log(venner);

/* SLETTING med pop og shift */

venner.pop();
console.log(venner);
venner.pop();
console.log(venner);

venner.shift();
console.log(venner);

/* Legge til på spesiell plass */
venner.splice(1, 0, "halvor");
console.log(venner);
venner.splice(3, 0, "aliah");
console.log(venner);

/* Slette på spesiell plass */
// pål har nå index 2, vil slette ham
// 2 betyr index, 1 betyr slett 1 element!
venner.splice(2, 1);
console.log(venner);
venner.splice(3, 1);
console.log(venner);
