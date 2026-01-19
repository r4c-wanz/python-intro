# Nested while Loop
# i = 1

# while rows <= 3:
#     columns = 1
#     while columns <= 3:
#         columns_3 = 1
#         while columns_3 <= 3:
#             print(rows, columns, columns_3)
#             columns_3 += 1
#         columns += 1
#     rows += 1

# Outer loop (Controls Rows)
# while i <= 3:
#     # Inner loop (Controls Columns/Items in a Row)
#     j = 1
#     while j <= 3:
#         print(i, j) # (1, 1), (1, 2), (1, 3) ... (3, 3)
#         j += 1
#     i += 1

star = int(input("How many stars do you want: "))
level = int(input("How many levels do you want: "))

i = 1

while i <= star:
    j = 1
    while j <= level:
        print("*" * i)
        j += 1
    i += 1

