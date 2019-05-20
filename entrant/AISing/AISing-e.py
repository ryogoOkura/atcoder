n=int(input())
a=list(map(int,input().split()))
network=[[0 for _ in range(n)]for _ in range(n)]
for i in range(n-1):
    u,v=map(int,input().split())
    network[u-1][v-1]=1
    network[v-1][u-1]=1



import numpy as np
print(np.array(network))
