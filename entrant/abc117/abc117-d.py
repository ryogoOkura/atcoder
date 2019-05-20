# logの中身が0になるのを見逃してた　ほぼできてた
import math
n,k=map(int,input().split())
a=list(map(int,input().split()))
# f=[0for _ in range(k+1)]
# for i in range(k+1):
#     for j in range(n):
#         f[i]+=a[j]^i
# f.sort(key=lambda x:-x)
a.sort(key=lambda x:-x)
powSize=math.ceil(math.log(k+1)/math.log(2))
digitCnt=[0for _ in range(powSize)]
for i in range(n):
    for j in range(powSize):
        if ( a[i]&(1<<j) )>0:
            digitCnt[j]+=1
ansNum=[0]
for i in range(powSize-1,-1,-1):
    if 2*digitCnt[i]<n: # digitCnt[i]<n-digitCnt[i]
        for j in range(len(ansNum)):
            ansNum[j]+=(1<<i)
            if ansNum[j]>k:
                if ( ansNum[j]&(1<<(i+1)) )>0:
                    ansNum.append(ansNum[j]-(1<<(i+1)))
                ansNum[j]-=(1<<i)
    # print(i,ansNum)

ans=[0for _ in range(len(ansNum))]
for i in range(n):
    for j in range(len(ansNum)):
        if ansNum[j]<=k:
            ans[j]+=(a[i]^ansNum[j])
# print(a[0],powSize)
# print(digitCnt)
# print(ansNum,ans)
ans.sort(key=lambda x:-x)
print(ans[0])
