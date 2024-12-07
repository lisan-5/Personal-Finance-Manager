from modules.utils.console import print_header, print_warning, print_success
from modules.database.core import save_data

def manage_categories(data):
    print_header("Manage Categories")
    
    while True:
        print("\n1. View Categories")
        print("2. Add Category")
        print("3. Remove Category")
        print("4. Back to Main Menu")
        
        choice = input("\nEnter your choice (1-4): ")
        
        if choice == "1":
            _view_categories(data["categories"])
        elif choice == "2":
            _add_category(data)
        elif choice == "3":
            _remove_category(data)
        elif choice == "4":
            break
        else:
            print("\nInvalid choice. Please try again.")

def _view_categories(categories):
    print("\nCurrent Categories:")
    for i, category in enumerate(categories, 1):
        print(f"{i}. {category}")

def _add_category(data):
    new_category = input("\nEnter new category name: ").strip()
    
    if not new_category:
        print_warning("Category name cannot be empty.")
        return
    
    if new_category in data["categories"]:
        print_warning("Category already exists.")
        return
    
    data["categories"].append(new_category)
    save_data(data)
    print_success("Category added successfully!")

def _remove_category(data):
    _view_categories(data["categories"])
    
    try:
        choice = int(input("\nEnter category number to remove: "))
        if 1 <= choice <= len(data["categories"]):
            category = data["categories"][choice - 1]
            
            # Check if category is in use
            in_use = any(e["category"] == category for e in data["expenses"])
            
            if in_use:
                print_warning("Cannot remove category that is in use.")
                return
            
            data["categories"].pop(choice - 1)
            
            # Remove from budget if exists
            if category in data["budget"]:
                del data["budget"][category]
            
            save_data(data)
            print_success("Category removed successfully!")
        else:
            print_warning("Invalid category number.")
    except ValueError:
        print_warning("Please enter a valid number.")