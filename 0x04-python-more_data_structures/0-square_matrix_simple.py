#!/usr/bin/python3
def square_matrix_simple(matrix = []):
    if matrix is None:
        print()
    return [[ a * a for a in row] for row in matrix]
