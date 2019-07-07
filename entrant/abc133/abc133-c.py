l,r=map(int,input().split())
if (l//2019) == (r//2019):
    l,r=l%2019,r%2019
    ans=2018
    for i in range(l,r):
        for j in range(i+1,r+1):
            tmp=(i*j)%2019
            if tmp<ans:
                ans=tmp
    print(ans)
else:
    print(0)
