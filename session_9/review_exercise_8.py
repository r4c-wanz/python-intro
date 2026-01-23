answer = 1

menu = []

while answer != 5:
    print("==== Menu ====")
    print("1. Show menu")
    print("2. Add menu")
    print("3. Edit menu")
    print("4. Delete menu")
    print("5. Exit")
    option = int(input("Choose the number (1-5): "))

    match option:
        case 1:
            if menu:
                print("==== Menu List ====")
                for idx, item in enumerate(menu, start=1):
                    print(f"{idx}. {item}")
                else:
                    print("=" * 19)
            else:
                print("Menu is empty.")
            print()
        case 2:
            if menu:
                print("==== Menu List ====")
                for idx, item in enumerate(menu, start=1):
                    print(f"{idx}. {item}")
                else:
                    print("=" * 19)
            else:
                print("Menu is empty.")

            option_add = input("Do you want to add new menu [y/n](default: n): ") or "n"
            if option_add == "y":
                value = input("Enter the name of menu you want to add: ")
                menu.append(value)
            elif 2:
                print()
                continue
            print()
        case 3:
            if menu:
                print("==== Menu List ====")
                for idx, item in enumerate(menu, start=1):
                    print(f"{idx}. {item}")
                else:
                    print("=" * 19)

                option_edit = input("Do you want to edit the menu [y/n](default: n): ") or "n"
                if option_edit == "y":
                    value = input("Enter the new menu you want to add: ")
                    idx = int(input("Choose the index number: "))
                    menu[idx] = value
                elif 2:
                    print()
                    continue
            else:
                print("Menu is empty, you can't edit the menu.")
            print()
        case 4:
            print(menu)
            idx = int(input("Choose the index number: "))
            menu.pop(idx)
            print()
        case 5:
            answer = 5
else:
    print("Exit this program.")
    print()
