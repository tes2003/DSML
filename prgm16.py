import numpy as np
# Create a 1D array
array_1d = np.array([1, 2, 3, 4, 5])
print("SJC23MCA-2056:TESMOL SHAJI")
print("Batch:MCA 2023-25")
print("\n\n1D Array before insertion:")
print(array_1d)
# Insert the value 6 at index 2
array_1d = np.insert(array_1d, 2, 6)
print("\n1D Array after insertion:")
print(array_1d)
# Create a 2D array
array_2d = np.array([[1, 2, 3],
[4, 5, 6]])
print("\nOriginal 2D Array:")
print(array_2d)
# Insert a row [7, 8, 9] at index 1 (between the existing rows)
array_2d = np.insert(array_2d, 1, [7, 8, 9], axis=0)
print("\n2D Array after insertions:")
print(array_2d)