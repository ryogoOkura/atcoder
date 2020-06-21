n=int(input())
a=list(map(int,input().split()))
q=int(input())
bc=[tuple(map(int,input().split())) for _ in range(q)]
d={}
for ai in a:
    if ai not in d:
        d[ai]=0
    d[ai]+=1
# print(d)

ans=0
for key in d:
    ans+=key*d[key]

for bi,ci in bc:
    if bi in d:
        tmp=d[bi]
        d[bi]=0
        ans-=bi*tmp
        if ci not in d:
            d[ci]=0
        d[ci]+=tmp
        ans+=ci*tmp
    print(ans)
