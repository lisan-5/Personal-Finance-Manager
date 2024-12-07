from modules.utils.console import print_header, print_table
from modules.utils.input_validators import validate_date_range
from modules.utils.date_helpers import parse_timestamp
from modules.utils.calculations import (
    calculate_category_totals,
    calculate_budget_status,
    calculate_savings_rate
)

def generate_report(data):
    print_header("Financial Report")
    
    # Date range selection
    start_date, end_date = validate_date_range()
    
    # Filter transactions by date range
    filtered_expenses = [
        e for e in data["expenses"] 
        if start_date <= parse_timestamp(e["timestamp"]).date() <= end_date
    ]
    filtered_income = [
        i for i in data["income"]
        if start_date <= parse_timestamp(i["timestamp"]).date() <= end_date
    ]
    
    # Calculate totals
    total_income = sum(t["amount"] for t in filtered_income)
    expenses_by_category, total_expenses = calculate_category_totals(filtered_expenses)
    savings_rate = calculate_savings_rate(total_income, total_expenses)
    
    _print_summary(total_income, total_expenses, savings_rate)
    _print_category_breakdown(expenses_by_category, total_expenses)
    _print_budget_comparison(data["budget"], expenses_by_category)

def _print_summary(total_income, total_expenses, savings_rate):
    print("\nSummary:")
    print("-" * 40)
    print(f"Total Income:    ${total_income:>10.2f}")
    print(f"Total Expenses:  ${total_expenses:>10.2f}")
    print(f"Net Balance:     ${(total_income - total_expenses):>10.2f}")
    print(f"Savings Rate:    {savings_rate:>10.1f}%")

def _print_category_breakdown(expenses_by_category, total_expenses):
    if not expenses_by_category:
        return
        
    print("\nExpenses by Category:")
    headers = ["Category", "Amount", "% of Total"]
    rows = []
    for category, amount in expenses_by_category.items():
        percentage = (amount / total_expenses * 100) if total_expenses > 0 else 0
        rows.append([category, f"${amount:.2f}", f"{percentage:.1f}%"])
    print_table(headers, rows)

def _print_budget_comparison(budget, expenses_by_category):
    if not budget:
        return
        
    print("\nBudget Comparison:")
    headers = ["Category", "Budget", "Spent", "Remaining", "% Used"]
    rows = []
    
    budget_status = calculate_budget_status(budget, expenses_by_category)
    for category, status in budget_status.items():
        rows.append([
            category,
            f"${status['budget']:.2f}",
            f"${status['spent']:.2f}",
            f"${status['remaining']:.2f}",
            f"{status['percentage']:.1f}%"
        ])
    print_table(headers, rows)