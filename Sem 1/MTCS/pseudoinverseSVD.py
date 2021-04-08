#PseudoInverse of a matrix via Singular Value Decomposition
import numpy as np
#defining a matrix
A=np.array([[1,2,3],[3,4,5]])
print("The Original matrix:")
print(A)
#SVD
U,s,VT=np.linalg.svd(A)
#reciprocals of s
d=1.0/s
#create m*n sigma inverse matrix
sigma_inverse=np.zeros(A.shape)
#A.shape[0]=3 and A.shape[1]=2 
sigma_inverse[:A.shape[0],:A.shape[0]]=np.diag(d) #shape[i] where i is smaller shape of 0 or 1
print("The sigma inverse is :\n",np.transpose(sigma_inverse))
#calculating pseudo inverse i.e. A^+ = V.Sigma^+.UT
B=np.transpose(VT).dot(np.transpose(sigma_inverse).dot(np.transpose(U)))
print("The PseudoInverse of A is(By calculating):")
print(B)
#verifying with pinv
invA=np.linalg.pinv(A)
print("The PseudoInverse of A is(By pinv built-in function):")
print(invA)