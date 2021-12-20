import random
import functools
import pprint

m = int(input("The number of rows in the matrix: "))
n = int(input("The number of columns in the matrix: "))
matrix = [[random.randint(1, 99) for _ in range(n)] for _ in range(m)]
print("The generated matrix:")
pprint.pp(matrix)
for i, column in enumerate(zip(*matrix)):
    elements = list(column)
    average = sum(column) / len(column)
    print(f"In row {i+1} there are {[element > average for element in elements].count(True)} elements above the mean")
