#!/usr/bin/python3
""" Module to rotate a 2d matrix in python
"""


def rotate_2d_matrix(matrix):
    """ Function to rotate a 2 d matrix in place
    """
    n = len(matrix)
    
    for layer in range(n // 2):
        first = layer
        last = n - layer - 1
        for i in range(first, last):
            # Save the top element
            top = matrix[first][i]
            
            # Move left element to top
            matrix[first][i] = matrix[-(i + 1)][first]
            
            # Move bottom element to left
            matrix[-(i + 1)][first] = matrix[last][-(i + 1)]
            
            # Move right element to bottom
            matrix[last][-(i + 1)] = matrix[i][last]
            
            # Assign top element to right
            matrix[i][last] = top
