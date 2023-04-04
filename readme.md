
# Bot do Twitter para Adafruit em Python

Estes são quatro bots do Twitter desenvolvidos em Python que utilizam a API do Adafruit para obter informações e tuitar essas informações automaticamente.
As informações são obtidas através de sensores e relés conectados à microcontroladores ESP32 e ESP8266 que gravam estes dados no Adafruit.

![Dashboard do Adafruit](https://images2.imgbox.com/5e/e8/0phZUHq2_o.jpg)

## Como funciona

Os bots se conectam à API do Adafruit usando a biblioteca `adafruit-io` e buscam informações de feeds especificados. Em seguida, eles formatam as informações em mensagens e publicam essas mensagens no Twitter usando a biblioteca `twython`.
Cada bot tem sua função específica.

![Twitter do projeto](https://images2.imgbox.com/35/a6/EqpvOjyj_o.jpg)

### Luminarias

Esse bot é responsável por ler o estado de duas entradas digitais e postar no Twitter o estado de cada uma delas. O objetivo é monitorar o estado de duas lâmpadas em uma casa.
Existem quatro funções que geram frases para cada situação possível de estado das duas lâmpadas: ligada ou desligada. Para cada lâmpada, há uma função para quando a lâmpada está ligada e outra para quando está desligada.
O código entra em um loop while, que é executado indefinidamente, enquanto o programa está em execução. Dentro do loop, o código lê o estado das duas entradas digitais e as compara com os valores armazenados anteriormente. Se houver uma mudança em um dos estados das lâmpadas, uma mensagem será gerada usando uma das funções de frase e postada no Twitter. O estado anterior das lâmpadas é atualizado após cada comparação para que o loop possa verificar novamente se houve alteração nas lâmpadas.

![enter image description here](https://images2.imgbox.com/02/77/rOc0ROgw_o.jpg)

### UmidadeSoloSamambaia

Este bot executa um loop infinito que checa a umidade da planta a cada hora. Se a umidade for menor que 45%, ele publica um tweet com uma mensagem aleatória pedindo para ser regada. Se a umidade aumentar mais do que 10 unidades em relação à última vez que foi medida, ele publica um tweet de agradecimento por ter sido regada. Se nenhuma dessas condições for atendida, o programa simplesmente imprime a hora atual e uma mensagem "nada acontece, feijoada".
![enter image description here](https://images2.imgbox.com/14/ec/ltJS3I42_o.jpg)

### TemperaturaExterna
A temperatura e umidade externas são coletadas do feed do Adafruit IO e salvas em variáveis, na sequência o programa lê alguns arquivos de texto que guardam as temperaturas e umidades mínimas e máximas, bem como os horários que elas ocorreram (para caso o programa se encerre inesperadamente e o usuário tenha que dispará-lo novamente, ele não perca as informações do dia). Posteriormente o bot checa os feeds do Adafruit a cada 30 minutos e verifica se há alteração em alguma variável, caso haja uma nova umidade ou temperatura máxima ou mínima, um tweet é disparado com esta informação, além dos dados serem armazenados nos arquivos de texto. 
O bot ainda chama a função verificahora() em cada repetição do While para verificar se é 00:00, caso seja o horário mencionado, o bot dispara um tweet com um resumo climático do dia e aguarda até as 01:00 para dar sequência na execução do while.
![enter image description here](https://images2.imgbox.com/cb/71/4p2CWJKK_o.jpg)

### TemperaturaInterna
Funciona de forma similar ao bot anterior, entretanto cada vez que uma nova temperatura máxima ou mínima é registrada, é gerado um novo tweet a partir de uma função que gera uma frase aleatória temática para cada situação.
![enter image description here](https://images2.imgbox.com/fc/b1/qmgJPajy_o.jpg)


## Configuração

Para usar este bot, você precisará das seguintes informações:

-   Chave de acesso e segredo do Twitter para a conta que o bot usará
-   Token de acesso e segredo do Twitter para a conta que o bot usará
-   Chave de acesso da API do Adafruit
-   Nome do feed do Adafruit que o bot irá monitorar

Essas informações devem ser armazenadas em um arquivo `auth.py` na pasta raiz do projeto. Use o arquivo `auth.py` como modelo e substitua as informações com suas próprias chaves e tokens.

## Instalação

1.  Clone este repositório para sua máquina local:

`git clone https://github.com/lulinucs/CasaEsperta.git` 

2.  Navegue até a pasta raiz do projeto e instale as dependências usando o pip:

`cd CasaEsperta
pip install -r requirements.txt` 
    
3.  Execute os bots que desejar:

`python Luminarias.py`
`python UmidadeSoloSamambaia.py`
`python TemperaturaExterna.py`
`python TemperaturaInterna.py`

O bot buscará informações do feed especificado no Adafruit e publicará um tweet com as informações a cada intervalo especificado no arquivo `config.py`.


## Projeto pausado

Infelizmente, devido à falta de tempo, tive que descontinuá-lo por enquanto.
O projeto foi muito importante para o meu aprendizado e desenvolvimento, e espero que tenha sido uma fonte de inspiração para outros makers. Embora o projeto esteja descontinuado, quero enfatizar que continuo comprometido com a minha jornada de criação e que espero retomar o projeto em algum momento.
Obrigado aos 22 seguidores que acompanharam essa jornada no Twitter da Casa Esperta.
