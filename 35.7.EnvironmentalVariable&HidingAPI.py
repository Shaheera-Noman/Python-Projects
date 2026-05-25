import requests
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

OWN_Endpoint = "https://api.openweathermap.org/data/3.0/onecall"
api_key = os.environ.get("f597280f6ef13321ced41057d5099d56")
account_sid = "AC03e579802ac6488747b079789e80e59d"
auth_token = "e75bbf9cd4be39ff34b662050fd2746d"

weather_params= {
    "lat": 24.860735,
    "lon": 67.001137,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}
response = requests.get(OWN_Endpoint, params=weather_params)
response.raise_for_status()
print(response.json())