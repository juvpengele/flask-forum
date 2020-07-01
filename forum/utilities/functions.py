import string
import random

def generate_random_str(str_length=6):
    letters = string.ascii_lowercase + string.digits
    return ''.join(random.choice(letters) for i in range(str_length))