import string
import random

def random_word(max_length: int, min_length = 1) -> str:
    random_length = random.SystemRandom().randint(min_length, max_length)
    return ''.join(random.SystemRandom().choices(string.ascii_letters, k=random_length))
