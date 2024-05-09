import requests

def hae_saa(kaupunki):
    api_avain = "a5f258ebce62bab18e7ea5967a2ea1f3"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={kaupunki}&appid={api_avain}&units=metric"
    vastaus = requests.get(url)
    data = vastaus.json()
    return data

def tarkista_pilvisyys(säädata):
    pilvisyys = säädata["weather"][0]["description"]
    return pilvisyys

def main():
    kaupunki = input("Syötä kaupungin nimi: ")
    sää = hae_saa(kaupunki)

    if sää["cod"] == 200:
        lämpötila = sää["main"]["temp"]
        print(f"Sää kaupungissa {kaupunki}: {lämpötila}°C")

        pilvisyys = tarkista_pilvisyys(sää)
        print(f"Pilvisyys: {pilvisyys}")

        if lämpötila >= 10:
            print("Kannattaa matkustaa!")
        else:
            print("Ehkä kannattaa odottaa vähän parempaa säätä.")

    else:
        print("Kaupunkia ei löytynyt. Yritä uudestaan.")

if __name__ == "__main__":
    main()
