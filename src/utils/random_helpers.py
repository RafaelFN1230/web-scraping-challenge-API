import random
import string

def generate_strong_password():
    """
    Generate a strong password, which must contain at least one lowercase letter, one uppercase letter, one digit, and one special character.

    The length of the password is 8 characters.

    Returns:
        str: The generated password.
    """
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
    """
    Generate a random string of characters.

    Args:
        length (int, optional): The length of the string to generate. Defaults to 10.

    Returns:
        str: A random string of characters.
    """
    return ''.join(random.choices(string.ascii_letters, k=length))
