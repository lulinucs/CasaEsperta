import time
import pytz
import random
import emoji
from datetime import datetime, date
from Adafruit_IO import Client, Feed, RequestError
from twython import Twython


from auth import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

ADAFRUIT_IO_KEY = '***'
ADAFRUIT_IO_USERNAME = '***'
aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

temperature = aio.feeds('temperature')
data = aio.receive(temperature.key)
temp = float(data.value) // 1
temp = int(temp)

umidadedoar = aio.feeds('humidity')
umidade = aio.receive(umidadedoar.key)
umi = float(umidade.value)
umi = int(umi)

arquivo_tempmax = open('/home/ubuntu/venvluli/EC_TemperaturaComLogs/tempmax.txt', 'r')
tempmax = arquivo_tempmax.read()
tempmax = int(tempmax)
arquivo_tempmax.close()

arquivo_tempmin = open('/home/ubuntu/venvluli/EC_TemperaturaComLogs/tempmin.txt', 'r')
tempmin = arquivo_tempmin.read()
tempmin = int(tempmin)
arquivo_tempmin.close()

arquivo_oldtemp = open('/home/ubuntu/venvluli/EC_TemperaturaComLogs/oldtemp.txt', 'r')
oldtemp = arquivo_oldtemp.read()
oldtemp = int(oldtemp)
arquivo_oldtemp.close()

arquivo_umimin = open('/home/ubuntu/venvluli/EC_TemperaturaComLogs/umimin.txt', 'r')
umimin = arquivo_umimin.read()
umimin = float(umimin)
arquivo_umimin.close()

arquivo_umimax = open('/home/ubuntu/venvluli/EC_TemperaturaComLogs/umimax.txt', 'r')
umimax = arquivo_umimax.read()
umimax = float(umimax)
arquivo_umimax.close()

arquivo_horamax = open('/home/ubuntu/venvluli/EC_TemperaturaComLogs/horamax.txt', 'r')
horamax = arquivo_horamax.read()
arquivo_horamax.close()

arquivo_horamin = open('/home/ubuntu/venvluli/EC_TemperaturaComLogs/horamin.txt', 'r')
horamin = arquivo_horamin.read()
arquivo_horamin.close()

arquivo_horaumimax = open('/home/ubuntu/venvluli/EC_TemperaturaComLogs/horaumimax.txt', 'r')
horaumimax = arquivo_horaumimax.read()
arquivo_horaumimax.close()

arquivo_horaumimin = open('/home/ubuntu/venvluli/EC_TemperaturaComLogs/horaumimin.txt', 'r')
horaumimin = arquivo_horaumimin.read()
arquivo_horaumimin.close()

termometro = emoji.emojize(':thermometer:')
gota = emoji.emojize(':droplet:')
resumo1 = emoji.emojize(':clipboard:')
resumo2 = emoji.emojize(':bar_chart:')
maximo = emoji.emojize(':upwards_button:')
minimo = emoji.emojize(':downwards_button:')
rel1 = emoji.emojize(':two-thirty:')
rel2 = emoji.emojize(':three-thirty:')
rel3 = emoji.emojize(':eight-thirty:')
rel4 = emoji.emojize(':ten-thirty:')


def init_twython():
    twitter = Twython(
        consumer_key,
        consumer_secret,
        access_token,
        access_token_secret
    )
    return twitter


def random_friopracaralho():  # <=15ºC
    p1 = ['Bota as meia de lã ', 'Coloca as luvinhas ', 'Hoje tá liberado o aquecedor elétrico ', 'Cancela o banho ',
          'Serve o conhaquinho ']
    p2 = ['pois ', 'porque ', 'pq ']
    p3 = ['está frio para um caralho ', 'tá uma friaca do djanho ']
    p4 = ['na Casa Amarela. ', 'na Casinha Amarelinha. ', 'na Casa Amarilla. ', 'na Yellow House. ', 'na Casa Esperta. ', 'aqui na Baia. ']
    frase = random.choice(p1) + random.choice(p2) + random.choice(p3) + random.choice(p4)
    return frase


def random_esfriou_inverno():  # 16ºC a 20ºC
    p1 = ['Pega uma cobertinha ', 'Esquenta a água pro cházinho ', 'Bota um casaquinho ', ]
    p2 = ['pois ', 'porque ', 'pq ']
    p3 = ['esfriou ', 'tá mais friozinho ', 'deu uma esfriadinha ', 'baixou a temperatura ', 'caiu a temperatura ']
    p4 = ['na Casa Amarela. ', 'na Casinha Amarelinha. ', 'na Casa Amarilla. ', 'na Yellow House. ',
          'na Casa Esperta. ', 'aqui na baia. ']
    frase = random.choice(p1) + random.choice(p2) + random.choice(p3) + random.choice(p4)
    return frase


