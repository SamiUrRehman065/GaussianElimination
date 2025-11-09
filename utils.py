"""
utils.py
--------
Helper functions for Gaussian Elimination assignment.
Includes a function to convert string equations into augmented matrices.
"""

import numpy as np
from sympy import sympify

def string_to_augmented_matrix(equations):
    """
    Converts string equations to augmented matrix (A|B) and variable list.
    """
    equations = equations.strip().split('\n')
    variables = set()

    # Extract all variable names
    for eq in equations:
        lhs = eq.split('=')[0]
        lhs = lhs.replace('*', '')
        for char in lhs:
            if char.isalpha():
                variables.add(char)
    variables = ' '.join(sorted(list(variables)))

    # Build coefficient matrix A and constants B
    A = []
    B = []
    var_list = variables.split(' ')

    for eq in equations:
        sides = eq.split('=')
        left_side = sympify(sides[0])
        right_side = float(sides[1])
        coeffs = [float(left_side.coeff(var)) for var in var_list]
        A.append(coeffs)
        B.append([right_side])

    return variables, np.array(A, dtype='float64'), np.array(B, dtype='float64')
