import random
import numpy

m = int(input("The size of the square matrix: "))
matrix = numpy.array([[random.randint(0, 99) for _ in range(m)] for _ in range(m)])
print("The generated matrix:")
print(matrix)

def counterclockwise_traverse(mat):
    if len(mat) == 1:
        return [mat[0][0]]
    path = []
    path.extend(mat[:,0])
    path.extend(mat[-1, 1:-1])
    path.extend(mat[::-1,-1])
    path.extend(mat[0, -2:0:-1])
    path.extend(counterclockwise_traverse(mat[1:-1, 1:-1]))
    return path

path = ", ".join(str(item) for item in counterclockwise_traverse(matrix))
print(f"Matrix traversed counterclockwise: {path}")
