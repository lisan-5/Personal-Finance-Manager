from modules.core import FinanceTracker
from modules.utils.console import clear_screen, print_header

def main():
    tracker = FinanceTracker()
    
    while True:
        clear_screen()
        print_header("Personal Finance Tracker")
        tracker.display_menu()
        choice = input("\nEnter your choice (1-9): ")
        
        clear_screen()
        if choice == "1":
            tracker.add_expense()
        elif choice == "2":
            tracker.add_income()
        elif choice == "3":
            tracker.generate_report()
        elif choice == "4":
            tracker.set_budget()
        elif choice == "5":
            tracker.export_data()
        elif choice == "6":
            tracker.view_transactions()
        elif choice == "7":
            tracker.manage_categories()
        elif choice == "8":
            tracker.analyze_trends()
        elif choice == "9":
            print("\nThank you for using Personal Finance Tracker!")
            break
        else:
            print("\nInvalid choice. Please try again.")
        
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()