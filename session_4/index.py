print("==== Mini Market ====")
print("1. Fruits")
print("2. Vegetables")
print("3. Meat")

first_option = int(input("Choose the number of list want to buy (1-3): "))

if first_option == 1:
    print("==== Fruits ====")
    print("1. Apple")
    print("2. Banana")
    print("3. Cherry")
    print("4. Strawberry")
    second_option = int(input("Choose the number of fruits want to buy (1-4): "))

    if second_option == 1:
        print("Here your fruit Apple")
    elif second_option == 2:
        print("Here your fruit Banana")
    elif second_option == 3:
        print("Here your fruit Cherry")
    elif second_option == 4:
        print("Here your fruit Strawberry")
    else:
        print("No one in the list. Please check your option!")
elif first_option == 2:
    print("==== Vegetables ====")
    print("1. Broccoli")
    print("2. Cabbage")
    print("3. Onion")
    print("4. Spring Onions")
    second_option = int(input("Choose the number of vegetables want to buy (1-4): "))

    if second_option == 1:
        print("Here your fruit Broccoli")
    elif second_option == 2:
        print("Here your fruit Cabbage")
    elif second_option == 3:
        print("Here your fruit Onion")
    elif second_option == 4:
        print("Here your fruit Spring Onions")
    else:
        print("No one in the list. Please check your option!")
elif first_option == 3:
    print("==== Meat ====")
    print("1. Chicken")
    print("2. Beef")
    print("3. Turkey")
    print("4. Fish")
    second_option = int(input("Choose the number of vegetables want to buy (1-4): "))

    if second_option == 1:
        print("Here your fruit Chicken")
    elif second_option == 2:
        print("Here your fruit Beef")
    elif second_option == 3:
        print("Here your fruit Turkey")
    elif second_option == 4:
        print("Here your fruit Fish")
    else:
        print("No one in the list. Please check your option!")
else:
    print("No one in the list. Please check your option!")
