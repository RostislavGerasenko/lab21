import random
import functools
import pprint

m = int(input("The number of rows in the matrix: "))
n = int(input("The number of columns in the matrix: "))
matrix = [[random.randint(1, 99) for _ in range(n)] for _ in range(m)]
print("The generated matrix:")
pprint.pp(matrix)
least_column = -1
min_product = float("inf")
for i, column in enumerate(zip(*matrix)):
    product = functools.reduce(lambda x, y: x * y, column)
    if product < min_product:
        min_product = product
        least_column = i
print(f"The column with the smallest product ({min_product}) is the column number {least_column + 1}")
