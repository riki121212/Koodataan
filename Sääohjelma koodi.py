import requests

def hae_saa(kaupunki):
    api_avain = "a5f258ebce62bab18e7ea5967a2ea1f3"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={kaupunki}&appid={api_avain}&units=metric"
    vastaus = requests.get(url)
    data = vastaus.json()
    return data

def tarkista_sää(säädata):
    sääkuvaus = säädata["weather"][0]["description"]
    if "rain" in sääkuvaus:
        return "Sataa"
    elif "clear" in sääkuvaus:
        return "Poutaa"
    else:
        return "Säätila ei ole selvillä"

def main():
    kaupunki = input("Syötä kaupungin nimi: ")
    sää = hae_saa(kaupunki)

    if sää["cod"] == 200:
        lämpötila = sää["main"]["temp"]
        print(f"Sää kaupungissa {kaupunki}: {lämpötila}°C")

        säätila = tarkista_sää(sää)
        print(f"Sää: {säätila}")

        if "sateista" in säätila:
            print("On sateista. Ehkä kannattaa odottaa vähän parempaa säätä ennen matkustamista.")
        elif "poutaista" in säätila:
            print("On poutaista. Kannattaa matkustaa kaupunkiin!")
        else:
            print("Säätila ei ole selvillä.")

    else:
        print("Kaupunkia ei löytynyt. Yritä uudestaan.")

if __name__ == "__main__":
    main()
