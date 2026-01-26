option = 1

while option != 5:
    option = int(input("Choose the number between 1 to 5 (5 - Exit): "))
    if option > 5:
        print("The number is not allowed. Please enter the number between 1 to 5.")
        break
    elif option == 5:
        print("Exit the program.")
