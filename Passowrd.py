import random
import string

def generate_password(length):
    if length < 4:
        print("Password length should be at least 4.")
        return None

    all_characters = string.ascii_letters + string.digits + string.punctuation
    password = []

    # Ensure the password contains at least one letter, one digit, and one punctuation
    password.append(random.choice(string.ascii_letters))
    password.append(random.choice(string.digits))
    password.append(random.choice(string.punctuation))

    # Fill the rest of the password length with random characters
    password.extend(random.choice(all_characters) for _ in range(length - 3))

    # Shuffle the list to avoid predictable patterns
    random.shuffle(password)

    # Join the list to form the final password string
    return ''.join(password)

def main():
    try:
        length = int(input("Enter the desired length for the password: "))
        password = generate_password(length)
        if password:
            print(f"Generated Password: {password}")
    except ValueError:
        print("Please enter a valid number for the password length.")

if __name__ == "__main__":
    main()
