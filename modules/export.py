import csv
from modules.utils.date_helpers import get_export_timestamp

def export_data(data):
    timestamp = get_export_timestamp()
    
    # Export expenses
    with open(f'expenses_{timestamp}.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Timestamp', 'Category', 'Amount', 'Description'])
        for expense in data['expenses']:
            writer.writerow([
                expense['timestamp'],
                expense['category'],
                expense['amount'],
                expense['description']
            ])
    
    # Export income
    with open(f'income_{timestamp}.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Timestamp', 'Amount', 'Description'])
        for income in data['income']:
            writer.writerow([
                income['timestamp'],
                income['amount'],
                income['description']
            ])
    
    print(f"\nData exported successfully!")
    print(f"Expenses: expenses_{timestamp}.csv")
    print(f"Income: income_{timestamp}.csv")