def random_esfriou_verao():  # 21ºC a 26ºC
    p1 = ['Deu uma refrescada ', 'Deu uma refrescadinha ', 'A temperatura caiu um cadinho ', 'Esfriou mas nem tanto ']
    p2 = ['na Casa Amarela. ', 'na Casinha Amarelinha. ', 'na Casa Amarilla. ', 'na Yellow House. ',
          'na Casa Esperta. ', 'aqui na Baia. ']
    frase = random.choice(p1) + random.choice(p2)
    return frase

def random_esfriou_calorpracaralho():  # >26ºC
    p1 = ['Faz muito calor ', 'Tá quente ', 'Tá abafado ', 'Está demasiadamente quente ']
    p2 = ['na Casa Amarela, ', 'na Casinha Amarelinha, ', 'na Casa Amarilla, ', 'na Yellow House, ', 'na Casa Esperta, ', 'aqui na Baia, ']
    p3 = ['mas ', 'porém ', 'entretanto ', 'todavia ', 'contudo ', 'no entanto ']
    p4 = ['a teperatura acaba de baixar um pouquinho. ', 'deu uma refrescada. ', 'Deu uma refrescadinha agora. ',
              'a temperatura caiu um cadinho. ']
    frase = random.choice(p1) + random.choice(p2) + random.choice(p3) + random.choice(p4)

    return frase


def random_esquentou_friopracaralho():  # <=15ºC
    p1 = ['Viva! ', 'Uma alento de esperança! ']
    p2 = ['Esquentou ', 'A temperatura subiu ']
    p3 = ['um pouquinho ', 'um cadinho, ', 'de leve ']
    p4 = ['na Casa Amarela.', 'na Casinha Amarelinha.', 'na Casa Amarilla.', 'na Yellow House.', 'na Casa Esperta.',
          'aqui na Baia.']
    p5 = ['mas ', 'porém ', 'entretanto ', 'todavia ', 'contudo ', 'no entanto ']
    p6 = ['continua ', 'está ', 'tá ', 'permanece ']
    p7 = ['frio para um caralho. ', 'uma friaca do djanho. ']
    frase = random.choice(p1) + random.choice(p2) + random.choice(p3) + random.choice(p4) + random.choice(
        p5) + random.choice(p6) + random.choice(p7)
    return frase


def random_esquentou_inverno():  # 16ºC a 20ºC
    p1 = ['Esquentou ', 'A temperatura subiu ']
    p2 = ['um pouquinho ', 'um cadinho ', 'de leve ']
    p3 = ['na Casa Amarela. ', 'na Casinha Amarelinha. ', 'na Casa Amarilla. ', 'na Yellow House. ',
          'na Casa Esperta. ', 'aqui na Baia. ']
    frase = random.choice(p1) + random.choice(p2) + random.choice(p3)
    return frase


def random_esquentou_verao():  # 21ºC a 26ºC
    p1 = ['Esquentou ', 'A temperatura subiu ']
    p2 = ['na Casa Amarela. ', 'na Casinha Amarelinha. ', 'na Casa Amarilla. ', 'na Yellow House. ',
          'na Casa Esperta. ', 'aqui na Baia. ']
    frase = random.choice(p1) + random.choice(p2)
    return frase


def random_calorpracaralho():  # >26ºC
    p1 = ['Bota a ceva pá gelá, os legumo na brrrrrrasa ', 'Prepara a caipirinha, ', 'Bota o ventilador no 3 ',
          'Enche a piscininha de prástico ']
    p2 = ['pois ', 'porque ', 'pq ']
    p3 = ['esquentou ', 'a temperatura subiu ']
    p4 = ['na Casa Amarela. ', 'na Casinha Amarelinha. ', 'na Casa Amarilla. ', 'na Yellow House. ',
          'na Casa Esperta. ', 'aqui na Baia. ']
    frase = random.choice(p1) + random.choice(p2) + random.choice(p3) + random.choice(p4)
    return frase

def random_dados(temperatura, umidade):
    p1 = ['Tá ', 'Faz ', 'Agora tá ']
    p2 = ['ºC e a umidade é de ', 'ºC e a umidade relativa do ar é ', 'ºC e a umidade do ar é ']
    frase_dados = random.choice(p1) + str(temp) + random.choice(p2) + str(umi) + str('%')
    return frase_dados

