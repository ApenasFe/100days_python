import requests
import os
from twilio.rest import Client

#Informações do Open Weather API
API_Endpoint = 'https://api.openweathermap.org/data/2.5/forecast'
parameters = {
    'lat': -14.235004,
    'lon': -51.925282,
    'appid': os.environ.get('OWM_API_KEY'),
    'cnt': 4,
}

#Informações da API do Twilio
account_sid = 'ABCDEFG123456789'
auth_token = os.environ.get('AUTH_TOKEN')
twilio_num = '+9999999999' #Sim, o número deve ser em string

#Informação do usuário
user_num = '+9999999999' #Sim, o número deve ser em string

with requests.get(url=API_Endpoint, params=parameters) as r:
    r.raise_for_status()
    data = r.json()

will_rain = False
will_snow = False
for index in range (0, 4):
    weather_id = data['list'][index]['weather'][0]['id']
    if weather_id < 600:
        will_rain = True
    elif weather_id < 700:
        will_snow = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body='Existe uma alta chance de chuva hoje, portanto, não esqueça do seu guarda-chuva!',
        from_=twilio_num,
        to=user_num
    )
elif will_snow:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body='De alguma forma, existe uma chance de neve',
        from_=twilio_num,
        to=user_num
    )
print(message.status)