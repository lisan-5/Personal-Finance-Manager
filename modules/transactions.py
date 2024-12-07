from modules.database.transactions import add_transaction, get_categories
from modules.utils.input_validators import validate_amount, validate_category_choice

def add_expense():
    print("\n=== Add Expense ===")
    amount = validate_amount()
    category = validate_category_choice(get_categories())
    description = input("Enter description: ")
    add_transaction("expenses", amount, category, description)
    print("\nExpense added successfully!")

def add_income():
    print("\n=== Add Income ===")
    amount = validate_amount()
    description = input("Enter description: ")
    add_transaction("income", amount, "Income", description)
    print("\nIncome added successfully!")