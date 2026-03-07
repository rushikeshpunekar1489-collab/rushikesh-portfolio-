"""
✊ Rock Paper Scissors
---------------------
Classic game vs the computer with score tracking.
Play multiple rounds and see who wins!

Author: Rushikesh Punekar
"""

import random


CHOICES = {"r": "Rock", "p": "Paper", "s": "Scissors"}
EMOJIS = {"Rock": "🪨", "Paper": "📄", "Scissors": "✂️"}

# What beats what
BEATS = {"Rock": "Scissors", "Paper": "Rock", "Scissors": "Paper"}


def get_computer_choice():
    return random.choice(list(CHOICES.values()))


def determine_winner(player, computer):
    if player == computer:
        return "draw"
    elif BEATS[player] == computer:
        return "player"
    else:
        return "computer"


def main():
    print("=" * 40)
    print("   ✊  ROCK  PAPER  SCISSORS  ✊")
    print("=" * 40)
    print("\nEnter R (Rock), P (Paper), S (Scissors)")
    print("Type 'quit' to exit.\n")

    wins = losses = draws = 0

    while True:
        choice = input("Your choice: ").strip().lower()

        if choice in ("quit", "exit", "q"):
            break

        if choice not in CHOICES:
            print("⚠️  Enter R, P, or S.\n")
            continue

        player = CHOICES[choice]
        computer = get_computer_choice()

        print(f"\n  You     : {EMOJIS[player]}  {player}")
        print(f"  Computer: {EMOJIS[computer]}  {computer}")

        result = determine_winner(player, computer)

        if result == "draw":
            print("  Result  : 🤝 It's a draw!")
            draws += 1
        elif result == "player":
            print("  Result  : 🎉 You win!")
            wins += 1
        else:
            print("  Result  : 😞 Computer wins!")
            losses += 1

        total = wins + losses + draws
        print(f"\n  📊 Score — W:{wins}  L:{losses}  D:{draws}  (Total: {total})\n")

    # Final summary
    total = wins + losses + draws
    if total > 0:
        print(f"\n{'=' * 40}")
        print("   📊  FINAL SCOREBOARD  📊")
        print(f"{'=' * 40}")
        print(f"  Wins   : {wins}")
        print(f"  Losses : {losses}")
        print(f"  Draws  : {draws}")
        print(f"  Total  : {total}")
        win_pct = (wins / total) * 100
        print(f"  Win %  : {win_pct:.1f}%")
        print(f"{'=' * 40}")

    print("\n👋 Thanks for playing!")


if __name__ == "__main__":
    main()
