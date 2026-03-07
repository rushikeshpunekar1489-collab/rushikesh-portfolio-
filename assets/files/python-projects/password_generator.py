"""
🔐 Password Generator
---------------------
Generate secure random passwords with customizable
length and character options.

Author: Rushikesh Punekar
"""

import random
import string


def generate_password(length=12, use_upper=True, use_digits=True, use_special=True):
    chars = string.ascii_lowercase
    required = [random.choice(string.ascii_lowercase)]

    if use_upper:
        chars += string.ascii_uppercase
        required.append(random.choice(string.ascii_uppercase))
    if use_digits:
        chars += string.digits
        required.append(random.choice(string.digits))
    if use_special:
        chars += string.punctuation
        required.append(random.choice(string.punctuation))

    remaining = length - len(required)
    if remaining < 0:
        remaining = 0

    password_chars = required + [random.choice(chars) for _ in range(remaining)]
    random.shuffle(password_chars)
    return "".join(password_chars)


def main():
    print("=" * 40)
    print("   🔐  PASSWORD GENERATOR  🔐")
    print("=" * 40)

    while True:
        try:
            length = int(input("\nPassword length (8-64, default 12): ") or "12")
            length = max(4, min(64, length))
        except ValueError:
            length = 12

        use_upper = input("Include uppercase? (Y/n): ").strip().lower() != "n"
        use_digits = input("Include digits? (Y/n): ").strip().lower() != "n"
        use_special = input("Include special chars? (Y/n): ").strip().lower() != "n"

        count = 1
        try:
            count = int(input("How many passwords? (default 1): ") or "1")
            count = max(1, min(20, count))
        except ValueError:
            count = 1

        print(f"\n{'─' * 40}")
        print("Generated Password(s):")
        print(f"{'─' * 40}")
        for i in range(count):
            pw = generate_password(length, use_upper, use_digits, use_special)
            print(f"  {i + 1}. {pw}")
        print(f"{'─' * 40}")

        again = input("\nGenerate more? (y/N): ").strip().lower()
        if again != "y":
            break

    print("\n✅ Stay safe with strong passwords!")


if __name__ == "__main__":
    main()
