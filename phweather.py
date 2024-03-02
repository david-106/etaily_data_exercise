import json, requests

BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
API_KEY = "e0c63dc6f98188bf9c81c76fff18f9e9"
CITY = "Malolos"

def k_to_c(kelvin):
    celsius = kelvin - 273.15
    return celsius

url = BASE_URL + "appid= " + API_KEY + "&q=" + CITY

response = requests.get(url).json()

print(response)

temp_k = response['main']['temp']
temp_c = k_to_c(temp_k)
feels_like_kelvin = response['main']['feels_like']
feels_like_celsius = k_to_c(feels_like_kelvin)
humidity = response['main']['humidity']
description = response['weather'][0]['description']
wind_speed = response['wind']['speed']

print(f"Temperature in {CITY}: {temp_c:.2f}Celsius")
print(f"Humidity in  {CITY}: {humidity}%")
print(f"Wind Speed in {CITY}: {wind_speed}m/s")
print(f"General Weather in {CITY}: {description}")

res = response.json()

#I think the historical data in openweathermap AI is paid.