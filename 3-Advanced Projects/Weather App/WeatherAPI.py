from typing import Final
import requests
import json
from Model import Weather, dt

api_key: Final[str] = 'Your_key'
base_url: Final[str] = 'https://api.openweathermap.org/data/2.5/forecast'

def get_weather(city_name: str, mock: bool = True) -> dict:
    if mock:
        with open('dummy_data.json') as file:
            return json.load(file)
    # request live data
    payload: doct = {'q': city_name, 'appid': api_key, 'units': 'metric'}
    request = requests.get(url=base_url, params=payload)
    data = request.json()
    return data

def get_weather_details(weather: dict) -> list[Weather]:
    days: list[dict] = weather.get('list')
    if not days:
        raise Exception(f'problem eith json: {weather}')

    list_of_weather: list[Weather] = []
    for day in days:
        w: Weather = Weather(date=dt.fromtimestamp(day.get('dt')),
                             details=(details := day.get('main')),
                             temp=details.get('temp'),
                             weather=(weather:= day.get('weather')),
                             description=weather[0].get('description'))
        list_of_weather.append(w)

    return list_of_weather

