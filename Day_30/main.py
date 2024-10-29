import requests
from datetime import datetime
import smtplib
import config
import time

MY_LAT = config.LAT
MY_LONG =  config.LONG

SENDER_EMAIL = config.EMAIL
SENDER_PASSWORD = config.PASSWORD
RECEIVER_EMAIL = config.TARGET_EMAIL

#Função para rastrear o ISS e verificar se está próximo da localização designada
def is_iss_close():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    #Verifica se o ISS está próximo da localização designada.
    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        return True

def is_night_time():
    parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()

    current_hour = datetime.now().hour
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])


    if current_hour <= sunrise or current_hour >= sunset:
        return True

while True:
    time.sleep(60)
    if is_iss_close() and is_night_time():
        print('O ISS está por perto!')
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=SENDER_EMAIL, password=SENDER_PASSWORD)
            connection.sendmail(from_addr=SENDER_EMAIL, to_addrs=RECEIVER_EMAIL, msg='Subject:ISS proximo\n\nA Estacao Espacial Internacional esta por perto!')
    else:
        print('Programa rodando...')