print("SJC23MCA-2056:TESMOL SHAJI")
print("Batch:MCA 2023-25")
import numpy as np
# Define matrix A with dimensions 5x6
A = np.array([[1,2,3,4,5,6],
[7,8,9,10,11,12],
[13,14,15,16,17,18],
[19,20,21,22,23,24],
[25,26,27,28,29,30]])

print("Matrix A is : ")
print(A)
# Define matrix B with dimensions 3x3
B = np.array([[1,2,3,],[4,5,6],[7,8,9]])
print("Matrix B is : ")
print(B)
# Extract a 3x3 sub-matrix from A, for example, the top-left sub-matrix
sub_matrix = A[:3, :3]
print("The sub matrix is ")
print(sub_matrix)
# Multiply the sub-matrix with matrix B
result = np.dot(sub_matrix,B)
print("Matrix after multiplication with the sub matrix of A an d matrix B")
print(result)
# Replace the extracted sub-matrix in A with the result
A[:3, :3] = result
print("Matrix A after the operation:")
print(A)