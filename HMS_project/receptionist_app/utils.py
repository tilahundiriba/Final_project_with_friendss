import random
import string

def generate_username(first_name, middle_name):
    # Use the first three letters of the first name and the first three letters of the middle name to generate username
    username = first_name[:3].lower() + middle_name[:3].lower()
    return username

def generate_password(length=8):
    # Generate a random password consisting of digits only
    password = ''.join(random.choice(string.digits) for _ in range(length))
    return password
