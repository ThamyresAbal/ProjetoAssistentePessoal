import json

import requests
from bs4 import BeautifulSoup
def noticias():
    url = 'http://g1.globo.com/ultimas-noticias.html'
    site = requests.get(url).text
    soup = BeautifulSoup(site, 'html.parser')
    lista_obj = []
    for indice in soup.findAll(class_="bastian-feed-item"):
        obj_temp = {}
        obj_temp["titulo"] = indice.find(class_="feed-post-body-title").get_text()
        obj_temp["resumo"] = indice.find(class_="feed-post-body-resumo").get_text()
        lista_obj.append(obj_temp)
        print(f"\u001b[34;1m Noticia: {obj_temp['titulo']}")
        print(f"\u001b[0m Resumo: {obj_temp['resumo']}\n")
    gravar_json(lista_obj)
def gravar_json(lista_obj):
    with open('dados_ultimas_noticias.json', 'w') as f:
        json.dump(lista_obj, f, indent= 4)

