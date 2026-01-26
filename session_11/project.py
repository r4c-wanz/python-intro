option = 1

while option != 5:
    print("=== Mini School Shop ===") 
    print("1. Stationary Items")
    print("2. Snacks")
    print("3. Drinks")
    print("4. Hiegene Products")
    print("5. Exit")
    option = int(input("Choose the item you want to buy (1-5): "))
    if option > 5:
        print("Its not allowed. Please input between 1 to 5.")

    if option == 1:
        print("=== STATIONARY ITEMS ===")
        print("1. Pencil")
        print("2. Notebook")
        print("3. Ruler")
        print("4. Erasor")
        second_option = int(input("Choose the number of stationary item you want to buy (1-4): "))

        if second_option == 1:
            print("You have chosen | pencil |")
        elif second_option == 2:
            print("You have chosen | Notebook |")
        elif second_option == 3:
            print("You have chosen | Ruler |")
        elif second_option == 4:
            print("You have chosen | Erasor |")
        else:
            print("This option is not available, Try Again !")

    elif option == 2:
        print("=== SNACKS ===")
        print("1. Chips")
        print("2. Popcorn")
        print("3. Chocolate")
        print("4. Cookies")
        second_option = int(input("Choose the number of snack you want to buy (1-4): "))

        if second_option == 1:
            print("You have chosen | Chips |")
        elif second_option == 2:
            print("You have chosen | Popcorn |")
        elif second_option == 3:
            print("You have chosen | Chocolate |")
        elif second_option == 4:
            print("You have chosen | Cookies |")
        else:
            print("This option is not available, Try Again !")

    elif option == 3:
        print("=== DRINKS ===")
        print("1. Soda")
        print("2. Milk")
        print("3. Water")
        print("4. Juice")
        second_option = int(input("Choose the number of drink you want to buy (1-4): "))

        if second_option == 1:
            print("You have chosen | Soda |")
        elif second_option == 2:
            print("You have chosen | Milk |")
        elif second_option == 3:
            print("You have chosen | Water |")
        elif second_option == 4:
            print("You have chosen | Juice |")
        else:
            print("This option is not available, Try Again !")

    elif option == 4:
        print("=== HIEGENE PRODUCTS ===")
        print("1. Tissues")
        print("2. Sanitizer")
        print("3. Sunscreen")
        print("4. Face Mask")
        second_option = int(input("Choose the number of Product you want to buy (1-4): "))

        if second_option == 1:
            print("You have chosen | Tissues |")
        elif second_option == 2:
            print("You have chosen | Sanitizer |")
        elif second_option == 3:
            print("You have chosen | Sunscreen |")
        elif second_option == 4:
            print("You have chosen | Face Mask |")
        else:
            print("This option is not available, Try Again !")
