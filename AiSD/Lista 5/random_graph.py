import numpy as np
import sys
n = int(sys.argv[1])
A = n+1
B = 2*n
np.random.seed(23)
print(n)
for i in range(1,n+1):
    for j in range(i+1,n+1): 
        w = np.random.randint(A,B)
        print(i,j,w)