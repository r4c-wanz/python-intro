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
        print(items)
