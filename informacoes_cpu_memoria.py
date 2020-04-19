import psutil
import json


def info_cpu():
    print('=' * 30)
    print('       C      P      U')
    print('=' * 30)
    for i in range(5):
        cpu = psutil.cpu_percent(interval=1)
        cpu_freq = psutil.cpu_freq()
        print(f'Percentual de uso : {cpu}')
    print(f'Frequêcnia: {cpu_freq}')
    print('=' * 30)
    gravar_json_cpu(dicionario_cpu())

def dicionario_cpu():
    dados_cpu = {
        "percentual": psutil.cpu_percent(interval=1),
        "frequencia": psutil.cpu_freq()
    }
    return dados_cpu

def gravar_json_cpu(dados_cpu):
    with open('dados_cpu.json', 'w') as f:
        json.dump(dados_cpu, f, indent=4)

def info_memoria():
    print('=' * 35)
    print('     M   E   M   Ó   R   I   A')
    print('=' * 35)
    mem = psutil.virtual_memory()
    # print(mem)
    print(f'Total: {mem[0]}\n'
          f'Usada: {mem[3]}\n'
          f'Livre: {mem[4]}\n'
          f'Percentual de uso: {mem[2]}')
    gravar_json_memoria(dicionario_memoria(mem))

def dicionario_memoria(mem):
    dados_memoria = {
        "total": mem[0],
        "usada": mem[3],
        "livre": mem[4],
        "percentual_uso": mem[2],
    }
    return dados_memoria

def gravar_json_memoria(dados_memoria):
    with open('dados_memoria.json', 'w') as f:
        json.dump(dados_memoria, f, indent=4)
