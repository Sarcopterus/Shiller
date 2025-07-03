import random

_TEMPLATES = {
    "hype": [
        "$BOMBUCKS is detonating as we speak. Get in or get vaporized.",
        "Chart looking like a rocket on steroids. $BOMBUCKS isn't a meme, it's prophecy.",
        "Degens already know: $BOMBUCKS > your retirement plan.",
    ],
    "warning": [
        "Don't say we didn't warn you. $BOMBUCKS just flipped reality.",
        "Imagine not buying $BOMBUCKS. Sad.",
        "They laughed. Now they cry. $BOMBUCKS just nuked the presale mafia.",
    ],
    "mystic": [
        "It fell from the glitch heavens. A new memetic god: $BOMBUCKS.",
        "Wizards saw it in the charts. Shamans screamed it in their sleep. $BOMBUCKS is here.",
        "The prophecy was pixelated. The name was $BOMBUCKS.",
    ],
}


def generate_message(tone: str = "hype") -> str:
    """Return a random shill message for the given tone."""
    messages = _TEMPLATES.get(tone.lower())
    if messages:
        return random.choice(messages)
    return "$BOMBUCKS is inevitable."


if __name__ == "__main__":
    print(generate_message("mystic"))
