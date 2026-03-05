"""
⏱️ Countdown Timer
------------------
Set a countdown in minutes and seconds.
Watch the timer tick down in real time!

Author: Rushikesh Punekar
"""

import time
import sys


def countdown(total_seconds):
    print()
    while total_seconds >= 0:
        mins, secs = divmod(total_seconds, 60)
        timer_display = f"  ⏱️  {mins:02d}:{secs:02d}  "
        sys.stdout.write(f"\r{timer_display}")
        sys.stdout.flush()
        time.sleep(1)
        total_seconds -= 1

    print("\n")
    print("=" * 34)
    print("   🔔  TIME'S UP!  🔔")
    print("=" * 34)


def main():
    print("=" * 34)
    print("   ⏱️  COUNTDOWN TIMER  ⏱️")
    print("=" * 34)

    while True:
        print()
        try:
            mins = int(input("Minutes (0-99): ") or "0")
            secs = int(input("Seconds (0-59): ") or "0")
        except ValueError:
            print("⚠️  Please enter valid numbers.")
            continue

        mins = max(0, min(99, mins))
        secs = max(0, min(59, secs))
        total = mins * 60 + secs

        if total == 0:
            print("⚠️  Set at least 1 second.")
            continue

        print(f"\n▶️  Starting {mins:02d}:{secs:02d} countdown...")
        countdown(total)

        again = input("\nSet another timer? (y/N): ").strip().lower()
        if again != "y":
            break

    print("\n👋 Goodbye!")


if __name__ == "__main__":
    main()
