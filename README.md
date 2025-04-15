# 📡 Monitoramento de Hosts com Alertas via Telegram

Este script monitora o status de conectividade de uma lista de dispositivos (hosts) através de **ping**. Quando um host fica **inacessível** ou volta a **responder**, o sistema envia alertas automaticamente via **Telegram**.

## ✅ Funcionalidades

- Verifica se dispositivos estão online através de `ping`
- Notifica via Telegram quando um host:
  - Falha por 4 tentativas consecutivas
  - Volta a responder após ficar offline
- Compatível com **Linux**, **Windows** e **macOS**

---

## 🛠️ Requisitos

- Python 3.x
- Internet ativa para enviar mensagens via Telegram
- Biblioteca `requests` instalada:

```bash
pip install requests
```

---

## ⚙️ Como configurar

### 1. Edite a lista de hosts a serem monitorados

No início do script, você pode incluir os IPs e nomes dos dispositivos:

```python
hosts = [
    {"ip": "192.168.15.1", "name": "Roteador Principal"},
    {"ip": "192.168.15.5", "name": "NVR"},
    {"ip": "192.168.15.50", "name": "Servidor de Backup"},
]
```

---

### 2. Configure o Bot do Telegram

#### a. Obtenha seu **BOT\_TOKEN**

1. Acesse o Telegram e inicie uma conversa com [@BotFather](https://t.me/BotFather)
2. Crie um novo bot com `/newbot`
3. Copie o token gerado (ex: `123456789:ABCdefGhIjKlmnOPQRstuVWxyZ`)
4. No script, substitua:

```python
BOT_TOKEN = 'TOKEN_ID_HERE'
```

#### b. Obtenha seu **CHAT\_ID**

1. Envie uma mensagem para o seu bot criado
2. Acesse no navegador:
   ```
   https://api.telegram.org/bot<SEU_BOT_TOKEN>/getUpdates
   ```
3. Procure no JSON por:
   ```json
   "chat": {"id": 123456789, ...}
   ```
4. Copie esse número e substitua:

```python
CHAT_ID = 'CHAT_ID_HERE'
```

---

## 🚀 Como executar

Após configurar, salve o script como `monitor.py` e execute com:

```bash
python monitor.py
```

O script irá rodar continuamente, verificando os dispositivos a cada 10 segundos e enviando alertas conforme necessário.

---

## 📂 Exemplo de saída via Telegram

- Quando um host falha 4 vezes seguidas:

  ```
  ❌ NVR (192.168.15.5) está INACESSÍVEL após 4 tentativas.
  ```

- Quando o host volta a responder:

  ```
  ✅ NVR (192.168.15.5) voltou a responder.
  ```

---

## 📄 Licença

Este projeto é de uso livre. Sinta-se à vontade para modificar e melhorar.

---

## 🤝 Contribuições

Contribuições são bem-vindas! Abra um *pull request* ou envie sugestões através de *issues* no repositório.

---

