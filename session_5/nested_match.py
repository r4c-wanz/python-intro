print("Welcome to choose a number program!")
print("1. One")
print("2. Two")
print("3. Three")
option = int(input("Choose a number between 1 and 3: "))

match option:
    case 1:
        print("Your number is one.")
        print("1. Apple")
        second_option = int(input("Choose a fruit: "))
        # Match - Case
        # match second_option:
        #     case 1:
        #         print("You choose an apple")

        # If, Elif, Else
        if second_option == 1:
            print("You choose an apple")
    case 2:
        print("Your number is Two.")
        print("1. Carrot")
        second_option = int(input("Choose a vegetables: "))
        match second_option:
            case 1:
                print("You choose a carrot")
    case _:
        print("No one in the list.")
