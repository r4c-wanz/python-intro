# Looping (while - for)
number = 0

while number <= 10:
    number = number + 1
    if number == 5:
        # break # Stop
        continue # Skip
    print(number, number <= 10)
else:
    print("The while loop is finished.")
