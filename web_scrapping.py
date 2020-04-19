import requests
from bs4 import BeautifulSoup
import json


def parse_to_json(raw_info):
    info = []
    for item in raw_info:
        obj_temp = {}
        list_temp = item.split('\n')
        obj_temp['pais'] = list_temp[1]
        obj_temp['nome'] = list_temp[2]
        obj_temp['porcentagem'] = (list_temp[3]).split('%')[0] + "%" #+0,63%97.821 pts
        obj_temp['valor'] = (list_temp[3]).split('%')[1]
        info.append(obj_temp)

    return info

def save_json(data, filename):  # TODO: Colocar em outro arquivo
    with open(filename, "w") as file:
        file.write(json.dumps(data, indent=4))


def ibovespa():
    raw_info = []
    url = 'https://www.infomoney.com.br/ibovespa'
    site = requests.get(url)
    soup = BeautifulSoup(site.text, 'html.parser')
    for indice in soup.findAll(class_="cm-mg-10-t cm-pad-10-b cm-border-b"):
        for li in indice.findAll(id="liStock"):
                raw_info.append(li.get_text())
                print(li.get_text())

    json_data = parse_to_json(raw_info)
    save_json(json_data, 'web_scrapping.json')
