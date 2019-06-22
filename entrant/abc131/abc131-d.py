import numpy as np
n=int(input())
ab=[list(map(int,input().split())) for _ in range(n)]
ab.sort(key=lambda x:x[1])
b=np.array([ab[i-1][1] if i>0 else 0 for i in range(n+1)])
ruisekiA=np.zeros(n+1)
for i in range(n):
    ruisekiA[i+1]=ruisekiA[i]+ab[i][0]
# print(ab)
# print(b)
# print(ruisekiA)
if len(ruisekiA[ruisekiA>b])==0:
    print('Yes')
else:
    print('No')
# now=0
# canFinish=True
# for i in range(n):
#     now+=ab[i][0]
#     if now>ab[i][1]:
#         canFinish=False
#         break
# if canFinish:
#     print('Yes')
# else:
#     print('No')
