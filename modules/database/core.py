import json
import os
from modules.config.constants import DATA_FILE, DEFAULT_CATEGORIES

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