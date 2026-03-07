"""
💰 Expense Tracker
------------------
Track your daily expenses with categories.
View summary, totals, and category breakdown.

Author: Rushikesh Punekar
"""

from datetime import datetime


CATEGORIES = ["Food", "Transport", "Shopping", "Bills", "Entertainment", "Health", "Other"]


def show_menu():
    print("\n  1. ➕ Add Expense")
    print("  2. 📋 View All Expenses")
    print("  3. 📊 View Summary")
    print("  4. 🗑️  Clear All")
    print("  5. 🚪 Exit")
    return input("\n  Choose (1-5): ").strip()


def add_expense(expenses):
    print(f"\n{'─' * 40}")
    print("  ➕ Add New Expense")
    print(f"{'─' * 40}")

    try:
        amount = float(input("  Amount (₹): "))
        if amount <= 0:
            print("  ⚠️  Amount must be positive.")
            return
    except ValueError:
        print("  ⚠️  Invalid amount.")
        return

    desc = input("  Description: ").strip() or "No description"

    print("\n  Categories:")
    for i, cat in enumerate(CATEGORIES, 1):
        print(f"    {i}. {cat}")

    try:
        cat_idx = int(input("  Choose category (1-7): ")) - 1
        category = CATEGORIES[cat_idx]
    except (ValueError, IndexError):
        category = "Other"

    expense = {
        "amount": amount,
        "description": desc,
        "category": category,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
    }
    expenses.append(expense)
    print(f"\n  ✅ Added: ₹{amount:.2f} — {desc} [{category}]")


def view_expenses(expenses):
    if not expenses:
        print("\n  📭 No expenses recorded yet.")
        return

    print(f"\n{'━' * 56}")
    print(f"  {'#':<4} {'Date':<17} {'Category':<14} {'Amount':>8}  Description")
    print(f"{'━' * 56}")

    for i, e in enumerate(expenses, 1):
        print(f"  {i:<4} {e['date']:<17} {e['category']:<14} ₹{e['amount']:>7.2f}  {e['description']}")

    total = sum(e["amount"] for e in expenses)
    print(f"{'━' * 56}")
    print(f"  {'TOTAL':<35} ₹{total:>7.2f}")
    print(f"{'━' * 56}")


def view_summary(expenses):
    if not expenses:
        print("\n  📭 No expenses to summarize.")
        return

    total = sum(e["amount"] for e in expenses)
    category_totals = {}
    for e in expenses:
        category_totals[e["category"]] = category_totals.get(e["category"], 0) + e["amount"]

    print(f"\n{'━' * 42}")
    print("  📊  EXPENSE SUMMARY")
    print(f"{'━' * 42}")
    print(f"  Total Expenses  : {len(expenses)}")
    print(f"  Total Amount    : ₹{total:.2f}")
    print(f"  Average Expense : ₹{total / len(expenses):.2f}")
    print(f"\n  Category Breakdown:")
    print(f"  {'─' * 34}")

    for cat, amt in sorted(category_totals.items(), key=lambda x: x[1], reverse=True):
        pct = (amt / total) * 100
        bar = "█" * int(pct / 5)
        print(f"  {cat:<14} ₹{amt:>8.2f}  {pct:>5.1f}%  {bar}")

    print(f"{'━' * 42}")


def main():
    expenses = []

    print("=" * 42)
    print("   💰  EXPENSE TRACKER  💰")
    print("=" * 42)

    while True:
        choice = show_menu()

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            view_summary(expenses)
        elif choice == "4":
            if expenses:
                confirm = input("\n  ⚠️  Clear all expenses? (y/N): ").strip().lower()
                if confirm == "y":
                    expenses.clear()
                    print("  🗑️  All expenses cleared.")
            else:
                print("\n  📭 Nothing to clear.")
        elif choice == "5":
            print("\n  👋 Goodbye! Stay on budget!")
            break
        else:
            print("  ⚠️  Enter 1-5.")


if __name__ == "__main__":
    main()
