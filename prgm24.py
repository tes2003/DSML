print("SJC23MCA-2056:TESMOL SHAJI")
print("Batch:MCA 2023-25")
import numpy as np
# Function to check if a matrix is symmetric
def is_symmetric(matrix):
 return (matrix == matrix.T).all()
# Function to check if a matrix is skew-symmetric
def is_skew_symmetric(matrix):
 return (matrix == -matrix.T).all()
# Define a matrix
matrix = np.array([[0, 1, -2],
[-1, 0, 3],
[2, -3, 0]])

# Check if the matrix is symmetric or skew-symmetric
if is_symmetric(matrix):
 print("The matrix is symmetric.")
elif is_skew_symmetric(matrix):
 print("The matrix is skew-symmetric.")
else:
 print("The matrix is neither symmetric nor skew-symmetric.")