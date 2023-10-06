import requests


def get_weather_data(api_key, city):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    print(url)
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None


def get_temperature(data):
    if 'main' in data:
        return data['main']['temp']
    else:
        return None
