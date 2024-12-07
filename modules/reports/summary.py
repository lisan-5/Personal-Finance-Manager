from modules.reports.formatters import format_currency, print_report_header

def generate_summary_report(total_income, total_expenses):
    print_report_header("Summary:")
    print(f"Total Income:    {format_currency(total_income):>10}")
    print(f"Total Expenses:  {format_currency(total_expenses):>10}")
    print(f"Net Balance:     {format_currency(total_income - total_expenses):>10}")