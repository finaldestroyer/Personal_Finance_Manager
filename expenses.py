import json
import os

DATA_FILE = 'data/expenses.json'

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    return []

def save_data(data):
    with open(DATA_FILE, 'w') as file:
        json.dump(data, file, indent=4)

def add_expense(category, description, amount):
    data = load_data()
    data.append({'category': category, 'description': description, 'amount': amount})
    save_data(data)

def view_expenses():
    return load_data()
