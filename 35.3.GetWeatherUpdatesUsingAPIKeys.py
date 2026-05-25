import requests

OWN_Endpoint = "https://api.openweathermap.org/data/3.0/onecall"
api_key = "f597280f6ef13321ced41057d5099d56"

weather_params= {
    "lat": 24.860735,
    "lon": 67.001137,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}
response = requests.get(OWN_Endpoint, params=weather_params)
print(response.json())