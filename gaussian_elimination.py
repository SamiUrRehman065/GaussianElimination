"""
gaussian_elimination.py
-----------------------
This file implements Gaussian Elimination for solving linear systems.
It includes:
1. Auxiliary functions
2. Row echelon form
3. Back substitution
4. Full Gaussian elimination

Author: Your Name
Course: Math for Machine Learning and Data Science (Coursera)
"""

import numpy as np
from utils import string_to_augmented_matrix

# -----------------------------
# Auxiliary Functions
# -----------------------------

def swap_rows(M, row_index_1, row_index_2):
    """
    Swap two rows of a matrix without modifying the original.
    """
    M = M.copy()
    M[[row_index_1, row_index_2]] = M[[row_index_2, row_index_1]]
    return M

def get_index_first_non_zero_value_from_column(M, column, starting_row):
    """
    Return index of the first non-zero value in a column starting from a row.
    Returns -1 if all values are zero.
    """
    column_array = M[starting_row:, column]
    for i, val in enumerate(column_array):
        if not np.isclose(val, 0, atol=1e-5):
            return i + starting_row
    return -1

def get_index_first_non_zero_value_from_row(M, row, augmented=False):
    """
    Return index of the first non-zero element in a row.
    If augmented=True, last column is ignored.
    """
    M = M.copy()
    if augmented:
        M = M[:, :-1]
    row_array = M[row]
    for i, val in enumerate(row_array):
        if not np.isclose(val, 0, atol=1e-5):
            return i
    return -1

def augmented_matrix(A, B):
    """
    Horizontally stack coefficient matrix A and constants B.
    """
    return np.hstack((A, B))

# -----------------------------
# Row Echelon Form
# -----------------------------
def row_echelon_form(A, B):
    """
    Transform matrices A, B into row echelon form with pivots as 1.
    """
    det_A = np.linalg.det(A)
    if np.isclose(det_A, 0):
        return 'Singular system'

    A = A.copy().astype('float64')
    B = B.copy().astype('float64')
    M = augmented_matrix(A, B)
    num_rows = len(A)

    for row in range(num_rows):
        pivot_candidate = M[row, row]
        if np.isclose(pivot_candidate, 0):
            idx = get_index_first_non_zero_value_from_column(M, row, row)
            if idx == -1:
                return 'Singular system'
            M = swap_rows(M, row, idx)
            pivot_candidate = M[row, row]

        pivot = pivot_candidate
        M[row] = (1 / pivot) * M[row]

        for j in range(row + 1, num_rows):
            value_below_pivot = M[j, row]
            M[j] = M[j] - value_below_pivot * M[row]

    return M

# -----------------------------
# Back Substitution
# -----------------------------
def back_substitution(M):
    """
    Perform back substitution on a row-echelon matrix to get solution vector.
    """
    M = M.copy()
    num_rows = M.shape[0]

    for row in reversed(range(num_rows)):
        substitution_row = M[row]
        index = get_index_first_non_zero_value_from_row(M, row, augmented=True)
        if index == -1:
            continue
        for j in range(row):
            row_to_reduce = M[j]
            value = row_to_reduce[index]
            M[j] = row_to_reduce - value * substitution_row

    solution = M[:, -1]
    return solution

# -----------------------------
# Full Gaussian Elimination
# -----------------------------
def gaussian_elimination(A, B):
    """
    Solve a linear system using Gaussian elimination.
    """
    row_echelon_M = row_echelon_form(A, B)
    if isinstance(row_echelon_M, str):
        return row_echelon_M
    solution = back_substitution(row_echelon_M)
    return solution

# -----------------------------
# Quick Test
# -----------------------------
if __name__ == "__main__":
    equations = """
    3*x + 6*y + 6*w + 8*z = 1
    5*x + 3*y + 6*w = -10
    4*y - 5*w + 8*z = 8
    4*w + 8*z = 9
    """
    variables, A, B = string_to_augmented_matrix(equations)
    sols = gaussian_elimination(A, B)
    if not isinstance(sols, str):
        for variable, solution in zip(variables.split(' '), sols):
            print(f"{variable} = {solution:.4f}")
    else:
        print(sols)
