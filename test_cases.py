"""
test_cases.py
-------------
Run multiple test cases for Gaussian elimination, including singular and regular systems.
"""

from gaussian_elimination import gaussian_elimination
from utils import string_to_augmented_matrix

def run_test(equations, test_case_name):
    """
    Run Gaussian elimination on a given set of equations and print results.
    """
    print(f"\n--- {test_case_name} ---")
    variables, A, B = string_to_augmented_matrix(equations)
    sols = gaussian_elimination(A, B)

    if isinstance(sols, str):  # Singular system
        print(f"{test_case_name} result: {sols}")
    else:
        var_list = variables.split(' ')
        for var, val in zip(var_list, sols):
            print(f"{var} = {val:.4f}")

# -----------------------------
# Test Cases
# -----------------------------

# 1. Regular 4x4 system
equations1 = """
3*x + 6*y + 6*w + 8*z = 1
5*x + 3*y + 6*w = -10
4*y - 5*w + 8*z = 8
4*w + 8*z = 9
"""
run_test(equations1, "Test Case 1: Regular 4x4 system")

# 2. Singular system (infinite solutions)
equations2 = """
x + y + z = 3
2*x + 2*y + 2*z = 6
x - y + z = 2
"""
run_test(equations2, "Test Case 2: Singular system (infinite solutions)")

# 3. Regular 3x3 system
equations3 = """
2*x + y - z = 1
-3*x - y + 2*z = -4
-2*x + y + 2*z = -2
"""
run_test(equations3, "Test Case 3: Regular 3x3 system")

# 4. Larger 5x5 system
equations4 = """
x + y + z + w + v = 10
2*x - y + z - w + 2*v = 8
-x + 3*y - z + 2*w - v = 3
3*x + y + w + v = 7
x - 2*y + z + 3*w - v = 4
"""
run_test(equations4, "Test Case 4: Larger 5x5 system")

# 5. Singular 3x3 system (no solution)
equations5 = """
x + y + z = 1
x + y + z = 2
2*x - y + z = 0
"""
run_test(equations5, "Test Case 5: Singular system (no solution)")

# 6. Regular 2x2 system
equations6 = """
x + y = 3
2*x - y = 0
"""
run_test(equations6, "Test Case 6: Regular 2x2 system")

# 7. Regular 3x3 with negative numbers
equations7 = """
-x + 2*y - z = 0
2*x - y + z = 3
3*x - y - 2*z = -4
"""
run_test(equations7, "Test Case 7: 3x3 system with negatives")

# 8. Singular 2x2 (infinite solutions)
equations8 = """
x + y = 2
2*x + 2*y = 4
"""
run_test(equations8, "Test Case 8: Singular 2x2 system (infinite solutions)")

# 9. Inconsistent 2x2 (no solution)
equations9 = """
x + y = 1
x + y = 2
"""
run_test(equations9, "Test Case 9: Inconsistent 2x2 system (no solution)")

# 10. 4x4 system with zeros
equations10 = """
x + y + z + w = 4
x - y + 2*z - w = 1
0*x + y + z + 2*w = 5
x + 0*y - z + w = 2
"""
run_test(equations10, "Test Case 10: 4x4 system with zeros")

# 11. 3x3 system with all negative solutions
equations11 = """
-2*x + y - z = -3
x - 3*y + z = -4
3*x - y - 2*z = -1
"""
run_test(equations11, "Test Case 11: 3x3 system with all negative solutions")
