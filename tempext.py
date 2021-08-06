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

tempext = aio.feeds('tempext')
dataext = aio.receive(tempext.key)
tempext = float(dataext.value) // 1
tempext = int(tempext)

umidadeexterna = aio.feeds('humiext')
umidadeext = aio.receive(umidadeexterna.key)
umiext = float(umidadeext.value)
umiext = int(umiext)

arquivo_tempmaxext = open('/home/ubuntu/venvluli/EC_TemperaturaComLogs/TEMPEXT/tempmaxext.txt', 'r')
tempmaxext = arquivo_tempmaxext.read()
tempmaxext = int(tempmaxext)
arquivo_tempmaxext.close()

arquivo_tempminext = open('/home/ubuntu/venvluli/EC_TemperaturaComLogs/TEMPEXT/tempminext.txt', 'r')
tempminext = arquivo_tempminext.read()
tempminext = int(tempminext)
arquivo_tempminext.close()

arquivo_oldtempext = open('/home/ubuntu/venvluli/EC_TemperaturaComLogs/TEMPEXT/oldtempext.txt', 'r')
oldtempext = arquivo_oldtempext.read()
oldtempext = int(oldtempext)
arquivo_oldtempext.close()

arquivo_umiminext = open('/home/ubuntu/venvluli/EC_TemperaturaComLogs/TEMPEXT/umiminext.txt', 'r')
umiminext = arquivo_umiminext.read()
umiminext = float(umiminext)
arquivo_umiminext.close()

arquivo_umimaxext = open('/home/ubuntu/venvluli/EC_TemperaturaComLogs/TEMPEXT/umimaxext.txt', 'r')
umimaxext = arquivo_umimaxext.read()
umimaxext = float(umimaxext)
arquivo_umimaxext.close()

arquivo_horamaxext = open('/home/ubuntu/venvluli/EC_TemperaturaComLogs/TEMPEXT/horamaxext.txt', 'r')
horamaxext = arquivo_horamaxext.read()
arquivo_horamaxext.close()

arquivo_horaminext = open('/home/ubuntu/venvluli/EC_TemperaturaComLogs/TEMPEXT/horaminext.txt', 'r')
horaminext = arquivo_horaminext.read()
arquivo_horaminext.close()

arquivo_horaumimaxext = open('/home/ubuntu/venvluli/EC_TemperaturaComLogs/TEMPEXT/horaumimaxext.txt', 'r')
horaumimaxext = arquivo_horaumimaxext.read()
arquivo_horaumimaxext.close()

arquivo_horaumiminext = open('/home/ubuntu/venvluli/EC_TemperaturaComLogs/TEMPEXT/horaumiminext.txt', 'r')
horaumiminext = arquivo_horaumiminext.read()
arquivo_horaumiminext.close()

termometro = emoji.emojize(':thermometer:')
gota = emoji.emojize(':cityscape:')
resumo1 = emoji.emojize(':window:')
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

