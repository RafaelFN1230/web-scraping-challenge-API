import random
import string

def generate_strong_password():
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_chars = "!@#$%&*"

    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(special_chars)
    ]

    all_chars = lowercase + uppercase + digits + special_chars
    password += random.choices(all_chars, k=6)
    random.shuffle(password)

    return ''.join(password)

def generate_random_string(length=10):
    return ''.join(random.choices(string.ascii_letters, k=length))
