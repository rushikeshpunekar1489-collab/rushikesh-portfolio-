"""
🎲 Number Guessing Game
-----------------------
Guess the secret number between 1 and 100.
The program gives you hints after each guess.

Author: Rushikesh Punekar
"""

import random


def play():
    secret = random.randint(1, 100)
    attempts = 0
    max_attempts = 10

    print("=" * 40)
    print("   🎲  NUMBER GUESSING GAME  🎲")
    print("=" * 40)
    print(f"\nI'm thinking of a number between 1 and 100.")
    print(f"You have {max_attempts} attempts. Good luck!\n")

    while attempts < max_attempts:
        try:
            guess = int(input(f"Attempt {attempts + 1}/{max_attempts} — Your guess: "))
        except ValueError:
            print("⚠️  Please enter a valid number.\n")
            continue

        attempts += 1

        if guess < secret:
            print("📈 Too low! Try higher.\n")
        elif guess > secret:
            print("📉 Too high! Try lower.\n")
        else:
            print(f"\n🎉 Correct! You guessed it in {attempts} attempt(s)!")
            break
    else:
        print(f"\n😞 Out of attempts! The number was {secret}.")

    print("\nThanks for playing!")


if __name__ == "__main__":
    play()
