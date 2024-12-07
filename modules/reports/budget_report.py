from modules.reports.formatters import print_report_header, format_category_line, format_currency

def generate_budget_report(budget_status):
    print_report_header("Budget Comparison:")
    print(f"{'Category':<20} {'Budget':>10} {'Spent':>10} {'Remaining':>10}")
    print("-" * 50)
    
    for category, status in budget_status.items():
        print(f"{category:<20} {format_currency(status['budget']):>9} "
              f"{format_currency(status['spent']):>9} {format_currency(status['remaining']):>9}")