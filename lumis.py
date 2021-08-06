import time
from datetime import datetime, date
import emoji
import random
from Adafruit_IO import Client, Feed, RequestError
from twython import Twython
import pytz

ADAFRUIT_IO_KEY = '***'
ADAFRUIT_IO_USERNAME = '***'
aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

# Importação do arquivo com os dados de autenticação na aplicação Twitter
from auth import (
 consumer_key,
 consumer_secret,
 access_token,
 access_token_secret
)

lampada = emoji.emojize(':light_bulb:')
ligada = emoji.emojize(':green_circle:')
apagada = emoji.emojize(':red_circle:')




def init_twython():
    """Initializes Twython connection using the imported keys and tokens"""
    twitter = Twython(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
    )
    return twitter

digital = aio.feeds('digital')
digital2 = aio.feeds('digital2')

def lumi_joao_acesa():
 p1 = ['A luminária', 'A lâmpada', 'A luz']
 p2 = [' do João', ' do querido amigo João', ' do João da Comunave', ' do cumpadi João']
 p3 = [' está', ' tá']
 p4 = [' ligada.', ' acesa.', ' ativa.', ' iluminando.']
 frase = ligada + lampada + ' ' + random.choice(p1) + random.choice(p2) + random.choice(p3) + random.choice(p4)
 return frase

def lumi_joao_apagada():
 p1 = ['A luminária', 'A lâmpada', 'A luz']
 p2 = [' do João', ' do querido amigo João', ' do João da Comunave', ' do cumpadi João']
 p3 = [' está', ' tá']
 p4 = [' apagada.', ' desligada.', ' desativada.', ' off.']
 frase = apagada + lampada + ' ' + random.choice(p1) + random.choice(p2) + random.choice(p3) + random.choice(p4)
 return frase

def luz_da_sala_acesa():
 p1 = ['A outra lâmpada', 'A outra luz', 'A luz da sala', 'A lâmpada da sala']
 p2 = [' (não a do João)', '(não a luminária do João)']
 p3 = [' está', ' tá', 'ta']
 p4 = [' ligada.', ' acesa.', ' ativa.', ' iluminando.']
 frase = ligada + lampada + ' ' +  random.choice(p1) + random.choice(p2) + random.choice(p3) + random.choice(p4)
 return frase

def luz_da_sala_apagada():
 p1 = ['A outra lâmpada', 'A outra luz', 'A luz da sala', 'A lâmpada da sala']
 p2 = [' (não a do João)', '(não a luminária do João)']
 p3 = [' está', ' tá']
 p4 = [' apagada.', ' desligada.', ' desativada.', ' off.']
 frase = apagada + lampada + ' ' + random.choice(p1) + random.choice(p2) + random.choice(p3) + random.choice(p4)
 return frase


dataold = aio.receive(digital.key)
dataold2 = aio.receive(digital2.key)
while True:
        data = aio.receive(digital.key)
        data2 = aio.receive(digital2.key)
        data_atual = date.today()
        hora_atual = datetime.now(pytz.timezone('America/Sao_Paulo')).strftime('%H:%M')
        data_atual = str(data_atual)
        if int(data.value) != int(dataold.value):
            time.sleep(10)
            if int(data.value) == 0:
                print('Luz do joão apagada!')
                message = lumi_joao_apagada()
                twitter = init_twython()
                time.sleep(5)
                twitter.update_status(status=message)
                log = open('logs.txt', 'a')
                log.write('lumi do joão apagada ' + data_atual + ' ' + hora_atual)
                log.close()
            elif int(data.value)== 1:
                print('Luz do joão acesa!')
                message = lumi_joao_acesa()
                twitter = init_twython()
                time.sleep(5)
                twitter.update_status(status=message)
                log = open('logs.txt', 'a')
                log.write('lumi do joão acesa ' + data_atual + ' ' + hora_atual)
                log.close()
        elif int(data.value) == int(dataold.value):
            print('O status não mudou' + data_atual + ' ' + hora_atual)
        dataold = data

        if int(data2.value) != int(dataold2.value):
            time.sleep(10)
            if int(data2.value) == 0:
                print('Lumi apagada!')
                message = luz_da_sala_apagada()
                twitter = init_twython()
                time.sleep(5)
                twitter.update_status(status=message)
                log = open('logs.txt', 'a')
                log.write('luz da sala apagada ' + data_atual + ' ' + hora_atual)
                log.close()
            elif int(data2.value)== 1:
                print('Lumi acesa!')
                message = luz_da_sala_acesa()
                twitter = init_twython()
                time.sleep(5)
                twitter.update_status(status=message)
                log = open('logs.txt', 'a')
                log.write('luz da sala acesa ' + data_atual + ' ' + hora_atual)
                log.close()
        elif int(data2.value) == int(dataold2.value):
            print('O status não mudou' + data_atual + ' ' + hora_atual)
        dataold = data
        dataold2 = data2
        log = open('logs.txt', 'a')
        log.write('Última execução: ' + data_atual + ' ' + hora_atual + '\n')
        log.close()
        time.sleep(300)



