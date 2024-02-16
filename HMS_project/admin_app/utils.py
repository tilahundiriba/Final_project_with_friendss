import random
import string

def generate_username(email, profession):
    # Extract a specific part of the email
    email_parts = email.split("@")
    username = email_parts[0].split(".")[0]  # Extract the first part before the dot (.) if available
    
    if profession:
        username += "_" + profession.lower().replace(" ", "_")
    
    return username

def generate_password(length=8):
    # Generate a random password of the specified length
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for _ in range(length))
    return password