def random_dados():
    p1 = ['Tá ', 'Faz ', 'Agora tá ']
    p2 = ['ºC e a umidade é de ', 'ºC e a umidade relativa do ar é ', 'ºC e a umidade do ar é ']
    p3 = [' lá fora.', ' na rua.', 'no pátio.', ' no quintal.']
    frase_dados = random.choice(p1) + str(tempext) + random.choice(p2) + str(umiext) + str('%') + random.choice(p3)
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
def resetmaxmin():
    global tempmaxext
    global tempminext
    global umimaxext
    global umiminext
    global horamaxext
    global horaminext
    global horaumimaxext
    global horaumiminext
    arquivo_tempmaxext = open('/home/ubuntu/venvluli/EC_TemperaturaComLogs/TEMPEXT/tempmaxext.txt', 'w')
    arquivo_tempminext = open('/home/ubuntu/venvluli/EC_TemperaturaComLogs/TEMPEXT/tempminext.txt', 'w')
    arquivo_umiminext = open('/home/ubuntu/venvluli/EC_TemperaturaComLogs/TEMPEXT/umiminext.txt', 'w')
    arquivo_umimaxext = open('/home/ubuntu/venvluli/EC_TemperaturaComLogs/TEMPEXT/umimaxext.txt', 'w')
    arquivo_horamaxext = open('/home/ubuntu/venvluli/EC_TemperaturaComLogs/TEMPEXT/horamaxext.txt', 'w')
    arquivo_horaminext = open('/home/ubuntu/venvluli/EC_TemperaturaComLogs/TEMPEXT/horaminext.txt', 'w')
    arquivo_horaumimaxext = open('/home/ubuntu/venvluli/EC_TemperaturaComLogs/TEMPEXT/horaumimaxext.txt', 'w')
    arquivo_horaumiminext = open('/home/ubuntu/venvluli/EC_TemperaturaComLogs/TEMPEXT/horaumiminext.txt', 'w')
    arquivo_tempmaxext.write('0')
    arquivo_tempminext.write('100')
    arquivo_umiminext.write('100')
    arquivo_umimaxext.write('0')
    arquivo_horamaxext.write('0')
    arquivo_horaminext.write('0')
    arquivo_horaumimaxext.write('0')
    arquivo_horaumiminext.write('0')
    arquivo_tempmaxext.close()
    arquivo_tempminext.close()
    arquivo_umiminext.close()
    arquivo_umimaxext.close()
    arquivo_horamaxext.close()
    arquivo_horaminext.close()
    arquivo_horaumimaxext.close()
    arquivo_horaumiminext.close()

    arquivo_tempminext = open('/home/ubuntu/venvluli/EC_TemperaturaComLogs/TEMPEXT/tempminext.txt', 'r')
    tempminext = arquivo_tempminext.read()
    tempminext = int(tempminext)
    arquivo_tempminext.close()

    arquivo_oldtempext = open('/home/ubuntu/venvluli/EC_TemperaturaComLogs/TEMPEXT/oldtempext.txt', 'r')
    oldtempext = arquivo_oldtempext.read()
    oldtempext = int(oldtempext)
    arquivo_oldtempext.close()

    arquivo_umiminext = open('/home/ubuntu/venvluli/EC_TemperaturaComLogs/TEMPEXT/umiminext.txt', 'r')
    umiminext = arquivo_umiminext.read()
    umiminext = float(umiminext)
    arquivo_umiminext.close()

    arquivo_umimaxext = open('/home/ubuntu/venvluli/EC_TemperaturaComLogs/TEMPEXT/umimaxext.txt', 'r')
    umimaxext = arquivo_umimaxext.read()
    umimaxext = float(umimaxext)
    arquivo_umimaxext.close()

    arquivo_horamaxext = open('/home/ubuntu/venvluli/EC_TemperaturaComLogs/TEMPEXT/horamaxext.txt', 'r')
    horamaxext = arquivo_horamaxext.read()
    arquivo_horamaxext.close()

    arquivo_horaminext = open('/home/ubuntu/venvluli/EC_TemperaturaComLogs/TEMPEXT/horaminext.txt', 'r')
    horaminext = arquivo_horaminext.read()
    arquivo_horaminext.close()

    arquivo_horaumimaxext = open('/home/ubuntu/venvluli/EC_TemperaturaComLogs/TEMPEXT/horaumimaxext.txt', 'r')
    horaumimaxext = arquivo_horaumimaxext.read()
    arquivo_horaumimaxext.close()

    arquivo_horaumiminext = open('/home/ubuntu/venvluli/EC_TemperaturaComLogs/TEMPEXT/horaumiminext.txt', 'r')
    horaumiminext = arquivo_horaumiminext.read()
    arquivo_horaumiminext.close()


def verificahora():
    hora_string = datetime.now(pytz.timezone('America/Sao_Paulo')).strftime('%H:%M')
    hora = int(hora_string.split(':')[0])
    if hora == 0:
        tweet = f'{resumo1} RESUMO CLIMÁTICO EXTERNO DO DIA {resumo2}\n{termometro} Temperatura máxima lá fora: {maximo} {tempmaxext}ºC às {rel1} {horamaxext}\n{termometro} Temperatura mínima lá fora: {minimo} {tempminext}ºC às {rel2} {horaminext}\n{gota} Umidade máxima lá fora: {maximo} {umimaxext}% às {rel3} {horaumimaxext}\n{gota} Umidade mínima lá fora: {minimo} {umiminext}% às {rel4} {horaumiminext}'
        twitter = init_twython()
        time.sleep(5)
        twitter.update_status(status=tweet)
        print(tweet)
        resetmaxmin()
        time.sleep(3600)


