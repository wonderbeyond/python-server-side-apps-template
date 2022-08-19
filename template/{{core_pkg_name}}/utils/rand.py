import string
import random


def get_random_string(N=12, allowed_chars=(string.ascii_letters + string.digits)):
    return ''.join(random.choice(allowed_chars) for _ in range(N))
