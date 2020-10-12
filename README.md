# Detecção de moedas de um real com visão computacional

## Introdução
Esse projeto foi construído como trabalho acadêmico do componente curricular Processamento Digital de Sinais 2 do Instituto Federal de Santa Catarina. A ideia era mostrar uma aplicação envolvendo algum tipo de processamento digital em imagens ou em audio que tivesse uma determinada complexidade agregada.  
  
Nesse sentido foi desenvolvido um script que usa visão computacional para reconhecer moedas de um real em imagens fornecidas pelo usuário. O script pode ser rodado de maneira direta na pasta scripts/img_analysis.py com o comando ``python img_analysis.py`` ou a partir do notebook jupyter no arquivo detector_moedas.ipynb.

Para alterar o nome do arquivo de origem no arquivo .py, altere o valor da variável filename. No arquivo .ipynb, altere o nome do arquivo na chamada da função count_moedas.

## Libs
### ImageAI
Teve o papel de operacionalizar o uso da inteligência artificial para o reconhecimento das imagens. A parte foram desenvolvidos scripts para a criação do modelo, aferimento de desempenho e teste preliminar de funcionamento.  
  
A biblioteca funciona muito bem para o caso de uso do input ser um arquivo e o output ser outro arquivo. Tentei fazer via array numpy a entrada/saída porém é provável que algum metadado não tenha sido lido adequadamente no processo. O resultado dessa tentativa eram imagens cujas coordenadas das moedas não correspondiam a realidade (fora de orientação). 