while True:
    umidadeexterna = aio.feeds('humiext')
    umidadeext = aio.receive(umidadeexterna.key)
    umiext = float(umidadeext.value)
    umiext  = int(umiext)

    tempext = aio.feeds('tempext')
    dataext = aio.receive(tempext.key)
    tempext = float(dataext.value) // 1
    tempext = int(tempext)

    hora_atual = datetime.now(pytz.timezone('America/Sao_Paulo')).strftime('%H:%M')

    if tempext > tempmaxext:
        tempmaxext = tempext
        horamaxext = hora_atual

        tempmaxexts = str(tempmaxext)
        arquivo_tempmaxext = open("/home/ubuntu/venvluli/EC_TemperaturaComLogs/TEMPEXT/tempmaxext.txt", "w")
        arquivo_tempmaxext.write(tempmaxexts)
        arquivo_tempmaxext.close()
        arquivo_horamaxext = open("/home/ubuntu/venvluli/EC_TemperaturaComLogs/TEMPEXT/horamaxext.txt", "w")
        arquivo_horamaxext.write(horamaxext)
        arquivo_horamaxext.close()

        print(f'Nova temperatura máxima externa registrada: {tempmaxext}ºC | {hora_atual}')

        random = random_dados()
        tweet = f'Nova temperatura máxima externa do dia registrada | {random}'
        twitter = init_twython()
        time.sleep(5)
        twitter.update_status(status=tweet)

    if tempext < tempminext:
        tempminext = tempext
        horaminext = hora_atual

        tempminexts = str(tempminext)
        arquivo_tempminext = open("/home/ubuntu/venvluli/EC_TemperaturaComLogs/TEMPEXT/tempminext.txt", "w")
        arquivo_tempminext.write(tempminexts)
        arquivo_tempminext.close()
        arquivo_horaminext = open("/home/ubuntu/venvluli/EC_TemperaturaComLogs/TEMPEXT/horaminext.txt", "w")
        arquivo_horaminext.write(horaminext)
        arquivo_horaminext.close()

        print(f'Nova temperatura externa mínima registrada: {tempminext}ºC | {hora_atual}')

        random = random_dados()
        tweet = f'Nova temperatura mínima externa do dia registrada | {random}'
        twitter = init_twython()
        time.sleep(5)
        twitter.update_status(status=tweet)

    if umiext > umimaxext:
        umimaxext = umiext
        horaumimaxext = hora_atual

        umimaxexts = str(umimaxext)
        arquivo_umimaxext = open("/home/ubuntu/venvluli/EC_TemperaturaComLogs/TEMPEXT/umimaxext.txt", "w")
        arquivo_umimaxext.write(umimaxexts)
        arquivo_umimaxext.close()
        arquivo_horaumimaxext = open("/home/ubuntu/venvluli/EC_TemperaturaComLogs/TEMPEXT/horaumimaxext.txt", "w")
        arquivo_horaumimaxext.write(horaumimaxext)
        arquivo_horaumimaxext.close()

        print(f'Nova umidade relativa do ar externa máxima registrada: {umimaxext}% | {hora_atual}')

        random = random_dados()
        tweet = f'Nova umidade relativa do ar externa máxima do dia registrada | {random}'
        twitter = init_twython()
        time.sleep(5)
        twitter.update_status(status=tweet)

    if umiext < umiminext:
        umiminext = umiext
        horaumiminext = hora_atual

        umiminexts = str(umiminext)
        arquivo_umiminext = open("/home/ubuntu/venvluli/EC_TemperaturaComLogs/TEMPEXT/umiminext.txt", "w")
        arquivo_umiminext.write(umiminexts)
        arquivo_umiminext.close()
        arquivo_horaumiminext = open("/home/ubuntu/venvluli/EC_TemperaturaComLogs/TEMPEXT/horaumiminext.txt", "w")
        arquivo_horaumiminext.write(horaumiminext)
        arquivo_horaumiminext.close()

        print(f'Nova umidade relativa do ar externa mínima registrada: {umiminext}% | {hora_atual}')

        random = random_dados()
        tweet = f'Nova umidade relativa do ar externa mínima do dia registrada | {random}'
        twitter = init_twython()
        time.sleep(5)
        twitter.update_status(status=tweet)

    verificahora()
    resumoparcial = f'{resumo1} RESUMO PARCIAL DO DIA {resumo2}\n{termometro} Temperatura máxima: {maximo} {tempmaxext}ºC às {rel1} {horamaxext}\n{termometro} Temperatura mínima: {minimo} {tempminext}ºC às {rel2} {horaminext}\n{gota} Umidade máxima: {maximo} {umimaxext}% às {rel3} {horaumimaxext}\n{gota} Umidade mínima: {minimo} {umiminext}% às {rel4} {horaumiminext}\n'
    data_atual = date.today()
    resumo_logext = f'RESUMO PARCIAL EXTERNO: {data_atual} {hora_atual} \n Temperatura máxima: {tempmaxext}ºC às  {horamaxext}\n Temperatura mínima: {tempminext}ºC às  {horaminext}\n Umidade máxima:  {umimaxext}% às  {horaumimaxext}\n Umidade mínima:  {umiminext}% às  {horaumiminext}\n {random_dados()}\n\n'
    print('##################################################################')
    print(resumoparcial)
    print(random_dados())
    print('##################################################################')
    print(' ')
    print(' ')
    logsext = open('/home/ubuntu/venvluli/EC_TemperaturaComLogs/TEMPEXT/logsext.txt', 'a')
    logsext.write(resumo_logext)
    logsext.close()
    time.sleep(1800)
