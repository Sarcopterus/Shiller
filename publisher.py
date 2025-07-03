import random
import time
import schedule
from datetime import datetime
from message_generator import generate_message


def post_message() -> None:
    """Generate a random-toned shill message and print it with timestamp."""
    tone = random.choice(["hype", "warning", "mystic"])
    message = generate_message(tone)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print("-" * 26)
    print(f"[{timestamp}] [BOMBUCKS SHILL] 🚨")
    print(message)
    print("-" * 26)


# Schedule postings every 10 minutes
schedule.every(10).minutes.do(post_message)


if __name__ == "__main__":
    print("🚀 BOMBUCKS SHILL BOT ACTIVATED")
    post_message()  # Primera vez
    while True:
        schedule.run_pending()
        time.sleep(1)

    main()

