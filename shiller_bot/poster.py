import random

try:
    from colorama import init, Fore, Style
    init(autoreset=True)
    COLOR = True
except Exception:
    COLOR = False


def _color(text: str) -> str:
    if COLOR:
        return f"{Fore.CYAN}{text}{Style.RESET_ALL}"
    return text


def post_to_console(message: str) -> None:
    print(_color(f">> {message}"))


def simulate_post_to_x(message: str) -> None:
    print(_color(f"[X] {message}"))


def simulate_post_to_telegram(message: str) -> None:
    print(_color(f"[Telegram] {message}"))


ALL_POSTERS = [simulate_post_to_x, simulate_post_to_telegram]


def post_random(message: str) -> None:
    random.choice(ALL_POSTERS)(message)
