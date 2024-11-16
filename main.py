import json
import requests

city_name = input("Enter a city name: ")

api_key = "907a7838458f0525646035b0accf428f"

# API for weather

api_url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric'

get_server_information = requests.get(api_url)

print(get_server_information.json())







