import random

phrases = [
    "BUY THE DIP",
    "BOMBUCKS IS THE FUTURE",
    "HODL STRONG",
    "TO THE MOON",
    "100x INCOMING"
]

templates = [
    "{phrase}! {topic} is about to explode!",
    "Get in on {topic} now - {phrase}!",
    "{topic} is the next big thing. {phrase}!",
    "Don't miss {topic}! {phrase}!"
]

def generate_shill_message(topic: str) -> str:
    phrase = random.choice(phrases)
    template = random.choice(templates)
    return template.format(topic=topic, phrase=phrase)
