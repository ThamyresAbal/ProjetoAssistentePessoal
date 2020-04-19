import subprocess
import json

def youtube():
    url = 'https://www.youtube.com/playlist?list=PLHz_AreHm4dm6wYOIW20Nyg12TAjmMGT-'
    subprocess.Popen(f'start chrome /new-tab {url}', shell=True)
    gravar_json(dicionario_web(url))

def dicionario_web(info_url):
    dados_webbrowser = {
        "url": info_url
    }
    return dados_webbrowser

def gravar_json(dados_webbrowser):
    with open('dados_webbrowser.json', 'w') as f:
        json.dump(dados_webbrowser, f, indent= 4)
