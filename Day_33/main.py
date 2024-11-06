import requests
import os
from twilio.rest import Client
import time

#Constante com a empresa selecionada
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

#Variáveis de ambiente com as keys necessárias
alpha_key = os.environ.get('ALPHA_KEY') #https://www.alphavantage.co
news_key = os.environ.get('NEWS_KEY') #https://newsapi.org
account_sid = os.environ.get('ACC_SID') #https://www.twilio.com/en-us
auth_token = os.environ.get('AUTH_TOKEN') #https://www.twilio.com/en-us

#Dados do remetente e destinatário do twilio
sender_number = '+999999999'
receiver_number = '+99999999'

#Acessa e retorna os dados da api do alphavantage
alpha_parameters = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': STOCK,
    'apikey': alpha_key
}
with requests.get(url='https://www.alphavantage.co/query', params=alpha_parameters) as r:
    data = r.json()

#retorna o valor de fechamento dos dois ultimos dias
count = 0
close_list = []
for date in data['Time Series (Daily)']:
    if count <= 1:
        close_value = data['Time Series (Daily)'][date]['4. close']
        close_list.append(float(close_value))
        count += 1
    else:
        break
#Calcula a variação entre esses dois dias
def variation():
    return (close_list[1] - close_list[0]) / close_list[0] * 100
stock_variation = round(variation(), 2)

#Ajusta o símbolo da variação de acordo com a variação
stock_sign = ''
if stock_variation < 0:
    stock_sign = '🔻'
elif stock_variation > 0:
    stock_sign = '🔺'
else:
    stock_sign = ''

#Acessa e retorna os dados da api da newsapi
news_parameters = {
    'q': COMPANY_NAME,
    'pageSize': 3,
    'apiKey': news_key
}
with requests.get(url='https://newsapi.org/v2/everything', params=news_parameters) as r:
    data = r.json()
#Cria uma lista com os 3 artigos mais recentes retornado pela API
article_list = []
for index in range (0, 3):
    headline = data['articles'][index]['title']
    description = data['articles'][index]['description']
    new_article = f'{STOCK}: {stock_variation}%{stock_sign}\nHeadline: {headline}\nDescrição: {description}'
    article_list.append(new_article)

#Conecta em sua conta do twilio para enviar os artigos ao número utilizando API do twilio
client = Client(account_sid, auth_token)
if stock_variation <= -5 or stock_variation >= 5:
    for article in article_list:
        message = client.messages.create(
            from_=str(sender_number), #Número do remetente
            to=str(receiver_number), #Número do destinatário
            body=f'{article}'
)
        print(message.status) #Caso retorne "queued" signica que a mensagem foi enviada
        time.sleep(5)