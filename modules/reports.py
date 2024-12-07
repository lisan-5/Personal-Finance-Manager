from modules.database import load_data
from modules.utils.calculations import calculate_category_totals, calculate_budget_status
from modules.reports.summary import generate_summary_report
from modules.reports.category_report import generate_category_report
from modules.reports.budget_report import generate_budget_report

def generate_report():
    print("\n=== Financial Report ===")
    data = load_data()
    
    # Calculate totals
    total_income = sum(transaction["amount"] for transaction in data["income"])
    expenses_by_category, total_expenses = calculate_category_totals(data["expenses"])
    
    # Generate reports
    generate_summary_report(total_income, total_expenses)
    generate_category_report(expenses_by_category, total_expenses)
    
    # Budget comparison
    if data["budget"]:
        budget_status = calculate_budget_status(data["budget"], expenses_by_category)
        generate_budget_report(budget_status)