print("==== Menu ====")
print("1. Show menu")
print("2. Add menu")
print("3. Edit menu")
print("4. Delete menu")
option = int(input("Choose the number (1-4): "))

menu = []

match option:
    case 1:
        print(menu)
    case 2:
        item = input("Enter the menu what you want to add: ")
        menu.append(item)
        print(menu)
    case 3:
        number = 1
        for x in menu:
            print(number, x)
            number += 1
        if menu:
            item = input("Enter the menu what you want to edit: ")
        else:
            print("No items in the list.")
    case 4:
        print(menu)
        if menu:
            item = input("Enter the menu what you want to delete: ")
        else:
            print("No items in the list.")
