n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
aHIKUb=[[i,(a[i]-b[i])/a[i],(a[i]-b[i])/b[i]] for i in range(3)]
aHIKUb.sort(key=lambda x:x[1])
changeCnt=[0,0,0]
changeCnt[aHIKUb[0][0]]=n//a[aHIKUb[0][0]]
for i,aibiai,aibibi in aHIKUb[1:]:
    remain=n
    for j in range(3):
        remain-=a[j]*changeCnt[j]
    if aibiai<0 and remain>a[i]:
        changeCnt[i]=remain//a[i]
for i in range(3):
    n+=(-a[i]+b[i])*changeCnt[i]

aHIKUb.sort(key=lambda x:x[2])
changeCnt=[0,0,0]
changeCnt[aHIKUb[2][0]]=n//b[aHIKUb[2][0]]
for i,aibiai,aibibi in aHIKUb[:2]:
    remain=n
    for j in range(3):
        remain-=a[j]*changeCnt[j]
    if aibibi>0 and remain>a[i]:
        changeCnt[i]=remain//a[i]
for i in range(3):
    n+=(a[i]-b[i])*changeCnt[i]
print(n)
