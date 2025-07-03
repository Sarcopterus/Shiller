import random
import time
import schedule
from datetime import datetime
from message_generator import generate_message
from publisher import post_message  # Asegúrate de que tenga el TOKEN correcto

def generate_and_send() -> None:
    """Generate a random-toned shill message and post it to Telegram with timestamp."""
    tone = random.choice(["hype", "warning", "mystic"])
    message = generate_message(tone)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print("-" * 26)
    print(f"[{timestamp}] [BOMBUCKS SHILL] 🚨")
    print(message)
    print("-" * 26)
    post_message(message)

# Schedule postings every 10 minutes
schedule.every(10).minutes.do(generate_and_send)

if __name__ == "__main__":
    print("🚀 BOMBUCKS SHILL BOT ACTIVATED")
    generate_and_send()  # Primera vez
    while True:
        schedule.run_pending()
        time.sleep(1)
