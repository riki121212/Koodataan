import requests

def get_weather(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    return data

def main():
    city = input("Syötä kaupungin nimi: ")
    api_key = "TÄHÄN_API_AVAIN"
    weather_data = get_weather(city, api_key)

    if weather_data["cod"] == 200:
        print(f"Aktuaalinen lämpötila kaupungissa {city}: {weather_data['main']['temp']}°C")
        print(f"Kuvaus: {weather_data['weather'][0]['description']}")
    else:
        print("Virhe: Kaupunkia ei löydy.")

if __name__ == "__main__":
    main()
