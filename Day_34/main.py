import requests
import os
import datetime as dt

#Endpoints
NUTRI_ENDPOINT = 'https://trackapi.nutritionix.com/v2/natural/exercise'
SHEETY_ENDPOINT = 'https://api.sheety.co/username/project/yoursheet' #Coloque o endpoint da sua conta do sheety (https://sheety.co)

#Variáveis de ambiente
nutri_id = os.environ.get('NUTRI_ID') #https://developer.nutritionix.com
nutri_key = os.environ.get('NUTRI_KEY') #https://developer.nutritionix.com
sheety_token = os.environ.get('SHEETY_TOKEN') # https://sheety.co

#Tempo formatado
today = dt.datetime.now()
formated_date = today.strftime('%d/%m/%Y')
formated_time = today.strftime('%H:%M:%S')

#Header de autenticação da api nutritionix
nutri_headers = {
    'x-app-id': nutri_id,
    'x-app-key': nutri_key
}
#Query sobre exercicio com input do usuário utilizando linguagem natural
user_input = str(input('Type what exercises you did today:\n'))
nutri_params = {
    'query': user_input
}
#Faz um request POST com o valor do usuário, retornando o resultado da query.
with requests.post(url=NUTRI_ENDPOINT, headers=nutri_headers, json=nutri_params) as response:
    data = response.json()
    exercise = data['exercises'][0]['name'].title()
    duration = data['exercises'][0]['duration_min']
    calories = data['exercises'][0]['nf_calories']

#Header de autorização
sheety_header = {'Authorization': f'Bearer {sheety_token}'}    
#Formatação para adicionar uma linha na planilha do Google Spredsheets
sheety_params = {
    'workout': {
        'date': str(formated_date),
        'time': str(formated_time),
        'exercise': str(exercise),
        'duration': str(duration),
        'calories': str(calories)
    }
}
#Faz um request POST para adicionar a linha na planilha utilizando api do Sheety
with requests.post(url=SHEETY_ENDPOINT, json=sheety_params, headers=sheety_header) as response:
    data = response.json()
    print(data)