'''
def resetmaxmin(tempmax, tempmin, umimin, umimax, horamax, horamin, horaumimax, horaumimin):
    umimin = float(umidade.value) + 50
    umimax = float(umidade.value) - 50
    tempmax = float(data.value) // 1
    tempmax = int(tempmax) - 10
    tempmin = float(data.value) // 1
    tempmin = int(tempmin) + 10
    horamax = datetime.now(pytz.timezone('America/Sao_Paulo')).strftime('%H:%M')
    horamin = datetime.now(pytz.timezone('America/Sao_Paulo')).strftime('%H:%M')
    horaumimax = datetime.now(pytz.timezone('America/Sao_Paulo')).strftime('%H:%M')
    horaumimin = datetime.now(pytz.timezone('America/Sao_Paulo')).strftime('%H:%M')
'''
def resetmaxmin(tempmax, tempmin, umimin, umimax, horamax, horamin, horaumimax, horaumimin):
    arquivo_tempmax = open('/home/ubuntu/venvluli/EC_TemperaturaComLogs/tempmax.txt', 'w')
    arquivo_tempmin = open('/home/ubuntu/venvluli/EC_TemperaturaComLogs/tempmin.txt', 'w')
    arquivo_umimin = open('/home/ubuntu/venvluli/EC_TemperaturaComLogs/umimin.txt', 'w')
    arquivo_umimax = open('/home/ubuntu/venvluli/EC_TemperaturaComLogs/umimax.txt', 'w')
    arquivo_horamax = open('/home/ubuntu/venvluli/EC_TemperaturaComLogs/horamax.txt', 'w')
    arquivo_horamin = open('/home/ubuntu/venvluli/EC_TemperaturaComLogs/horamin.txt', 'w')
    arquivo_horaumimax = open('/home/ubuntu/venvluli/EC_TemperaturaComLogs/horaumimax.txt', 'w')
    arquivo_horaumimin = open('/home/ubuntu/venvluli/EC_TemperaturaComLogs/horaumimin.txt', 'w')
    arquivo_tempmax.write('0')
    arquivo_tempmin.write('100')
    arquivo_umimin.write('100')
    arquivo_umimax.write('0')
    arquivo_horamax.write('0')
    arquivo_horamin.write('0')
    arquivo_horaumimax.write('0')
    arquivo_horaumimin.write('0')
    arquivo_tempmax.close()
    arquivo_tempmin.close()
    arquivo_umimin.close()
    arquivo_umimax.close()
    arquivo_horamax.close()
    arquivo_horamin.close()
    arquivo_horaumimax.close()
    arquivo_horaumimin.close()

def verificahora(tempmax, tempmin, umimax, umimin, horamax, horamin, horaumimax, horaumimin):
    hora_string = datetime.now(pytz.timezone('America/Sao_Paulo')).strftime('%H:%M')
    hora = int(hora_string.split(':')[0])
    if hora == 0:
        tweet = f'{resumo1} RESUMO CLIMÁTICO DO DIA {resumo2}\n{termometro} Temperatura máxima: {maximo} {tempmax}ºC às {rel1} {horamax}\n{termometro} Temperatura mínima: {minimo} {tempmin}ºC às {rel2} {horamin}\n{gota} Umidade máxima: {maximo} {umimax}% às {rel3} {horaumimax}\n{gota} Umidade mínima: {minimo} {umimin}% às {rel4} {horaumimin}'
        twitter = init_twython()
        time.sleep(5)
        twitter.update_status(status=tweet)
        print(tweet)
        resetmaxmin(tempmax, tempmin, umimin, umimax, horamax, horamin, horaumimax, horaumimin)
        exit()
        time.sleep(3600)


