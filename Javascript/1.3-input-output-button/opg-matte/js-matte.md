# 20 øveoppgaver input output JS

## Info:
 Hver oppgave har: hva som skal lages, hvilke inputfelt som trengs, formel, og hva som skal vises i output når de klikker en knapp. Bruk input, p, button.

 **Viktig**: Lag 1 ny html fil for hver oppgave.

1. Areal av rektangel
   Input: bredde, høyde.
   Formel: areal = bredde * høyde.
   Output: “Areal: X cm²”.

2. Omkrets av rektangel
   Input: bredde, høyde.
   Formel: omkrets = 2*(bredde + høyde).
   Output: “Omkrets: X cm”.

3. Areal og omkrets av sirkel
   Input: radius.
   Formler: areal = π*r², omkrets = 2*π*r.
   Output: begge verdier.

4. BMI-kalkulator
   Input: høyde (m), vekt (kg).
   Formel: BMI = vekt / (høyde²).
   Output: BMI (avrundet til 1 desimal).

5. Temperaturkonvertering
   Input: temperatur i °C.
   Formel: °F = (°C * 9/5) + 32, K = °C + 273.15.
   Output: i °F og K.

6. Rabattkalkulator (prosent)
   Input: originalpris, rabatt (%)
   Formel: pris_med_rabatt = pris * (1 - rabatt/100).
   Output: ny pris og spart beløp.

7. Fart, tid, strekning (velg én ukjent)
   Input: to av tre: fart (km/t), tid (t), strekning (km).
   Formler: s=f*t, f=s/t, t=s/f.
   Output: beregn den manglende.

8. Gjennomsnittskalkulator (3 tall)
   Input: tall1, tall2, tall3.
   Formel: snitt = (t1+t2+t3)/3.
   Output: gjennomsnitt (2 desimaler).

9. Valutakonverterer (NOK → EUR)
   Input: beløp i NOK, kurs (NOK per EUR).
   Formel: EUR = NOK / kurs.
   Output: beløp i EUR.

10. Pythagoras (rettvinklet trekant)
    Input: katet a, katet b.
    Formel: c = √(a² + b²).
    Output: hypotenus.

11. Areal av trekant (grunnlinje–høyde)
    Input: grunnlinje, høyde.
    Formel: areal = (grunnlinje*høyde)/2.
    Output: areal.

12. Trapesareal
    Input: a (øverste), b (nederste), h (høyde).
    Formel: areal = (a + b)/2 * h.
    Output: areal.

13. Sylinder: volum og overflate
    Input: radius r, høyde h.
    Formler: V = πr²h, A = 2πr(h + r).
    Output: begge verdier.

14. Kule: volum og overflate
    Input: radius r.
    Formler: V = 4/3 π r³, A = 4π r².
    Output: begge verdier.

15. Lånekalkulator (enkel månedskostnad, annuitet)
    Input: lånebeløp L, rente p% pr år, antall år n.
    Formel: månedsrente r = p/100/12; avdrag = L * r / (1 - (1+r)^(-12n)).
    Output: månedlig betaling (avrundet).

16. Prosentvis endring
    Input: gammel verdi, ny verdi.
    Formel: endring% = (ny − gammel)/gammel * 100.
    Output: prosent med +/−-tegn.

17. Karakterkalkulator (vekta snitt)
    Input: poeng for 3 vurderinger + vekter (sum 100%).
    Formel: snitt = Σ(poeng_i * vekt_i/100).
    Output: vekta poengsum.

18. Drivstoffkostnad på tur
    Input: distanse (km), forbruk (liter/100km), pris per liter.
    Formel: liter = distanse * forbruk / 100; kostnad = liter * pris.
    Output: liter og total kostnad.

19. Lønn etter skatt og fradrag
    Input: brutto lønn, skattesats %, fradrag.
    Formel: skatt = brutto * sats/100; netto = brutto − skatt − fradrag.
    Output: skatt og netto.

20. Andregradsløsning (ax²+bx+c=0)
    Input: a, b, c.
    Formler: D = b²−4ac.
    Hvis D<0 → “Ingen reelle røtter”.
    Hvis D=0 → x = −b/(2a).
    Hvis D>0 → x1,2 = (−b ± √D)/(2a).
    Output: røtter.

Tips til struktur (alle oppgaver):

* HTML: `<input>`-felter med `id`, en `<button>` med `onclick`, og et `<p id="txtUt">`.
* JS: Les verdier med `Number(document.getElementById("...").value)`, beregn med variabler, og skriv ut med `textContent` eller `innerHTML`.
* Validering: sjekk tomme felt og negative verdier der det er naturlig.
* Avrunding: bruk `toFixed(2)` ved penger og målinger.
