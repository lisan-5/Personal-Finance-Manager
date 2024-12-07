from modules.utils.console import print_header, print_warning, print_success
from modules.utils.input_validators import validate_amount
from modules.utils.date_helpers import get_current_timestamp
from modules.database.core import save_data
from datetime import datetime

def add_income(data):
    print_header("Add Income")
    amount = validate_amount()
    description = input("Enter description: ")
    date = input("Enter date (YYYY-MM-DD) or press Enter for today: ").strip()
    
    if not date:
        timestamp = get_current_timestamp()
    else:
        try:
            timestamp = f"{date} {datetime.now().strftime('%H:%M:%S')}"
            datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S")
        except ValueError:
            print_warning("Invalid date format. Using current date.")
            timestamp = get_current_timestamp()
    
    income = {
        "timestamp": timestamp,
        "amount": amount,
        "description": description
    }
    data["income"].append(income)
    save_data(data)
    print_success("Income added successfully!")