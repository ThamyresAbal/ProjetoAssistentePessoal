import json

import requests

def dados_url():
    with open("chave.json", "r") as configuracao:
        dados_chave = json.load(configuracao)

    url = 'http://api.openweathermap.org/data/2.5/weather?id=3451189&units=metric&lang=pt&appid='\
          + dados_chave['chave_api']

    dados_pagina = requests.post(url, json={'key': 'value'})
    return dados_pagina.json()

def dicionario_clima(content):
    dados_clima = {
        "cidade" : content["name"],
        "temp_min": content["main"]["temp_min"],
        "temp_max": content["main"]["temp_max"],
        "umidade_relativa_do_ar": str(content["main"]["humidity"]),
        "condicao_climatica": content["weather"][0]["description"]
        }
    return dados_clima

def informacao_clima():
    dados_clima = dicionario_clima(dados_url())
    print('**********************************************************')
    print(dados_clima["cidade"])
    print(f'Temperatura Mínima: {dados_clima["temp_min"]}ºC')
    print(f'Temperatura Máxima: {dados_clima["temp_max"]}ºC')
    print(f'Umidade relativa do ar: {dados_clima["umidade_relativa_do_ar"]} %')
    print(f'Condição climática: {dados_clima["condicao_climatica"]}')
    print('**********************************************************')
    gravar_json(dados_clima)

def gravar_json(dados_clima):
    with open('dados_clima.json', 'w') as f:
        json.dump(dados_clima, f, indent= 4)

#informacao_clima()