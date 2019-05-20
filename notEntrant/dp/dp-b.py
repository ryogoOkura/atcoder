import numpy as np
INF=100000000
n,k=map(int,input().split())
h=np.array(list(map(int,input().split())))
cost=np.array([INF for _ in range(n)])
cost[0]=0
# print(h,cost)
for i in range(1,n):
    s=max(0,i-k)
    cost[i]=min(cost[s:i]+abs(h[i]-h[s:i]))
print(cost[n-1])
