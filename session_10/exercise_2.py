answer = 1

while answer != 5:
    answer = int(input("Enter the number between 1 to 4 (5 to exit): "))
    if answer > 5:
        print("Its not allowed. Please input between 1 to 4.")
