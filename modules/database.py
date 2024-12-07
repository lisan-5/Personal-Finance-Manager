import json
import os
from datetime import datetime
from modules.utils.date_helpers import get_current_timestamp

DEFAULT_CATEGORIES = ["Food", "Transportation", "Housing", "Utilities", "Entertainment", "Healthcare", "Other"]
DATA_FILE = "finance_data.json"

def initialize_database():
    if not os.path.exists(DATA_FILE):
        default_data = {
            "expenses": [],
            "income": [],
            "budget": {},
            "categories": DEFAULT_CATEGORIES
        }
        save_data(default_data)

def load_data():
    try:
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        initialize_database()
        return load_data()

def save_data(data):
    with open(DATA_FILE, 'w') as file:
        json.dump(data, file, indent=2)

def add_transaction(type_name, amount, category, description):
    data = load_data()
    transaction = {
        "timestamp": get_current_timestamp(),
        "amount": amount,
        "category": category,
        "description": description
    }
    data[type_name].append(transaction)
    save_data(data)

def get_categories():
    return load_data()["categories"]

def set_budget(budget_data):
    data = load_data()
    data["budget"] = budget_data
    save_data(data)