while True:
    umidadedoar = aio.feeds('humidity')
    umidade = aio.receive(umidadedoar.key)
    umi = float(umidade.value)
    umi = int(umi)
    temperature = aio.feeds('temperature')
    data = aio.receive(temperature.key)
    temp = float(data.value)
    temp = int(temp)
    hora_atual = datetime.now(pytz.timezone('America/Sao_Paulo')).strftime('%H:%M')
    if temp > tempmax:
        tempmax = temp
        horamax = hora_atual

        tempmaxs = str(tempmax)
        arquivo_tempmax = open("/home/ubuntu/venvluli/EC_TemperaturaComLogs/tempmax.txt", "w")
        arquivo_tempmax.write(tempmaxs)
        arquivo_tempmax.close()
        arquivo_horamax = open("/home/ubuntu/venvluli/EC_TemperaturaComLogs/horamax.txt", "w")
        arquivo_horamax.write(horamax)
        arquivo_horamax.close()

        print(f'Nova temperatura máxima registrada: {tempmax}ºC | {hora_atual}')

    if temp < tempmin:
        tempmin = temp
        horamin = hora_atual

        tempmins = str(tempmin)
        arquivo_tempmin = open("/home/ubuntu/venvluli/EC_TemperaturaComLogs/tempmin.txt", "w")
        arquivo_tempmin.write(tempmins)
        arquivo_tempmin.close()
        arquivo_horamin = open("/home/ubuntu/venvluli/EC_TemperaturaComLogs/horamin.txt", "w")
        arquivo_horamin.write(horamin)
        arquivo_horamin.close()

        print(f'Nova temperatura mínima registrada: {tempmin}ºC | {hora_atual}')

    if umi > umimax:
        umimax = umi
        horaumimax = hora_atual

        umimaxs = str(umimax)
        arquivo_umimax = open("/home/ubuntu/venvluli/EC_TemperaturaComLogs/umimax.txt", "w")
        arquivo_umimax.write(umimaxs)
        arquivo_umimax.close()
        arquivo_horaumimax = open("/home/ubuntu/venvluli/EC_TemperaturaComLogs/horaumimax.txt", "w")
        arquivo_horaumimax.write(horaumimax)
        arquivo_horaumimax.close()

        print(f'Nova umidade relativa do ar máxima registrada: {umimax}% | {hora_atual}')
    if umi < umimin:
        umimin = umi
        horaumimin = hora_atual

        umimins = str(umimin)
        arquivo_umimin = open("/home/ubuntu/venvluli/EC_TemperaturaComLogs/umimin.txt", "w")
        arquivo_umimin.write(umimins)
        arquivo_umimin.close()
        arquivo_horaumimin = open("/home/ubuntu/venvluli/EC_TemperaturaComLogs/horaumimin.txt", "w")
        arquivo_horaumimin.write(horaumimin)
        arquivo_horaumimin.close()

        print(f'Nova umidade relativa do ar mínima registrada: {umimin}% | {hora_atual}')

    if temp < oldtemp:
        if temp <= 15:
            frase = random_friopracaralho()
        elif temp <= 20:
            frase = random_esfriou_inverno()
        else:
            frase = random_esfriou_verao()
        tweet = frase
        tweet_dados = random_dados(temp, umi)
        twitter = init_twython()
        time.sleep(10)
        twitter.update_status(status=tweet + tweet_dados)
        print(f'Esfriou na casa Amarela | Temperatura atual: {int(temp)}ºC | {hora_atual}')
        oldtemp = temp
        oldtemps = str(oldtemp)
        arquivo_oldtemp = open("/home/ubuntu/venvluli/EC_TemperaturaComLogs/oldtemp.txt", "w")
        arquivo_oldtemp.write(oldtemps)
        arquivo_oldtemp.close()

    elif temp > oldtemp:
        if temp <= 15:
            frase = random_esquentou_friopracaralho()
        elif temp <= 20:
            frase = random_esquentou_inverno()
        elif temp <= 26:
            frase = random_esquentou_verao()
        else:
            frase = random_calorpracaralho()
        tweet = frase
        tweet_dados = random_dados(temp, umi)
        twitter = init_twython()
        time.sleep(10)
        twitter.update_status(status=tweet + tweet_dados)
        print(f'Esquentou na casa Amarela | Temperatura atual: {int(temp)}ºC | {hora_atual}')
        oldtemp = temp
        oldtemps = str(oldtemp)
        arquivo_oldtemp = open("/home/ubuntu/venvluli/EC_TemperaturaComLogs/oldtemp.txt", "w")
        arquivo_oldtemp.write(oldtemps)
        arquivo_oldtemp.close()

    else:
        print(f'Temperatura tá igual. | {hora_atual}')
    verificahora(tempmax, tempmin, umimax, umimin, horamax, horamin, horaumimax, horaumimin)
    resumoparcial = f'{resumo1} RESUMO PARCIAL DO DIA {resumo2}\n{termometro} Temperatura máxima: {maximo} {tempmax}ºC às {rel1} {horamax}\n{termometro} Temperatura mínima: {minimo} {tempmin}ºC às {rel2} {horamin}\n{gota} Umidade máxima: {maximo} {umimax}% às {rel3} {horaumimax}\n{gota} Umidade mínima: {minimo} {umimin}% às {rel4} {horaumimin}\n'
    data_atual = date.today()
    resumo_log = f'RESUMO PARCIAL DO DIA: {data_atual} {hora_atual} \n Temperatura máxima: {tempmax}ºC às  {horamax}\n Temperatura mínima: {tempmin}ºC às  {horamin}\n Umidade máxima:  {umimax}% às  {horaumimax}\n Umidade mínima:  {umimin}% às  {horaumimin}\n {random_dados(temp, umi)}\n\n'
    print('##################################################################')
    print(resumoparcial)
    print(random_dados(temp, umi))
    print('##################################################################')
    print(' ')
    print(' ')
    logs = open('/home/ubuntu/venvluli/EC_TemperaturaComLogs/logs.txt', 'a')
    logs.write(resumo_log)
    logs.close()
    time.sleep(1800)
