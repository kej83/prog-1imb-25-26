<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>Flervalgsquiz</h1>

    <h2>Spørsmål 1</h2>
    <p>Hva heter det høyeste fjellet på dovrefjell?</p>
<!-- samme name kobler radioknapper sammen! -->
   <input type="radio" name="fjell" value="snohetta" id="snohetta">
   <label for="snohetta">Snøhetta</label><br>
    <input type="radio" name="fjell" value="galdhopiggen" id="galdhopiggen">
   <label for="galdhopiggen">Galdhøpiggen</label><br>
   <input type="radio" name="fjell" value="glittertind" id="glittertind">
   <label for="glittertind">Glittertind</label><br>

   <h2>Spørsmål 1</h2>
    <p>Hva heter den største elva i Finnmark?</p>
<!-- samme name kobler radioknapper sammen! -->
   <input type="radio" name="elv" value="lakselv" id="lakselv">
   <label for="lakselv">Lakselv</label><br>

    <input type="radio" name="elv" value="tana" id="tana">
   <label for="tana">Tana</label><br>

   <input type="radio" name="elv" value="stabburselva" id="stabburselva">
   <label for="stabburselva">Stabburselva</label><br>

   <!-- TODO: 
    LEGG TIL 3 spørsmål! -->

   <button onclick="sjekkSvar()">Sjekk svar</button>
   <p id="txtUt"></p>

   <script>
    function sjekkSvar() {
        let poeng = 0;

        let svar1 = document.querySelector("input[name='fjell']:checked").value;
        let svar2 = document.querySelector("input[name='elv']:checked").value;
        // Hente svar fra spm 3-5.

        if (svar1 == fasit1) {
            // Øk poeng med 1
        } 
        if (svar2 == fasit2) {
            // Øk poeng med 1
        }

        // TODO: Skriv en samlet melding med antall poeng. Skriv 3 ulike meldinger. 5 poeng gir hurra, 3 eller 4 poeng gir greit nok, ellers dårlig.
    }
    
    let fasit1 = "snohetta";
    let fasit2 = "tana";
    // TODO fasit til spm 3-5.
   </script>
</body>
</html>


<!DOCTYPE html>
<html lang="no">
<head>
  <meta charset="UTF-8">
  <title>Oppgave: Discord Tilgangslogikk</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      max-width: 700px;
      margin: 40px auto;
      line-height: 1.6;
    }
    h1 {
      margin-bottom: 10px;
    }
    code {
      background: #f3f3f3;
      padding: 2px 5px;
      border-radius: 4px;
    }
    .box {
      border: 1px solid #ccc;
      padding: 15px;
      margin-top: 20px;
      background: #fafafa;
      border-radius: 8px;
    }
  </style>
</head>
<body>

  <h1>Oppgave: Brukertilgang til Discord-server</h1>

  <p>Når brukeren trykker på en knapp, skal du vise en melding basert på hvilken tilgang de får.</p>

  <div class="box">
    <h2>Krav til logikk</h2>

    <ul>
      <li>Hvis brukernavn er tomt → <strong>"Du må skrive inn brukernavn."</strong></li>
      <li>Hvis regler ikke er huket av → <strong>"Du må godta reglene for å bli med."</strong></li>
      <li>Hvis regler er godkjent og rolle er <code>admin</code> eller <code>mod</code> → <strong>"Full tilgang"</strong></li>
      <li>Hvis regler er godkjent og rolle er <code>member</code> → <strong>"Begrenset tilgang"</strong></li>
      <li>Hvis rolle er <code>guest</code> uansett → <strong>"Kun visning, ingen tilgang"</strong></li>
    </ul>
  </div>

  <label for="username">Brukernavn:</label>
  <input type="text" id="username">
  <br><br>

  <label for="role">Velg rolle:</label>
  <select id="role">
    <option value="guest">Guest</option>
    <option value="member">Member</option>
    <option value="mod">Moderator</option>
    <option value="admin">Admin</option>
  </select>
  <br><br>

  <input type="checkbox" id="rules">
  <label for="rules">Jeg har lest og godtatt reglene</label>
  <br><br>

  <button onclick="checkAccess()">Sjekk</button>

  <p id="result"></p>

  <script>
    function checkAccess() {
      const username = document.getElementById("username").value;
      const role = document.getElementById("role").value;
      const rules = document.getElementById("rules").checked;
      const result = document.getElementById("result");

      // Sjekk om username tomt
      // username.trim() FJERNER mellomrom
      // " erna  ".trim() blir "erna"
      if (username.trim().length === 0) {
            result.textContent = "Skriv inn brukernavn!";
            //return;  // avslutter funksjonen
            // ! betyr IKKE. !true gir false, !false gir true
            // ELLERS HVIS IKKE RULES ER HAKET AV
      } else if (!rules) {
           result.textContent = "Du må godta reglene for å bli med.";
      } // Regler godkjent: sjekk user
      else if(role === "mod" || role === "admin" ) {
            result.textContent = "Full tilgang!";
      } else if(role === "member") {
        result.textContent = "Begrenset tilgang";
      } else {  // role === "guest"
        result.textContent = "Kun visningstilgang";
      }
    }
  </script>

</body>
</html>


<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>Straffespark</h1>
    <p>Arne skyter straffe. Han treffer med 70 % sannsynlighet.</p>
    <button onclick="sparkTo()">Spark to ganger</button>
    <h2></h2>

    <script>
        function sparkTo(){
            let tall1 = Math.random();
            let tall2 = Math.random();
            // Boolske variabler: er enten true eller false
            let treff1 = tall1 < 0.70;
            let treff2 = tall2 < 0.70;

            let antallTreff = 0;
            // Antall treff
            if(treff1) {
                antallTreff++;
            }
            if(treff2) {
                antallTreff++;
            }
            let txt = `Du skårte ${antallTreff} av 2 mulige.`;
            document.querySelector("h2").textContent = txt;
            // Oppgave 1:
            // Utvid slik at utskriften viser hvilket skudd som var treff og hvilket skudd som var bom.
            // Eksempelutskrift:
            // Skudd 1: bom
            // Skudd 2: treff
            // Du skårte 1 av 2 mulige.

            // Oppgave 2:
            // Utvid til 3 skudd totalt.
    
        }
    </script>
</body>
</html>
