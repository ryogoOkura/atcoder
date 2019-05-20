import math
n=int(input())
p=[]
p.append(int(input()))
pAdded=[p[0]]
pmax=0
pmaxIndex=0
for i in range(1,n):
    p.append(int(input()))
    pAdded.append(pAdded[i-1]+p[i])
    if pmax<p[i]:
        pmaxIndex=i
        pmax=p[i]
print(pAdded[n-1]-math.floor(p[pmaxIndex]/2))
