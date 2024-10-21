print("SJC23MCA-2056:TESMOL SHAJI")
print("Batch:MCA 2023-25")
import numpy as np
A = np.array([[5, 27, 32], [14, 53, 62], [67, 88, 19]])
U, S, Vt = np.linalg.svd(A)
A_hat = U @ np.diag(S) @ Vt
print('Original Matrix A :' )
print(A)
print('\nSingular Values : ')
print(S)
print('\nReconstructed Matrix A_hat : ')
print(A_hat)