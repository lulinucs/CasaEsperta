#importa as bibliotecas utilizadas

import time #pra trabalhar com horários dos eventos
from datetime import datetime, date #pra trabalhar com datas dos eventos
import emoji #pra tuitar com emojis kkk
import random #pra gerar as frases
from Adafruit_IO import Client, Feed, RequestError #pra comunicar com o serviço Adafruit
from twython import Twython #pra tuitar
import pytz #pra ajustar o fuso horário da biblioteca time

#Dados de acesso da api do AdaFruit



# Importação do arquivo com os dados de autenticação da api do Twitter / os dados ficam em um arquivo a parte
from auth import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret,
    ADAFRUIT_IO_KEY,
    ADAFRUIT_IO_USERNAME
)

aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

#Atribui os emojis
lampada = emoji.emojize(':light_bulb:')
ligada = emoji.emojize(':green_circle:')
apagada = emoji.emojize(':red_circle:')




def init_twython(): #Função que inicia a biblioteca do twitter e retorna uma instância do Twitter logado na API
    """Initializes Twython connection using the imported keys and tokens"""
    twitter = Twython(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
    )
    return twitter

#recebe o status das chaves de cada lâmpada do Adafruit
digital = aio.feeds('digital')
digital2 = aio.feeds('digital2')

#Funções que geram a a frase que será tuitada de acordo com cada situação

def lumi_joao_acesa():
 p1 = ['A luminária', 'A lâmpada', 'A luz'] #p1 a p4 são listas com sinônimos
 p2 = [' do João', ' do querido amigo João', ' do João da Comunave', ' do cumpadi João']
 p3 = [' está', ' tá']
 p4 = [' ligada.', ' acesa.', ' ativa.', ' iluminando.']
 frase = ligada + lampada + ' ' + random.choice(p1) + random.choice(p2) + random.choice(p3) + random.choice(p4) #A frase é gerada com 2 emojis "ligada e lâmpada" + um termo aleatório de cada p (p1 a p4)
 return frase #retorna a frase criada acima

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


dataold = aio.receive(digital.key) #atribui o valor da chave digital em dataold (para comparar mais tarde)
dataold2 = aio.receive(digital2.key) #atribui o valor da chave digital2 em dataold2 (para comparar mais tarde)

while True: #repete eternamente
        data = aio.receive(digital.key) #recebe o status da chave digital 
        data2 = aio.receive(digital2.key) #recebe o status da chave digital2
        data_atual = date.today() #armazena a data atual
        hora_atual = datetime.now(pytz.timezone('America/Sao_Paulo')).strftime('%H:%M') #armazena a hora atual (com ajuste do fuso horário)
        data_atual = str(data_atual) #converte a data para string
        if int(data.value) != int(dataold.value): #compara se data e dataold são diferentes (houve alteração no estado da chave digital1?)
            time.sleep(10) #aguarda 10 segundos
            if int(data.value) == 0: #o valor da chave digital é igual a zero?
                print('Luz do joão apagada!') #printa no console
                message = lumi_joao_apagada() #message chama a função lumi_joao_apagada e recebe a frase gerada lá
                twitter = init_twython() #chama a função de logar no twitter
                time.sleep(5) #espera 5 segundos
                twitter.update_status(status=message) #publica o conteúdo de message no twitter
                log = open('logs.txt', 'a') #abre o arquivo de logs
                log.write('lumi do joão apagada ' + data_atual + ' ' + hora_atual) #grava informações no log
                log.close() #fecha o arquivo de logs
            elif int(data.value)== 1:  #o valor da chave digital é igual a 1?
                print('Luz do joão acesa!') #printa no console
                message = lumi_joao_acesa() #chama a função de gerar frase para luminária ACESA e armazena a frase em message
                twitter = init_twython() #daqui pra baixo tudo igual até fechar este elif
                time.sleep(5)
                twitter.update_status(status=message)
                log = open('logs.txt', 'a')
                log.write('lumi do joão acesa ' + data_atual + ' ' + hora_atual)
                log.close()
        elif int(data.value) == int(dataold.value): #aqui poderia ser um ELSE ao invés de ELIF (autocrítica mas funciona igual) 
            print('O status não mudou' + data_atual + ' ' + hora_atual) #apenas printa no console que não houve alteração no status da chave digital
        dataold = data #dataold recebe o valor da chave nesta execução para comparar novamente na próxima execução deste laço

        if int(data2.value) != int(dataold2.value): #faz tudo igual só que para a chave digital2
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
        time.sleep(300) #Aguarda 5 minutos antes de executar o While novamente



