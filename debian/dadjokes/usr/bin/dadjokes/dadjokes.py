#!/usr/bin/env python3
import random

JOKE_FILE = '/usr/share/dadjokes'

def load_jokes():
    """Load jokes from the specified file."""
    with open(JOKE_FILE, 'r') as file:
        return [line.strip() for line in file if line.strip()]

def get_random_joke(jokes):
    """Return a random joke from the list of jokes."""
    return random.choice(jokes)

if __name__ == "__main__":
    jokes = load_jokes()
    print(get_random_joke(jokes))
