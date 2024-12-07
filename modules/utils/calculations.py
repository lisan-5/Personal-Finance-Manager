from datetime import datetime
from collections import defaultdict
from modules.utils.date_helpers import parse_timestamp

def calculate_category_totals(expenses):
    category_totals = {}
    total = 0
    
    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]
        category_totals[category] = category_totals.get(category, 0) + amount
        total += amount
    
    return category_totals, total

def calculate_budget_status(budget, expenses_by_category):
    status = {}
    for category, budget_amount in budget.items():
        spent = expenses_by_category.get(category, 0)
        remaining = budget_amount - spent
        status[category] = {
            "budget": budget_amount,
            "spent": spent,
            "remaining": remaining,
            "percentage": (spent / budget_amount * 100) if budget_amount > 0 else 0
        }
    return status

def calculate_savings_rate(total_income, total_expenses):
    if total_income <= 0:
        return 0.0
    return ((total_income - total_expenses) / total_income) * 100

def calculate_monthly_trends(expenses, income):
    # Initialize data structures
    monthly_expenses = defaultdict(lambda: {"expenses": 0, "by_category": defaultdict(float)})
    monthly_income = defaultdict(float)
    
    # Process expenses
    for expense in expenses:
        date = parse_timestamp(expense["timestamp"])
        month_key = date.strftime("%Y-%m")
        amount = expense["amount"]
        category = expense["category"]
        
        monthly_expenses[month_key]["expenses"] += amount
        monthly_expenses[month_key]["by_category"][category] += amount
    
    # Process income
    for inc in income:
        date = parse_timestamp(inc["timestamp"])
        month_key = date.strftime("%Y-%m")
        monthly_income[month_key] += inc["amount"]
    
    # Combine data and calculate trends
    trends = {}
    for month in sorted(set(monthly_expenses.keys()) | set(monthly_income.keys())):
        exp_data = monthly_expenses[month]
        inc_amount = monthly_income[month]
        
        # Find top category
        top_category = max(
            exp_data["by_category"].items(),
            key=lambda x: x[1],
            default=("None", 0)
        )
        
        trends[month] = {
            "income": inc_amount,
            "expenses": exp_data["expenses"],
            "net": inc_amount - exp_data["expenses"],
            "top_category": top_category[0],
            "top_amount": top_category[1]
        }
    
    return trends