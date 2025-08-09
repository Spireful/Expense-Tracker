import os


def go_to_menu():
    input("\nPress enter to go back to menu! ")


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def menu():
    print("""\nType:
          1 to Add Expenses
          2 to Delete Expenses
          3 to View Expenses
          4 to Calculate Expenses
          5 to Exit""")


def choice(): # menu navigation

    while True:
        choice = input("\nType your choice: ")

        if choice in ['1', '2', '3', '4', '5']:
            return int(choice)
            break
        else: 
            menu()


def add_expense():
    clear_screen()

    while True:
        name = input("\nName of the expense: ").lower().strip() # name
        if len(name) == 0:
            print("Please enter a valid name!")
        else:
            break

    while True:
        amount = input("Cost of the expense: ") # cost
        try:
            amount = float(amount)
            if amount.is_integer():
                amount = int(amount)
                print(f"\nAdded Expense: '{name.capitalize()}' of Value: ${amount}!")
                go_to_menu()
                break
        except ValueError:
            print("Please enter an Integer")
            continue

    return name, amount


def del_expense(dic): # dic is the dictionary
    clear_screen()

    if len(dic) == 0:
        print("There are no Expenses yet! ")
        go_to_menu()
        return

    view_expenses(dic)
    while True:
        input_delete = input("\nWhich expense do you want to delete?\n(Type m to back to menu) ").lower() # what they want to delete
            
        if input_delete in dic:
            del dic[input_delete]
            again = input("Do you wanna delete again? y for yes, anything else for no").lower()
                
            if again == 'y':
                continue
            else:
                break
            
        elif input_delete == "m":
            return
        else:
            print("That expense does not exist")

    return dic


def calc_expenses(dic): # takes dic
    clear_screen()

    if len(dic) == 0:
        print("There are no Expenses yet! ")
        go_to_menu()
        return
        
    
    all = round(sum(dic.values()), 2) # sums all value
    if all.is_integer(): # if its an empty float
        all = int(all) # converts into int

    print("Value: $" + str(all)) # converts into string for combination
    go_to_menu()

def view_expenses(dic):
    clear_screen()

    if len(dic) == 0:
        print("There are no Expenses yet! ")
        return
    
    print("Expenses: \n")
    i = 1
    for item, amount in dic.items():
        print(f"{i}. {item.capitalize()}: ${amount:.2f}") # no clear screen, by the way, it interferes
        i += 1