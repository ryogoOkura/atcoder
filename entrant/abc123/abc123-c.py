import math
n=int(input())
a=[int(input()) for _ in range(5)]
print(math.ceil(n/min(a))+4)
# num=[n,0,0,0,0,0]
# cnt=0
# while num[5]<n:
#     for i in range(4,-1,-1):
#         move=min(num[i],a[i])
#         num[i+1]+=move
#         num[i]-=move
#     cnt+=1
# print(cnt)
