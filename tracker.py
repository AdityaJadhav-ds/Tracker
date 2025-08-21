import json
import os

FILENAME = "expenses.json"

def load_expenses():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as f:
            return json.load(f)
    return []

def save_expenses(expenses):
    with open(FILENAME, "w") as f:
        json.dump(expenses, f, indent=4)

def add_expense(expenses):
    category = input("Enter category (Food/Transport/Entertainment/Other): ")
    amount = float(input("Enter amount: "))
    description = input("Enter description: ")

    expenses.append({
        "category": category,
        "amount": amount,
        "description": description
    })
    save_expenses(expenses)
    print("✅ Expense added successfully!")

def view_expenses(expenses):
    if not expenses:
        print("📭 No expenses found.")
        return
    
    print("\n--- All Expenses ---")
    for i, e in enumerate(expenses, 1):
        print(f"{i}. {e['category']} - ₹{e['amount']} ({e['description']})")
    
    total = sum(e['amount'] for e in expenses)
    print(f"\n💰 Total Expenses: ₹{total}")

def category_summary(expenses):
    summary = {}
    for e in expenses:
        summary[e['category']] = summary.get(e['category'], 0) + e['amount']
    
    print("\n--- Expense by Category ---")
    for cat, amt in summary.items():
        print(f"{cat}: ₹{amt}")

def main():
    expenses = load_expenses()
    while True:
        print("\n=== 💰 Personal Expense Tracker ===")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Category Summary")
        print("4. Exit")
        choice = input("Enter choice (1-4): ")

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            category_summary(expenses)
        elif choice == "4":
            print("👋 Goodbye!")
            break
        else:
            print("⚠️ Invalid choice! Please enter 1-4.")

if __name__ == "__main__":
    main()
