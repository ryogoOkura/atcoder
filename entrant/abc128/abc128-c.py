n,m=map(int,input().split())
s=[list(map(int,input().split())) for _ in range(m)]
p=list(map(int,input().split()))

isAffectedSwitch=[[False for _ in range(n)] for _ in range(m)]
for i in range(m):
    for j in range(1,s[i][0]+1):
        isAffectedSwitch[i][s[i][j]-1]=True
# print(isAffectedSwitch)
onoff=[[(i%(2**(n-j)))>>(n-j-1) for j in range(n)]for i in range(2**n)]
# print(onoff)
ans=0
for i in range(2**n):
    cnt=[0 for _ in range(m)]
    for j in range(n):
        for k in range(m):
            if onoff[i][j]==1:
                if isAffectedSwitch[k][j]==True:
                    cnt[k]+=1
    isOK=True
    for k in range(m):
        if cnt[k]%2!=p[k]:
            isOK=False
    if isOK:
        ans+=1
print(ans)
