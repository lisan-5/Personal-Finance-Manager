from datetime import datetime, timedelta
from modules.utils.date_helpers import get_default_date_range

def validate_amount():
    while True:
        try:
            amount = float(input("Enter amount: $"))
            if amount <= 0:
                print("Amount must be greater than 0")
                continue
            return amount
        except ValueError:
            print("Please enter a valid number")

def validate_category_choice(categories):
    while True:
        print("\nAvailable categories:")
        for i, category in enumerate(categories, 1):
            print(f"{i}. {category}")
        
        try:
            choice = int(input("\nSelect category number: "))
            if 1 <= choice <= len(categories):
                return categories[choice - 1]
            print("Invalid category number")
        except ValueError:
            print("Please enter a valid number")

def validate_date_range():
    default_start, default_end = get_default_date_range()
    
    print("\nEnter date range (YYYY-MM-DD) or press Enter for current month")
    start_input = input(f"Start date [{default_start}]: ").strip()
    end_input = input(f"End date [{default_end}]: ").strip()
    
    try:
        start_date = (datetime.strptime(start_input, "%Y-%m-%d").date() 
                     if start_input else default_start)
        end_date = (datetime.strptime(end_input, "%Y-%m-%d").date() 
                   if end_input else default_end)
        
        if start_date > end_date:
            print("Invalid date range. Using default range.")
            return default_start, default_end
            
        return start_date, end_date
    except ValueError:
        print("Invalid date format. Using default range.")
        return default_start, default_end