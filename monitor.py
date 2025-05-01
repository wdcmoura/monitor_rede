import os
import time
import subprocess
import requests
import platform

# Lista de hosts
hosts = [
    {"ip": "192.168.15.1", "name": "Roteador Principal"},
    {"ip": "192.168.15.5", "name": "NVR"},
    {"ip": "192.168.15.50", "name": "FAIL"},
    {"ip": "Google.com", "name": "Google"},

]

# Configuração do Telegram
BOT_TOKEN = 'TOKEN_ID_HERE'
CHAT_ID = 'CHAT_ID_HERE'

def enviar_telegram(mensagem):
    url = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage'
    payload = {
        'chat_id': CHAT_ID,
        'text': mensagem
    }
    try:
        requests.post(url, data=payload)
    except Exception as e:
        print(f"Erro ao enviar mensagem: {e}")

# Inicializa dicionário de falhas e status
falhas = {host["ip"]: 0 for host in hosts}
status_atual = {host["ip"]: True for host in hosts}  # True = online, False = offline



def verificar_ping(ip):
    try:
        sistema = platform.system().lower()

        if sistema == 'windows':
            comando = ['ping', '-n', '1', '-w', '1000', ip]  # 1 tentativa, 1 segundo timeout
        else:
            comando = ['ping', '-c', '1', '-W', '1', ip]     # 1 tentativa, 1 segundo timeout

        resultado = subprocess.run(comando,
                                   stdout=subprocess.DEVNULL,
                                   stderr=subprocess.DEVNULL)

        return resultado.returncode == 0
    except Exception:
        return False


while True:
    for host in hosts:
        ip = host["ip"]
        nome = host["name"]
        online = verificar_ping(ip)

        if online:
            if not status_atual[ip] and falhas[ip] >= 4:
                msg = f"✅ {nome} ({ip}) voltou a responder."
                enviar_telegram(msg)
            falhas[ip] = 0
            status_atual[ip] = True
        else:
            falhas[ip] += 1
            if falhas[ip] == 4 and status_atual[ip]:
                msg = f"❌ {nome} ({ip}) está INACESSÍVEL após 4 tentativas."
                enviar_telegram(msg)
                status_atual[ip] = False

    time.sleep(10)  # Aguarda 10 segundos antes da próxima rodada
