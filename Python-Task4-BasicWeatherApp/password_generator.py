import secrets
import string
print("=== Random Password Generator ===")
while True:
    try:
        length = int(input("Enter the desired password length (minimum 8 characters): "))
        if length < 8:
            print("Password length must be at least 8 characters.")
            continue
        print("\nChoose character types:")
        use_upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
        use_lower = input("Include lowercase letters? (y/n): ").lower() == 'y'
        use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
        use_symbols = input("Include symbols? (y/n): ").lower() == 'y'
        selected_types = sum([use_upper, use_lower, use_numbers, use_symbols])
        if selected_types < 2:
            print("Please select at least 2 character types.")
            continue
        characters =""
        if use_upper:
            characters += string.ascii_uppercase
        if use_lower:
            characters += string.ascii_lowercase
        if use_numbers:
            characters += string.digits
        if use_symbols:
            characters += string.punctuation
        password = ''.join(secrets.choice(characters) for _ in range(length))
        print("\nGenerated Password:" , password)
        again = input("\nGenerate another password? (y/n): ").lower()
        if again != 'y':
            print("Thank you for using the Random Password Generator!")
            break
    except ValueError:
        print("Error: Please enter a valid numeric value for password length.")