"""
📝 Word Counter Tool
--------------------
Analyze any text: word count, character count,
sentence count, and word frequency.

Author: Rushikesh Punekar
"""

import string
from collections import Counter


def analyze_text(text):
    # Basic counts
    char_count = len(text)
    char_no_spaces = len(text.replace(" ", ""))
    words = text.split()
    word_count = len(words)
    sentence_count = sum(1 for c in text if c in ".!?") or (1 if text.strip() else 0)
    line_count = text.count("\n") + 1 if text.strip() else 0

    # Word frequency (cleaned)
    cleaned_words = [
        w.strip(string.punctuation).lower() for w in words if w.strip(string.punctuation)
    ]
    frequency = Counter(cleaned_words)

    return {
        "chars": char_count,
        "chars_no_spaces": char_no_spaces,
        "words": word_count,
        "sentences": sentence_count,
        "lines": line_count,
        "frequency": frequency,
    }


def display_results(stats):
    print(f"\n{'━' * 42}")
    print("  📊  TEXT ANALYSIS RESULTS")
    print(f"{'━' * 42}")
    print(f"  📝  Words          :  {stats['words']}")
    print(f"  🔤  Characters     :  {stats['chars']}")
    print(f"  🔡  Chars (no spc) :  {stats['chars_no_spaces']}")
    print(f"  📃  Sentences      :  {stats['sentences']}")
    print(f"  📄  Lines          :  {stats['lines']}")
    print(f"{'━' * 42}")

    # Top 10 most common words
    if stats["frequency"]:
        print("\n  🏆  Top 10 Most Frequent Words:")
        print(f"  {'─' * 30}")
        for word, count in stats["frequency"].most_common(10):
            bar = "█" * min(count, 20)
            print(f"  {word:<15} {count:>3}  {bar}")
        print()


def main():
    print("=" * 42)
    print("   📝  WORD COUNTER TOOL  📝")
    print("=" * 42)

    while True:
        print("\nOptions:")
        print("  1. Type / paste text")
        print("  2. Analyze a file")
        print("  3. Quit")

        choice = input("\nYour choice (1/2/3): ").strip()

        if choice == "1":
            print("\nEnter your text (press Enter twice to finish):")
            lines = []
            while True:
                line = input()
                if line == "":
                    break
                lines.append(line)
            text = "\n".join(lines)
            if text.strip():
                stats = analyze_text(text)
                display_results(stats)
            else:
                print("⚠️  No text entered.")

        elif choice == "2":
            filepath = input("\nEnter file path: ").strip()
            try:
                with open(filepath, "r", encoding="utf-8") as f:
                    text = f.read()
                stats = analyze_text(text)
                display_results(stats)
            except FileNotFoundError:
                print(f"❌ File '{filepath}' not found.")
            except Exception as e:
                print(f"❌ Error reading file: {e}")

        elif choice in ("3", "quit", "q"):
            break
        else:
            print("⚠️  Enter 1, 2, or 3.")

    print("\n👋 Goodbye!")


if __name__ == "__main__":
    main()
