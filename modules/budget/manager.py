from modules.database.core import load_data, save_data
from modules.utils.input_validators import validate_amount

def set_budget_for_categories(categories):
    budgets = {}
    print("\n=== Set Budget ===")
    for category in categories:
        while True:
            try:
                amount = validate_amount()
                if amount >= 0:
                    budgets[category] = amount
                    break
                print("Budget must be non-negative")
            except ValueError:
                print("Please enter a valid number")
    return budgets

def update_budget(budgets):
    data = load_data()
    data["budget"] = budgets
    save_data(data)
    print("\nBudget updated successfully!")