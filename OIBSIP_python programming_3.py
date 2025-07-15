import string
import random

def get_user_preferences():
    print("Welcome to the Password Generator!\n")

    while True:
        try:
            length = int(input("Enter password length (minimum 4): "))
            if length < 4:
                print("Password length should be at least 4.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")

    use_letters = input("Include letters? (y/n): ").lower() == 'y'
    use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
    use_symbols = input("Include symbols? (y/n): ").lower() == 'y'

    if not any([use_letters, use_numbers, use_symbols]):
        print("You must select at least one character type.")
        return get_user_preferences()

    return length, use_letters, use_numbers, use_symbols

def generate_password(length, use_letters, use_numbers, use_symbols):
    characters = ''
    if use_letters:
        characters += string.ascii_letters  # a-zA-Z
    if use_numbers:
        characters += string.digits         # 0-9
    if use_symbols:
        characters += string.punctuation    # Special chars like !@#$%^&*

    if not characters:
        return "No character sets selected."

    # Secure password using random.SystemRandom()
    secure_random = random.SystemRandom()
    password = ''.join(secure_random.choice(characters) for _ in range(length))
    return password

def main():
    length, use_letters, use_numbers, use_symbols = get_user_preferences()
    password = generate_password(length, use_letters, use_numbers, use_symbols)
    print("\nGenerated Password:", password)

if __name__ == "__main__":
    main()
