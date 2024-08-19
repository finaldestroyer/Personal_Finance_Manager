import json
import os

DATA_FILE = 'data/savings.json'

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    return {'goal': 0, 'saved': 0}

def save_data(data):
    with open(DATA_FILE, 'w') as file:
        json.dump(data, file, indent=4)

def set_savings_goal(goal):
    data = load_data()
    data['goal'] = goal
    save_data(data)

def add_savings(amount):
    data = load_data()
    data['saved'] += amount
    save_data(data)

def view_savings():
    return load_data()
