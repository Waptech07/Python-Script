import random
import string

def generate_password(length):
    if length < 6:
        print("Password length should be at least 6 characters for security.")
        return None

    # Characters to use in the password
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    try:
        # Accept input for password length
        length = int(input("Enter the desired password length (minimum 6): "))
        secure_password = generate_password(length)
        if secure_password:
            print(f"Your secure password: {secure_password}")
    except ValueError:
        print("Please enter a valid number for the password length.")
