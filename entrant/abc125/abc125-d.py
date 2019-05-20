import numpy as np
n=int(input())
a=np.array(list(map(int,input().split())),dtype='int64')
if np.sum(a<0)%2==0:
    a=abs(a)
else:
    a=abs(a)
    a[a.argmin()]=-a[a.argmin()]
# print(a)
print(int(sum(a)))
