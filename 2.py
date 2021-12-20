import random
import functools
import pprint

m = int(input("The number of rows in the matrix: "))
n = int(input("The number of columns in the matrix: "))
matrix = [[random.randint(0, 99) for _ in range(n)] for _ in range(m)]
print("The generated matrix:")
pprint.pp(matrix)
k = int(input("The number of the row to work with: "))
s = sum(matrix[k])
p = functools.reduce(lambda x, y: x*y, matrix[k])
print(f"The sum of row {k} is {s}, the product is {p}")
