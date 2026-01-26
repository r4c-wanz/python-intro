items = []

while True:
    print("==== Restaurant ====")
    print("1. Show menu")
    print("2. Add menu")
    print("3. Edit menu")
    print("4. Delete menu")
    print("5. Exit")
    option = int(input("Choose the number, what you want to do (1-5): "))
    if option > 5:
        print("The number is not allowed. Please enter the number between 1 to 5.")
        break
    elif option == 5:
        print("Exit the program.")
        break

    if option == 1:
        if items:
            print("==== Menu ====")
            number = 1
            for x in items:
                print(f"{number}. {x}")
                number += 1
        else:
            print("Items is empty.")
    elif option == 2:
        if items:
            print("==== Menu ====")
            number = 1
            for x in items:
                print(f"{number}. {x}")
                number += 1
        else:
            print("Items is empty.")

        second_option = input("Do you want to add items [y/n](default y): ") or "y"
        if second_option == "y" or second_option == "yes":
            item_add = input("What the name item you want to add: ")
            items.append(item_add)
        else:
            print("Exit add menu.")
    elif option == 3:
        if items:
            print("==== Menu ====")
            number = 1
            for x in items:
                print(f"{number}. {x}")
                number += 1
            second_option = input("Do you want to edit items [y/n](default y): ") or "y"
            if second_option == "y" or second_option == "yes":
                idx = int(input("Choose the number you want to edit: "))
                new_item = input("What the name item you want to add: ")
                items[idx - 1] = new_item
            else:
                print("Exit edit menu.")
        else:
            print("Items is empty. You cannot edit anything.")
    elif option == 4:
        if items:
            print("==== Menu ====")
            number = 1
            for x in items:
                print(f"{number}. {x}")
                number += 1
            second_option = input("Do you want to delete items [y/n](default y): ") or "y"
        else:
            print("Items is empty. You cannot delete anything.")
