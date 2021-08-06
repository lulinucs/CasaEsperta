import time
import random
import pytz
from datetime import datetime
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

analog = aio.feeds('analog')
data = aio.receive(analog.key)
sede = float(data.value) // 1
sedesami = int(sede)
oldsede =  int(sede)

def init_twython():
    twitter = Twython(
        consumer_key,
        consumer_secret,
        access_token,
        access_token_secret
    )
    return twitter

def frase_sami():
    p1 = ['Little ', 'Lady ', 'Dona ']
    p2 = ['Sami, ', 'Samizinha, ']
    p3 = ['a samambaia, ', 'a planta, ', 'la planta, ', 'a pteridófita, ']
    p4 = ['diz: ', 'says: ', 'habla: ', 'avisa: ', 'mandou avisar: ', 'grita: ', 'implora: ']
    p5 = ['Estou com sede!', 'Tô com sede!', 'Alguém me rega!', 'quelo água .-.', '@babfrnnds, @atenciosmanete VOCÊS ME ODEIAM?']
    frase = random.choice(p1) + random.choice(p2) + random.choice(p3) + random.choice(p4) + random.choice(p5)
    return frase

def agradece_sami():
    p1 = ['Little ', 'Lady ', 'Dona ']
    p2 = ['Sami, ', 'Samizinha, ']
    p3 = ['a samambaia, ', 'a planta, ', 'la planta, ', 'a pteridófita, ']
    p4 = ['diz: ', 'says: ', 'habla: ', 'avisa: ', 'mandou avisar: ', 'grita: ']
    p5 = ['Só agradece ', 'Muito obrigado ', 'Thanks ', 'Valeuzão ', 'Gratidão ']
    p6 = ['pela aguinha ', 'pela água ', 'pelo líquido precioso ']
    p7 = ['meus quiridu!', 'queridos roomies!', 'meus anjos', 'feios!']
    frase = random.choice(p1) + random.choice(p2) + random.choice(p3) + random.choice(p4) + random.choice(p5) + random.choice(p6) + random.choice(p7)
    return frase

while True:
    analog = aio.feeds('analog')
    data = aio.receive(analog.key)
    sede = float(data.value) // 1
    sedesami = int(sede)
    hora_atual = datetime.now(pytz.timezone('America/Sao_Paulo')).strftime('%H:%M')

    if sedesami >= 45:
        twitter = init_twython()
        tweet = frase_sami()
        time.sleep(5)
        print(tweet)
        print(hora_atual)
        twitter.update_status(status=tweet)

    elif oldsede - sedesami >= 10:
        twitter = init_twython()
        tweet = agradece_sami()
        time.sleep(5)
        print(tweet)
        print(hora_atual)
        twitter.update_status(status=tweet)

    else:
        print('nada acontece, feijoada')
        print(hora_atual)

    oldsede = sedesami
    time.sleep(3600)

