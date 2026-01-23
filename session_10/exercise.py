matrix = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
]

print(f"Element in row 2, column 3: {matrix[1][2]}")

matrix[1][1] = 0

print("Matrix update results:")
for row in matrix:
    for column in row:
        print(column, end="     ")
    print()
