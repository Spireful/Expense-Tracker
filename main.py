from utility import menu, choice, add_expense, del_expense, clear_screen, calc_expenses, go_to_menu
from utility import view_expenses
print("\nWelcome to the Expense Tracker!")

expenses = {}

while True:
    clear_screen()
    menu()
    user_choice = choice()

    if user_choice == 1:
        name, cost = add_expense()
        expenses[name] = cost
    elif user_choice == 2:
        del_expense(expenses)
    elif user_choice == 3:
        view_expenses(expenses)
        go_to_menu()
    elif user_choice == 4:
        calc_expenses(expenses)
    else:
        clear_screen()
        print("Thank you for using the Expense Tracker!\n")
        break