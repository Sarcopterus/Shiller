import requests

BOT_TOKEN = "PEGAR_TU_TOKEN_AQUÍ"
CHANNEL_ID = "@nombre_de_tu_canal"  # Ej: @bombucksarmy

def post_message(message: str):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHANNEL_ID,
        "text": message,
        "parse_mode": "Markdown"
    }
    res = requests.post(url, json=payload)
    if res.status_code == 200:
        print("✅ Mensaje enviado a Telegram")
    else:
        print("❌ Error al enviar:", res.text)
