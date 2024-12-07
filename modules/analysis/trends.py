from modules.utils.console import print_header, print_table
from modules.utils.calculations import calculate_monthly_trends
from modules.utils.date_helpers import parse_timestamp

def analyze_trends(data):
    print_header("Financial Trends Analysis")
    
    # Calculate monthly trends
    trends = calculate_monthly_trends(data["expenses"], data["income"])
    
    if not trends:
        print("\nNo data available for trend analysis.")
        return
    
    # Display monthly summary
    headers = ["Month", "Income", "Expenses", "Net", "Top Category", "Category Amount"]
    rows = []
    
    for month, stats in trends.items():
        rows.append([
            month,
            f"${stats['income']:.2f}",
            f"${stats['expenses']:.2f}",
            f"${stats['net']:.2f}",
            stats['top_category'],
            f"${stats['top_amount']:.2f}"
        ])
    
    print_table(headers, rows)