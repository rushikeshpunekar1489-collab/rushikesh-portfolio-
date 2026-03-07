"""
🧠 Quiz App
-----------
A multiple-choice quiz with score tracking.
Test your knowledge across different topics!

Author: Rushikesh Punekar
"""


QUESTIONS = [
    {
        "question": "What is the capital of France?",
        "options": ["A) Berlin", "B) Madrid", "C) Paris", "D) Rome"],
        "answer": "C",
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A) Venus", "B) Mars", "C) Jupiter", "D) Saturn"],
        "answer": "B",
    },
    {
        "question": "What does CPU stand for?",
        "options": [
            "A) Central Processing Unit",
            "B) Computer Personal Unit",
            "C) Central Program Utility",
            "D) Central Processor Unifier",
        ],
        "answer": "A",
    },
    {
        "question": "Who developed the Python programming language?",
        "options": [
            "A) James Gosling",
            "B) Dennis Ritchie",
            "C) Guido van Rossum",
            "D) Bjarne Stroustrup",
        ],
        "answer": "C",
    },
    {
        "question": "What is the largest ocean on Earth?",
        "options": [
            "A) Atlantic Ocean",
            "B) Indian Ocean",
            "C) Arctic Ocean",
            "D) Pacific Ocean",
        ],
        "answer": "D",
    },
    {
        "question": "Which data structure uses FIFO (First In, First Out)?",
        "options": ["A) Stack", "B) Queue", "C) Tree", "D) Graph"],
        "answer": "B",
    },
    {
        "question": "How many bits are in a byte?",
        "options": ["A) 4", "B) 8", "C) 16", "D) 32"],
        "answer": "B",
    },
    {
        "question": "What year was the first iPhone released?",
        "options": ["A) 2005", "B) 2006", "C) 2007", "D) 2008"],
        "answer": "C",
    },
    {
        "question": "Which HTML tag is used for the largest heading?",
        "options": ["A) <heading>", "B) <h6>", "C) <head>", "D) <h1>"],
        "answer": "D",
    },
    {
        "question": "What does 'HTTP' stand for?",
        "options": [
            "A) HyperText Transfer Protocol",
            "B) HighText Transfer Protocol",
            "C) HyperText Transmission Program",
            "D) Hyper Transfer Text Protocol",
        ],
        "answer": "A",
    },
]


def run_quiz():
    print("=" * 44)
    print("   🧠  PYTHON QUIZ APP  🧠")
    print("=" * 44)
    print(f"\nAnswer {len(QUESTIONS)} questions. Enter A, B, C, or D.\n")

    score = 0

    for i, q in enumerate(QUESTIONS, 1):
        print(f"Q{i}. {q['question']}")
        for opt in q["options"]:
            print(f"    {opt}")

        while True:
            ans = input("Your answer: ").strip().upper()
            if ans in ("A", "B", "C", "D"):
                break
            print("⚠️  Enter A, B, C, or D.")

        if ans == q["answer"]:
            print("✅ Correct!\n")
            score += 1
        else:
            print(f"❌ Wrong! The answer was {q['answer']}.\n")

    print("=" * 44)
    pct = (score / len(QUESTIONS)) * 100
    print(f"\n📊 Your Score: {score}/{len(QUESTIONS)} ({pct:.0f}%)")

    if pct == 100:
        print("🏆 Perfect score! You're a genius!")
    elif pct >= 70:
        print("🎉 Great job! Well done!")
    elif pct >= 50:
        print("👍 Not bad! Keep learning!")
    else:
        print("📚 Keep studying, you'll improve!")

    print()


if __name__ == "__main__":
    run_quiz()
