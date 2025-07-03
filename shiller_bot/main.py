from message_generator import generate_shill_message
from poster import post_to_console, post_random


def main():
    topic = input("\u00bfTema del shill? ")
    message = generate_shill_message(topic)
    post_to_console(message)
    post_random(message)


if __name__ == "__main__":
    main()
