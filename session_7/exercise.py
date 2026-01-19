# Create Python Pyramid using Nested For
# Output:
# n = 5
#         *
#       * *
#     * * *
#   * * * *
# * * * * *

n = 5

# for i in range(1, n + 1):
#     for j in range(1, n - i + 1):
#         print(" ", end=" ")
#     for k in range(1, i + 1):
#         print("*", end=" ")
#     print()

# for i in range(1, n + 1):
#     for j in range(1, n - i + 1):
#         print(i, end=" ")
#     for k in range(1, i + 1):
#         print("*", end=" ")
#     print()

# Create Python Pyramid using Nested For
# Output:
# n = 5
# * * * * *
#   * * * *
#     * * *
#       * *
#         *

for i in range(1, n + 1):
    for j in range(1, i):
        print(" ", end=" ")
    for k in range(1, n - i + 2):
        print("*", end=" ")
    print()
