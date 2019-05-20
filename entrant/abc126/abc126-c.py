import math
n,k=map(int,input().split())
ans=0
for i in range(1,n+1):
    if i<k:
        # print(i,math.ceil(math.log2(k/i)))
        times=math.ceil(math.log2(k/i))
        ans+=math.pow(0.5,times)
    else:
        ans+=1
print(ans/n)
