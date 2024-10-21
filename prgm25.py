print("SJC23MCA-2056:TESMOL SHAJI")
print("Batch:MCA 2023-25")
import numpy as np
# Define matrix A and vector b
A = np.array([[2, 1,-2],[3,0,1],[1,1,-1]])
b = np.array([-3,5,-2])
# Solve for X using the solve() function
X = np.linalg.solve(A, b)
print("Matrix A:")
print(A)
print("Vector b:")
print(b)
print("Solution for X:")
print(X)