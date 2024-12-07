from modules.reports.formatters import print_report_header, format_category_line

def generate_category_report(expenses_by_category, total_expenses):
    print_report_header("Expenses by Category:")
    print(f"{'Category':<20} {'Amount':>10} {'% of Total':>10}")
    print("-" * 40)
    
    for category, amount in expenses_by_category.items():
        percentage = (amount / total_expenses * 100) if total_expenses > 0 else 0
        print(format_category_line(category, amount, percentage))