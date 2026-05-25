import requests
from twilio.rest import Client

# OWN_Endpoint ="https://api.openweathermap.org/data/2.5/onecall"
# api_key = ""
# account_sid = "AC03e579802ac6488747b079789e80e59d"
# auth_token = "e75bbf9cd4be39ff34b662050fd2746d"

# weather_params = {
#     "lat": 37.711079, 
#     "lon": -97.335228, 
#     "appid": api_key, 
#     "exclude": "current minute, daily"
# }

# response = requests.get(OWN_Endpoint, params=weather_params)
# response.raise_for_status()
# weather_data = response.json()
# weather_slice = weather_data["hourly"][:12]

# will_rain = False

# for hour_data in weather_slice:
#     condition_code = hour_data["weather"][0]["id"]









# Download the helper library from https://www.twilio.com/docs/python/install
# import os
# from twilio.rest import Client


# # Find your Account SID and Auth Token at twilio.com/console
# # and set the environment variables. See http://twil.io/secure
account_sid = "AC03e579802ac6488747b079789e80e59d"
auth_token = "e75bbf9cd4be39ff34b662050fd2746d"
client = Client(account_sid, auth_token)

message = client.messages \
    .create(
         body="Congratulations, You're selected for an interview.", 
         from_='+12512903572', 
         to="+923486885985"
     )

print(message.status)