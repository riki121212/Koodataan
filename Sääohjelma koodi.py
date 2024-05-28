import requests

# Hakee säätiedot OpenWeatherMap API:sta käyttäjän syöttämän kaupungin perusteella.

def hae_saa(kaupunki):
    api_avain = "a5f258ebce62bab18e7ea5967a2ea1f3"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={kaupunki}&appid={api_avain}&units=metric&lang=fi"
    vastaus = requests.get(url)
    data = vastaus.json()
    return data

# Kerää säätiedot ja muodostaa ne meidän haluamalla tavalla. 

def tarkista_sää(säädata):
    sääkuvaus = säädata["weather"][0]["description"]
    lämpötila = säädata["main"]["temp"]
    tuulen_nopeus = säädata["wind"]["speed"]
    pilvisyys = säädata["clouds"]["all"]
    kosteus = säädata["main"]["humidity"]
    säätila = f"""
    Sää: {sääkuvaus}
    Lämpötila: {lämpötila}°C
    Tuulen nopeus: {tuulen_nopeus} m/s
    Pilvisyys: {pilvisyys}%
    Ilmankosteus: {kosteus}%
    """
    return säätila

# Antaa matkustussuosituksen säätietojen perusteella.

def matkustus_suositus(säädata):
    sääkuvaus = säädata["weather"][0]["main"].lower()
    lämpötila = säädata["main"]["temp"]
    
    if "sateinen" in sääkuvaus:
        return "On sateinen sää. Ehkä kannattaa odottaa vähän parempaa säätä ennen matkustamista."
    elif "lumisade" in sääkuvaus or "räntäsade" in sääkuvaus:
        return "On lumisadetta tai räntäsadetta. Ehkä kannattaa odottaa vähän parempaa säätä ennen matkustamista."
    elif lämpötila >= 25:
        return "On lämmin sää. Ota aurinkorasvaa mukaan ja nauti matkasta!"
    elif lämpötila >= 10:
        return "On kohtalainen sää. Hyvä aika matkustaa!"
    elif lämpötila < 10:
        return "On viileä sää. Pidä lämpimät vaatteet mukana ja nauti matkastasi!"
    else:
        return "Säätila ei ole selvillä."

# Pääohjelma, joka pyytää käyttäjältä kaupungin nimen ja näyttää säätiedot ja matkustussuosituksen. 

def main():
    while True:
        kaupunki = input("Syötä kaupungin nimi: ")
        sää = hae_saa(kaupunki)

        if sää["cod"] == 200:
            säätila = tarkista_sää(sää)
            print(f"Sää kaupungissa {kaupunki}:")
            print(säätila)
            
            valinta1 = input("Haluatko saada myös matkustussuosituksen? (kyllä/ei): ")
            if valinta1.lower() == "kyllä":
                suositus = matkustus_suositus(sää)
                print(suositus)
            
            valinta2 = input("Haluatko nähdä säätiedot toisesta kaupungista? (kyllä/ei): ")
            if valinta2.lower() != "kyllä":
                print("Kiitos, että käytit sääpalveluamme!")
                break

        else:
            print("Kaupunkia ei löytynyt. Yritä uudestaan.")

if __name__ == "__main__":
    main()
