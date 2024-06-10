# Sääohjelma


<h3>Mistä ohjelmassa on kysymys? </h3>

Ohjelma hakee ja kertoo sään OpenWeatherMap sivun API:n avulla
käyttäjän syöttämän kaupungin perusteella. Se tarjoaa myös matkustussuosituksen näiden säätietojen perusteella.

<h3>Mitä se tekee? </h3>

Kysyy käyttäjältä kaupungin nimen, jonka jälkeen ohjelma hakee säätiedot kyseisestä kaupungista ja muotoilee ne käyttäjälle valmiiksi määritetyllä tavalla. Lisäksi ohjelma antaa käyttäjälle mahdollisuuden pyytää matkustussuositusta säätietojen perusteella. 

<h3>Miten aiotte sen toteuttaa? </h3>

Ohjelman toteutus tapahtuu käyttämällä Python-ohjelmointikieltä ja hyödyntämällä OpenWeatherMapin tarjoamaa API
säätietojen hakuun.

----------------------------------------------------------------------------------------------------

<h3>Miten käyttää/käynnistää? </h3>

1. <h5>Lataa "Sääohjelma koodi.py" -tiedosto haluamaasi sijaintiin tietokoneellasi. </h5>

2. <h5>Avaa komentokehote tai PowerShell: </h5>
Paina "Windows+R" avataksesi "Suorita"-ruudun. Kirjoita sitten "cmd" tai "powershell" ja napsauta "OK" avataksesi komentokehotteen tai PowerShellin.

3. <h5>Siirry tiedoston hakemistoon: </h5>
Käytä "cd"-komennolla siirtyäksesi kansioon, jossa "Sääohjelma koodi.py" -tiedosto sijaitsee. Esimerkiksi, jos tiedosto on latautunut "Lataukset" -kansioon, kirjoita: cd C:\Users\käyttäjänimi\Downloads

4. <h5>Käynnistä ohjelma: </h5>
Kun olet haluamassasi hakemistossa, kirjoita komento: python "Sääohjelma koodi.py". Tämä käynnistää ohjelman, ja se alkaa pyytämään kaupungin nimeä säätietojen hakemiseksi.

5. <h5>Anna kaupungin nimi: </h5>
Ohjelma pyytää sinua syöttämään kaupungin nimen. Kirjoita haluamasi kaupungin nimi ja paina Enter. Tämän jälkeen ohjelma näyttää kyseisen kaupungin säätiedot.

6. <h5>Valinnainen: Matkasuositus: </h5>
Ohjelma kysyy haluatko matkasuosituksen. Vastaa "kyllä" saadaksesi suosituksen tai "ei" ohittaaksesi sen.

7. <h5>Valinnainen: Uusi säätiedotus: </h5>
Ohjelma kysyy haluatko nähdä säätiedot toisesta kaupungista. Vastaa "kyllä" jatkaaksesi tai "ei" lopettaaksesi ohjelman.

----------------------------------------------------------------------------------------------------

<h3>Toimintalogiikka vuokaavio </h3>

![What is this](Kaavio.jpg)

----------------------------------------------------------------------------------------------------

<h3>Demo ohjelmasta </h3>

<link>https://youtu.be/E8aR07q0nHc?si=1d1HzVArYfoSeubr</link>

----------------------------------------------------------------------------------------------------

Ryhmän jäsenet: Riki Leppänen, Mika Venäläinen ja Niilo Pitkänen
