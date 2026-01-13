import random
import string

def generate_simple_password():
    characters = string.ascii_letters + string.digits + string.punctuation
    
    password = "".join(random.choice(characters) for i in range(8))
    
    print(f"Your new password is: {password}")

generate_simple_password()