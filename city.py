import pprint
import requests
from datetime import datetime


class Weather:

    def __init__(self):
        self._city_cache = {}

    def get(self, city):
        if city in self._city_cache:
            return self._city_cache[city]
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}\
        &units=metric&APPID=320d7d15ce9a97364305254fa0f2e1bf"
        data = requests.get(url).json()
        forecast = []
        forecast_data = data["main"]
        forecast.append(data['name'])
        forecast.append(datetime.utcfromtimestamp(data['dt']).strftime('%Y-%m-%d %H:%M:%S'))
        for day_data in forecast_data:
            if day_data == 'temp':
                forecast.append({
                    "temp": forecast_data['temp']
                })
            elif day_data == 'temp_min':
                forecast.append({
                    "temp_min": forecast_data['temp_min']
                })
            elif day_data == 'temp_max':
                forecast.append({
                    "temp_max": forecast_data["temp_max"]
                     })
        self._city_cache[city] = forecast
        return forecast


class CityInfo:

    def __init__(self, city, forecast_provider=None):
        self.city = city
        self._weather_forecast = forecast_provider or Weather()

    def weather_forecast(self):
        return self._weather_forecast.get(self.city)


def _main():
    weather_forecast = Weather()
    city_info = CityInfo("Minsk",  forecast_provider=weather_forecast)
    forecast = city_info.weather_forecast()
    pprint.pprint(forecast)


if __name__ == "__main__":
    _main()
