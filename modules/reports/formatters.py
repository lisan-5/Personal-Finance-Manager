from modules.config.constants import REPORT_SEPARATOR, CATEGORY_COLUMN_WIDTH, AMOUNT_COLUMN_WIDTH

def format_currency(amount):
    return f"${amount:>.2f}"

def print_report_header(title):
    print(f"\n{title}")
    print(REPORT_SEPARATOR)

def format_category_line(category, amount, percentage=None):
    if percentage is not None:
        return f"{category:<{CATEGORY_COLUMN_WIDTH}} {format_currency(amount):>{AMOUNT_COLUMN_WIDTH}} {percentage:>9.1f}%"
    return f"{category:<{CATEGORY_COLUMN_WIDTH}} {format_currency(amount):>{AMOUNT_COLUMN_WIDTH}}"