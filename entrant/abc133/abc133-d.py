n=int(input())
a=list(map(int,input().split()))
plusA=[a[i] if i%2==0 else -1*a[i] for i in range(n)]
ruisekiPlusA=[0 for i in range(n+1)]
for i in range(1,n+1):
    ruisekiPlusA[i]=ruisekiPlusA[i-1]+plusA[i-1]
for i in range(n):
    if i%2==0:
        print(ruisekiPlusA[n]-2*ruisekiPlusA[i],end=' ')
    else:
        print(2*ruisekiPlusA[i]-ruisekiPlusA[n],end=' ')

# import numpy as np
# n=int(input())
# a=list(map(int,input().split()))
# sign=[1 if i%2==0 else -1 for i in range(n)]
# a=np.array(a)
# sign=np.array(sign)
# plusA=a*sign
# minusA=a*sign*-1
# # print(plusA,minusA)
# for i in range(n):
#     if i%2==0:
#         # print(minusA[:i],plusA[i:])
#         print(np.sum(minusA[:i])+np.sum(plusA[i:]),end=' ')
#     else:
#         # print(plusA[:i],minusA[i:])
#         print(np.sum(plusA[:i])+np.sum(minusA[i:]),end=' ')

# n=int(input())
# a=list(map(int,input().split()))
# sign=[(-1)**i for i in range(n)]
# ans=[0 for i in range(n)]
# for i in range(n):
#     tmp=0
#     for j in range(n):
#         tmp+=a[(i+j)%n]*sign[j]
#     ans[i]=tmp
# for ai in ans:
#     print(ai, end=' ')
