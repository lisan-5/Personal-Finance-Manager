from modules.utils.console import print_header, print_table, print_warning
from modules.utils.input_validators import validate_date_range
from modules.utils.date_helpers import parse_timestamp

def view_transactions(data):
    print_header("View Transactions")
    
    # Date range selection
    start_date, end_date = validate_date_range()
    
    # Filter and sort transactions
    expenses = [
        {**e, "type": "Expense"} 
        for e in data["expenses"]
        if start_date <= parse_timestamp(e["timestamp"]).date() <= end_date
    ]
    income = [
        {**i, "type": "Income", "category": "Income"} 
        for i in data["income"]
        if start_date <= parse_timestamp(i["timestamp"]).date() <= end_date
    ]
    
    transactions = sorted(
        expenses + income,
        key=lambda x: parse_timestamp(x["timestamp"]),
        reverse=True
    )
    
    if not transactions:
        print_warning("No transactions found for the selected period.")
        return
    
    headers = ["Date", "Type", "Category", "Amount", "Description"]
    rows = []
    for t in transactions:
        date = parse_timestamp(t["timestamp"]).strftime("%Y-%m-%d")
        rows.append([
            date,
            t["type"],
            t["category"],
            f"${t['amount']:.2f}",
            t["description"]
        ])
    
    print_table(headers, rows)