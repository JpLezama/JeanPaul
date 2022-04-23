from App.models import Word
from App.database import db
import random


def get_all_words_json():
    words = Word.query.all()
    if not words:
        return []
    words = [Word.toDict() for Word in words]
    return words

def start_game(amount):
    words = Word.query.all()
    random_word = random.sample(words, amount)
    return random_word

def check_word():
    words = Word.query.all()