import os


def go_to_menu():
    input("\nPress enter to go back to menu! ")


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def select():
    while True:
        choice = input("Type 1 for a new file, type 2 to load a file! ")
        if choice in ['1', '2']:
            if choice == '1':
                return
            else:
                load()
        else:
            print("Please type either 1 or 2")

#def load():

def menu():
    print("""Type:
          1 to Add Expenses
          2 to Delete Expenses
          3 to View Expenses
          4 to Calculate Expenses
          5 to Save and Exit\n""")


def choice(): # menu navigation

    while True:
        choice = input("Type your choice: ")

        if choice in ['1', '2', '3', '4', '5']:
            return int(choice)
            break
        else: 
            print("\nPlease select a valid option\n")


def add_expense(dic):
    clear_screen()

    while True:
        name = input("Name of the expense: ").lower().strip() # name
        if len(name) == 0:
            print("Please enter a valid name!")
            continue
        elif name in dic:
            choice = input(f"{name} already exists, do you wanna overwrite? y/n ").lower().strip()
            if choice != "y":
                continue
        break

    while True:
        amount = input("Cost of the Expense: ") # cost

        try:
            amount = float(amount)
            if amount < 0.01:
                print("Please enter a valid Cost!")
                continue
            elif amount > 999999999:
                print("Amount is too large!")
                continue
            if amount.is_integer():
                amount = int(amount)
            print(f"\nAdded Expense: '{name.capitalize()}' of Value: ${amount}!")
            go_to_menu()
            break
        except ValueError:
            print("Please enter a valid Cost!")
            continue

    return name, amount


def del_expense(dic): # dic is the dictionary
    clear_screen()
    dic_list = list(dic.items())
    if len(dic) == 0:
        print("There are no Expenses yet! ")
        go_to_menu()
        return

    view_expenses(dic)
    while True:
        key_to_delete = input("\nWhich Expense do you want to delete? (In number) or type m to go back to the menu ")
        if key_to_delete == "m":
            return
        try:
            key_to_delete = int(key_to_delete)    
        except ValueError:
            print("Please enter an Integer")
            continue
        if 1 <= key_to_delete <= len(dic):
            num_to_delete = dic_list[key_to_delete - 1][0]
            del dic[num_to_delete]
            if len(dic) == 0:
                break
            again = input("\nDo you wanna delete again? y/n ").lower()
                
            if again == 'y':
                continue
            else:
                break
        else:
            print("That Expense does not exist!")

        
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
        if amount.is_integer():
            amount = int(amount)
        else:
            amount = round(amount, 2)
        print(f"{i}. {item.capitalize()}: ${amount}") # no clear screen, by the way, it interferes
        i += 1