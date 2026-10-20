#!/usr/bin/env python3
def print_matrix_integer(matrix=[[]]):
    """Print a matrix of integers, one row per line, space separated."""
    for row in matrix:
        for i in range(len(row)):
            if i != 0:
                print(" ", end="")
            print("{:d}".format(row[i]), end="")
        print()
