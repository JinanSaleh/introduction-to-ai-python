# Expense Tracker Project

def show_expenses(expenses):
    print("\n--- Your Expenses ---")
    if not expenses:
        print("No expenses recorded yet.")
        return 0
    
    total = 0
    for i, item in enumerate(expenses, 1):
        print(f"{i}. {item['category']}: ${item['amount']:.2f}")
        total += item['amount']
    
    print(f"Total Spent: ${total:.2f}")
    return total

def main():
    expenses = []
    
    while True:
        print("\n=== Expense Tracker Menu ===")
        print("1. Add an expense")
        print("2. View all expenses")
        print("3. Exit")
        
        choice = input("Choose an option (1-3): ")
        
        if choice == '1':
            category = input("Enter expense category (e.g., Food, Transport): ")
            try:
                amount = float(input("Enter amount ($): "))
                if amount < 0:
                    print("Amount cannot be negative.")
                    continue
                # Store the expense as a dictionary inside a list
                expenses.append({"category": category, "amount": amount})
                print("Expense added successfully!")
            except ValueError:
                print("Invalid amount. Please enter a number.")
                
        elif choice == '2':
            show_expenses(expenses)
            
        elif choice == '3':
            print("Exiting Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose 1, 2, or 3.")

# Run the program
if __name__ == "__main__":
    main()
