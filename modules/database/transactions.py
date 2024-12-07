from modules.database.core import load_data, save_data
from modules.utils.date_helpers import get_current_timestamp

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