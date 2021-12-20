import random
import functools
import pprint

m = int(input("The number of rows in the matrix: "))
n = int(input("The number of columns in the matrix: "))
matrix = [[random.randint(1, 99) for _ in range(n)] for _ in range(m)]
print("The generated matrix:")
pprint.pp(matrix)
first_column = 0
for i, column in enumerate(zip(*matrix)):
    if all(element % 2 == 1 for element in column):
        first_column = i+1
        break
print(f"The first column where all elements are odd is the column number {first_column}")
