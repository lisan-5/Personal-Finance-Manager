from modules.utils.console import print_header, print_warning
from modules.database.core import load_data
from modules.transactions.expense_manager import add_expense
from modules.transactions.income_manager import add_income
from modules.reports.report_generator import generate_report
from modules.budget.manager import set_budget_for_categories, update_budget
from modules.categories.manager import manage_categories
from modules.analysis.trends import analyze_trends
from modules.transactions.viewer import view_transactions
from modules.export import export_data

class FinanceTracker:
    def __init__(self):
        self.data = load_data()

    def display_menu(self):
        print("\n1. Add Expense")
        print("2. Add Income")
        print("3. View Report")
        print("4. Set Budget")
        print("5. Export Data")
        print("6. View Transactions")
        print("7. Manage Categories")
        print("8. Analyze Trends")
        print("9. Exit")

    def add_expense(self):
        add_expense(self.data)

    def add_income(self):
        add_income(self.data)

    def generate_report(self):
        generate_report(self.data)

    def set_budget(self):
        budgets = set_budget_for_categories(self.data["categories"])
        update_budget(budgets)
        self.data = load_data()  # Reload data after update

    def export_data(self):
        print_header("Export Data")
        export_data(self.data)

    def view_transactions(self):
        view_transactions(self.data)

    def manage_categories(self):
        manage_categories(self.data)
        self.data = load_data()  # Reload data after category changes

    def analyze_trends(self):
        analyze_trends(self.data)