Os recursos diposnibilizados para criação de models, avaliação de performance e teste preliminar podem ser encontrados [nesse link](https://imageai.readthedocs.io/en/latest/customdetection/).  

Com relação a lib, não houve dificuldade de trabalho após o ambiente ter sido definido. A documentação não é tão contundente nisso, porém é necessário que o python seja a versão 3.6.x. De resto, seguindo religiosamente a documentação, a *developer experience* é bem boa.  
  
### PIL
PIL é uma das bibliotecas mais tranquilas de trabalhar dentro do Python. É uma das principais naquilo que faz, que é operacionalização de imagens. É com ela que é possível abrir uma imagem, cortar, inserir formas geométricas, texto e etc. Nesse projeto ela é usada para abrir o arquivo resultado das operações com a ImageAI e posterior inserção das labels indicando os objetos encontrados.  


```python
from imageai.Detection.Custom import CustomObjectDetection
from PIL import Image, ImageDraw, ImageFont
```

    Using TensorFlow backend.


## Downloads adicionais
### yolo.h5
Para baixar o arquivo yolo.h5, acesse [esse link](https://github.com/OlafenwaMoses/ImageAI/releases/tag/1.0/). Esse download é necessário caso haja interesse em criar um novo modelo.  
  
## Funções
  
### trasnform_points_rect(width: number, heigh: number, points: list),
### transform_points_text(width: number, heigh: number, points: list)
Durante o desenvolvimento foi tentado trabalhar com as imagens em forma de arrays, de maneira a operacionalizar apenas uma abertura de arquivo e um salvamento. No entanto, foi percebido que dependendo da foto, as labels e caixas, que são usadas para destacar os elementos, ficavam em uma orientação diferente da orientação da imagem original. A princípio se pensou que isso era um fenômeno comum a todas as imagens, sendo assim utilizada essa função como maneira de corrigir isso.  
  
Mais tarde, dado que as funções não resolveram o problema, foi mudada a abordagem de trabalho para a que segue:
- Passa-se a referência do arquivo para a lib ImageAI;
- ImageAI abre esse arquivo, faz as detecções e cria outro arquivo;
- É aberto o arquivo gerado pela lib ImageAI, pego o retorno da função de deteção e feitas as marcações necessárias
- Salva a imagem.
  
Seria notadamente melhor fazer isso com apenas uma abertura de arquivo e apenas um salvamento (ou criação), como foi dito anteriormente. Essa abordagem tem uma pequena degradação de desempenho por conta do procedimento descrito, mas não é nada que inviabilize a aplicação.


```python
def transform_points_rect(w, h, points):
    return [points[0], points[1], points[2], points[3]]

def transform_points_text(w, h, points):
    return [points[0], points[1]-130]
```

### find_real(path_in, path_out, filename)
Essa função é o âmago de todo o trabalho. O procedimento de trabalho com relação as imagens foi narrado anteriormente. Aqui vou me ater as minúcias dessa função.  
  
De início se cria o objeto para realizar todas as operações envolvendo o modelo de visão computacional e deteção dos objetos. Na sequência é definido um modelo de referência, pois o modelo que criei foi feito em cima do modelo YOLOv3, dado que uma criação de um modelo em cima de um modelo já existente entrega melhores resultados.


```python
def find_real(path_in, path_out, filename):
    detector = CustomObjectDetection()
    detector.setModelTypeAsYOLOv3()
    detector.setModelPath("./models/modelo_moedas_igor.h5")
    detector.setJsonPath("./models/detection_config.json")
    detector.loadModel()
    
    detections = detector.detectObjectsFromImage(
        input_image=path_in+filename, 
        output_image_path=path_out+filename,
        minimum_percentage_probability=40
    )
    
    im_out = Image.open(path_out+filename)
    w,h = im_out.size
    draw = ImageDraw.Draw(im_out)
    font = ImageFont.truetype("./fonts/roboto.ttf", 80)
    for detection in detections:
        points_rect = transform_points_rect(w,h,detection["box_points"])
        draw.rectangle(points_rect, width=20)
        points_text = transform_points_text(w,h,detection["box_points"])
        draw.text(points_text, "Um real",(255,255,255),font=font)
    im_out.save(path_out+filename, "JPEG")
    return len(detections)
```


```python
path_in = "./images_in/"
path_out = "./images_out/"

filenames = [
    "real-1.jpg",
    "real-2.jpg",
    "real-3.jpg",
    "real-4.jpg",
    "real-5.jpg",
    "real-6.jpg",
    "real-7.jpg",
    "real-8.jpg",
    "real-9.jpg",
    "real-10.jpg",
    "real-11.jpg",
    "real-12.jpg",
    "real-13.jpg"
]

for filename in filenames:
    count_moedas = find_real(path_in, path_out, filename)
    print(filename + ": " + str(count_moedas) + " moedas")
    

```

    WARNING:tensorflow:From /Users/igordebastiani/.pyenv/versions/3.7.6/lib/python3.7/site-packages/tensorflow/python/framework/op_def_library.py:263: colocate_with (from tensorflow.python.framework.ops) is deprecated and will be removed in a future version.
    Instructions for updating:
    Colocations handled automatically by placer.
    real-1.jpg: 1 moedas
    real-2.jpg: 2 moedas
    real-3.jpg: 3 moedas
    real-4.jpg: 2 moedas
    real-5.jpg: 2 moedas
    real-6.jpg: 3 moedas
    real-7.jpg: 3 moedas
    real-8.jpg: 1 moedas
    real-9.jpg: 3 moedas
    real-10.jpg: 3 moedas
    real-11.jpg: 3 moedas
    real-12.jpg: 4 moedas
    real-13.jpg: 2 moedas


## Um pouco sobre visão computacional
A biblioteca ImageAI vem com a ideia de facilitar o uso/criação de modelos para visão computacional, por isso é bastante simplificado operar a partir dela. Em uma operação mais tradicional, para uso de redes neurais, seria utilizado a biblioteca Tensorflow de maneira direta, que oferece bem mais parametrizações e controle sobre o processo. 
  
O processo aqui desenvolvido requeriu a criação de um modelo do zero a partir de um dataset, de minha autoria, de 250 fotos de moedas de um real e outras mais, sendo o objeto de interesse as moedas de um real. Para classificar as imagens, a fim de fornecer os insumos necessários a biblioteca ImageAI, foi utilizado um script python chamado [labelImg](https://github.com/tzutalin/labelImg).  
  
Uma vez classificadas as imagens, iniciou-se o processo de treinamento do modelo. Como foi dito anteriormente, o ImageAI veio com a ideia de facilitar a vida no que diz respeito a visão computacional, logo, poucos parâmetros precisaram ser fornecidos a função de treinamento. Foram eles:
- Caminho do modelo pré-treinado (foi utilizado modelo YoLoV3);
- Nome da coleção (o nome escolhido foi 1real);
- Número de experimentos.
  
O número de experimentos é o mesmo que o número de EPOCHs, no entanto ao definir como "número de experimentos" e não epochs, se especula que o ImageAI na realidade faça uma série de experimentos mudando os parâmetros de entrada que normalmente seriam fornecidos pelo usuário caso estivesse sendo feito uso direto do Tensorflow.  
O resultado dessa função de treinamento é uma coleção de modelos de "numero de experimentos" modelos.  
Para treinar o modelo existem duas pastas, uma de treino e outra de validação. A de validação é utilizada, posteriormente, para validar a qualidade do modelo. Uma vez que todos os experimentos que fiz (30) estavam concluídos, fiz a avaliação de performance, em que, dentre as opções, a  mais performática tinha precisão de 87%. Uma precisão tida como satisfatória, segundo referências.

## Conclusões
O modelo apresentou um resultado muito interessante para um dataset de apenas 250 imagens. Nas imagens testadas existem falsos positivos e falsos negativos, mas ambos em minoria. Em imagens "padrão" onde não há elementos em um fundo desfocado e há uma distribuição homogêna de luz, a detecção é bem mais precisa. De qualquer modo a ideia foi criar um modelo e ver como a detecção de moedas via rede neural funcionaria e possíveis pontos de melhoria.

## Mapa do repositório
Na raiz temos o notebook jupyter com essa mesma explicação e código rodável. Na pasta scripts temos o mesmo conteúdo porém aplicados em sripts. Na pasta model, o modelo propriamente dito. Por fim, as pastas imgs_in e imgs_out, que representam as imagens de entrada e de saída.
