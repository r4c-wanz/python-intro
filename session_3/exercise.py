# Simple calculator using input number, match case and if, elif, else

print("=== Calculator ===")
print("1. Plus (+)")
print("2. Minus (-)")
print("3. Times (*)")
print("4. Division (/)")

option = int(input("Choose an operation (1-4): "))

first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))

match option:
    case 1:
        print("Result:", first_number + second_number)
    case 2:
        print("Result:", first_number - second_number)
    case 3:
        print("Result:", first_number * second_number)
    case 4:
        print("Result:", first_number / second_number)
