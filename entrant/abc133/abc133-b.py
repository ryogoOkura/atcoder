import numpy as np
n,d=map(int,input().split())
x=[list(map(int,input().split())) for _ in range(n)]
square=[i**2 for i in range(127)]
# print(square)
x=np.array(x)
# print(x)
ans=0
for i in range(n-1):
    for j in range(i+1,n):
        # print(x[i],x[j],np.sum((x[i]-x[j])**2))
        if np.sum((x[i]-x[j])**2) in square:
            ans+=1
print(ans)
