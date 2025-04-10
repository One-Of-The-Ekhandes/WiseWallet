from flask import Flask, render_template, request, redirect
import csv
from datetime import datetime
import os

app = Flask(__name__)

# Initialize CSV file if it doesn't exist
if not os.path.exists('expenses.csv'):
    with open('expenses.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Amount', 'Category', 'Date', 'Description'])

@app.route("/")
def home():
    return render_template("add_expense.html")

@app.route("/add", methods=["POST"])
def add():
    amount = request.form["amount"]
    category = request.form["category"]
    description = request.form["description"]
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("expenses.csv", "a", newline='') as file:
        writer = csv.writer(file)
        writer.writerow([amount, category, date, description])

    return redirect("/view")

@app.route("/view")
def view():
    try:
        with open('expenses.csv', 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header row
            expenses = list(reader)
    except FileNotFoundError:
        expenses = []

    return render_template("view_expense.html", expenses=expenses)

if __name__ == "__main__":
    app.run(debug=True)