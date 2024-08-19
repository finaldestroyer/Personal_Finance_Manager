import json
import os

DATA_FILE = 'data/budget.json'

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    return {}

def save_data(data):
    with open(DATA_FILE, 'w') as file:
        json.dump(data, file, indent=4)

def set_budget(category, amount):
    data = load_data()
    data[category] = amount
    save_data(data)

def view_budget():
    return load_data()
