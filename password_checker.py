SPECIAL_CHARACTERS = "!@#$%^&*()-_=+[]{};:'\",.<>/?\\|`~"

def has_uppercase(password):
    return any(ch.isupper() for ch in password)

def has_lowercase(password):
    return any(ch.islower() for ch in password)

def has_digit(password):
    return any(ch.isdigit() for ch in password)

def has_special_character(password):
    return any(ch in SPECIAL_CHARACTERS for ch in password)

def check_password(password):
    tips = []
    checks = 0
    if len(password) >= 8: checks += 1
    else: tips.append("Make it at least 8 characters long.")
    if has_uppercase(password): checks += 1
    else: tips.append("Add at least one UPPERCASE letter.")
    if has_lowercase(password): checks += 1
    else: tips.append("Add at least one lowercase letter.")
    if has_digit(password): checks += 1
    else: tips.append("Add at least one number (0-9).")
    if has_special_character(password): checks += 1
    else: tips.append("Add at least one special character.")
    strength = "Weak" if checks <= 2 else "Moderate" if checks <= 4 else "Strong"
    return strength, tips, checks

def main():
    print("=== Password Strength Checker ===")
    while True:
        password = input("Enter a password: ")
        if password.lower() == "quit":
            print("Goodbye!")
            break
        strength, tips, checks = check_password(password)
        print(f"\nStrength: {strength} ({checks}/5 checks passed)")
        if tips:
            for tip in tips: print("  - " + tip)
        else: print("Great job! This password meets all 5 checks.")

if __name__ == "__main__": main()
