import pandas as pd
import datetime as dt
import random
import smtplib
import os

#Carrega o arquivo CSV e o formata para um Dataframe
CSV_PATH = '100days_python/Day_29/birthdays.csv'
dataset = pd.read_csv(CSV_PATH)
df = pd.DataFrame(dataset)

#Captura o tempo atual do computador
current_time = dt.datetime.now()
month = current_time.month
day = current_time.day

#Escolhe um arquivo aleatório do diretório
TXT_PATH = '100days_python/Day_29/letter_templates'
letter_files = os.listdir(TXT_PATH)
choosen_letter = random.choice(letter_files)

#Dados do remetente
sender_email = 'yourtest@mail.com'
sender_password = 'yourpassword'

#Itera sobre o dataframe
for index, row in df.iterrows():
    b_name = row.values[0]
    b_email = row.values[1]
    b_month = row.values[3]
    b_day = row.values[4]
    #Caso o dia e mês do aniversáriante seja o mesmo do tempo atual, escolhe uma mensagem aleatória, conecta e envia um email pelo gmail para o aniversariante.
    if b_month == month and b_day == day:
        with open(f'100days_python/Day_29/letter_templates/{choosen_letter}', 'r') as file:
            content = file.read()
            formated_msg = content.replace('[NAME]', b_name)
        with smtplib.SMTP('smtp.gmail.com', 587) as mail_connection:
            mail_connection.starttls()
            mail_connection.login(user=sender_email, password=sender_password)
            mail_connection.sendmail(
            from_addr=sender_email, 
            to_addrs=b_email, 
            msg=f'Subject: Happy birthday!\n\n{formated_msg}')