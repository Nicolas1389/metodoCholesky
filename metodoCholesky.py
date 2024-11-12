from math import sqrt
from pprint import pprint

# La matriz debe ser siemtrica y definida positiva

def cholesky(A):
    n=len(A)
    #creal matriz cero para L
    L= [[0.0] * n for i in range(n)]
    #desarrollo de la descomposición de cholesky
    for i in range(n):
        for k in range(i+1):
            tmp_sum = sum(L[i][j]*L[k][j] for j in range(k))
            if (i==k):#Elementos de la diagonal
                L[i][k]=sqrt(A[i][i]-tmp_sum)
            else:
                L[i][k]=(1.0/L[k][k]*(A[i][k]-tmp_sum))
    return L
A=[[4,1,2],[1,2,0],[2,0,5]]
L=cholesky(A)
print ("A: ")
pprint(A)
print ("l: ")
pprint((L))
