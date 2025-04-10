import csv
from datetime import datetime

def add_expense():
    try:
        amount = float(input("Enter the expense amount: ₹"))
        category = input("Enter the category (e.g., food, rent, travel, etc.): ").strip()
        description = input("Enter a description (optional): ").strip()
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open("expenses.csv", "a", newline='') as file:
            writer = csv.writer(file)
            writer.writerow([amount, category, date, description])

        print("✅ Expense added successfully.")
    except ValueError:
        print("❌ Invalid input. Please enter a valid number for amount.")

def view_expenses():
    try:
        with open('expenses.csv', 'r') as file:
            reader = csv.reader(file)
            expenses = list(reader)

            if not expenses:
                print("No expenses recorded yet.")
                return

            print("\n--- Expense History ---")
            print(f"{'Amount':<10} | {'Category':<10} | {'Date':<19} | {'Note'}")
            print("-" * 60)
            for row in expenses:
                try:
                    print(f"₹{float(row[0]):<8.2f} | {row[1]:<10} | {row[2]:<19} | {row[3]}")
                except (IndexError, ValueError):
                    continue  # Skip malformed rows

            # Group by category
            category_totals = {}
            for row in expenses:
                try:
                    category = row[1]
                    amount = float(row[0])
                    category_totals[category] = category_totals.get(category, 0) + amount
                except (IndexError, ValueError):
                    continue

            print("\n--- Total Spent by Category ---")
            for cat, total in category_totals.items():
                print(f"{cat.capitalize():<10}: ₹{total:.2f}")

    except FileNotFoundError:
        print("No expenses recorded yet.")








