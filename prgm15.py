print("SJC23MCA-2056:TESMOL SHAJI")
print("Batch:MCA 2023-25")
import numpy as np
# Create two 2D arrays
matrix1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix2 = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])
# Add the two matrices
matrix_sum = matrix1 + matrix2
# Subtract the two matrices
matrix_diff = matrix1 - matrix2
# Multiply the individual elements of the matrices
matrix_product = matrix1 * matrix2
# Divide the elements of the matrices
matrix_divide = matrix1 / matrix2
# Perform matrix multiplication
matrix_multiply = np.dot(matrix1, matrix2)
# Display transpose of the matrix
matrix1_transpose = np.transpose(matrix1)
# Sum of diagonal elements of a matrix
diagonal_sum = np.trace(matrix1)
print("Matrix 1:\n", matrix1)
print("Matrix 2:\n", matrix2)
print("Matrix Sum:\n", matrix_sum)
print("Matrix Difference:\n", matrix_diff)
print("Matrix Element-wise Product:\n", matrix_product)
print("Matrix Element-wise Division:\n", matrix_divide)
print("Matrix Multiplication:\n", matrix_multiply)
print("Transpose of Matrix 1:\n", matrix1_transpose)
print("Sum of Diagonal Elements of Matrix 1:", diagonal_sum)