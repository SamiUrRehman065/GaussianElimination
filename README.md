# 🧮 GaussianElimination: Linear System Solver

## 📌 Overview

**GaussianElimination** is a Python project that implements **Gaussian Elimination** to solve linear systems of equations.

It allows you to:

* Transform a system into **row echelon form**
* Perform **back substitution** to get the solution
* Detect **singular systems** (no unique solution)
* Handle **regular systems** (unique solution)

Built with **Python** and **NumPy**, this project provides a **modular structure** separating **algorithms**, **utility functions**, and **test cases**.

---

## ✨ Key Features

### 🔹 Row Echelon Form

* Converts an augmented matrix `[A|B]` into **row echelon form**
* Normalizes pivots to **1**
* Applies **row operations** for clarity and accuracy

### 🔹 Back Substitution

* Extracts the solution vector from row echelon form
* Handles equations from **bottom-up**
* Ensures correctness for non-singular systems

### 🔹 Full Gaussian Elimination

* Combines **row echelon form** and **back substitution**
* Automatically checks for **singular systems**
* Returns solution vector for regular systems

### 🔹 Test Cases

* Includes multiple **regular and singular systems**
* Demonstrates edge cases and unique solution handling
* Easy to extend with your own equations

---

## 🧱 Project Structure

```
GaussianElimination/
│
├── gaussian_elimination.py       # Core algorithms: row echelon, back substitution, full Gaussian elimination
├── utils.py                       # Helper functions for parsing string equations into matrices
├── test_cases.py                  # Multiple test cases (regular & singular systems)
├── README.md                      # Project documentation
└── requirements.txt               # Python dependencies (numpy, sympy)
```

---

## 🧮 Module Breakdown

| Module                    | Purpose                                               |     |
| ------------------------- | ----------------------------------------------------- | --- |
| `gaussian_elimination.py` | Implements Gaussian elimination logic                 |     |
| `utils.py`                | Converts string equations into augmented matrices `[A | B]` |
| `test_cases.py`           | Contains multiple test systems for validation         |     |
| `requirements.txt`        | Lists Python dependencies                             |     |

---

## 🖥️ How It Works

### 🔹 Solving a System

1. Write equations as strings:

```python
equations = """
3*x + 6*y + 6*w + 8*z = 1
5*x + 3*y + 6*w = -10
4*y - 5*w + 8*z = 8
4*w + 8*z = 9
"""
```

2. Convert equations into **augmented matrices**:

```python
variables, A, B = string_to_augmented_matrix(equations)
```

3. Solve using **Gaussian elimination**:

```python
solutions = gaussian_elimination(A, B)
```

4. Print results:

```python
for var, sol in zip(variables.split(' '), solutions):
    print(f"{var} = {sol:.4f}")
```

### 🔹 Handling Singular Systems

* If the determinant of the coefficient matrix is zero, the system is **singular**.
* The algorithm automatically returns `"Singular system"`.

---

## 🖥️ Technologies Used

| Technology | Role                                     |
| ---------- | ---------------------------------------- |
| Python     | Backend scripting and computation        |
| NumPy      | Matrix operations and numerical handling |
| SymPy      | Parsing algebraic expressions            |

---

## 🚀 How to Run Locally

1. Clone the repo:

```bash
git clone https://github.com/SamiUrRehman065/GaussianElimination.git
cd GaussianElimination
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the main solver:

```bash
python gaussian_elimination.py
```

4. Run all test cases:

```bash
python test_cases.py
```

---

## ⚠️ Notes

* Works for **Python 3.8+**
* Handles both **unique and singular systems**
* Modular code allows **easy extension** for larger systems

---

## 🧑‍💻 Author

**Name:** Sami Ur Rehman  
**Location:** Karachi, Pakistan  
**GitHub:** [SamiUrRehman065](https://github.com/SamiUrRehman065)

---

## 🪞 Developer Reflection

### What I Learned

* Implementation of **Gaussian elimination** from scratch
* Handling edge cases like singular systems
* Modularizing algorithms and utility functions
* Writing **clear test cases** for multiple systems

### Challenges

* Managing floating-point precision in row operations
* Ensuring correct pivot selection for row echelon form
* Handling singular matrices gracefully

### Solutions

* Used `np.isclose` for float comparisons
* Added helper functions for row operations and pivot detection
* Implemented test cases for **regular and singular systems**

---

## 🤝 Contributing

Contributions welcome! 🎉
Feel free to open issues or submit PRs for new features, bug fixes, or improvements.


