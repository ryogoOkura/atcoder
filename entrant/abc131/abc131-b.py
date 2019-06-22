n,l=map(int,input().split())
taste=[l+i for i in range(n)]
absTaste=[abs(l+i) for i in range(n)]
eat=min(enumerate(absTaste),key=lambda x:x[1])[0]
# print(taste,eat)
ans=0
for i in range(n):
    if i!=eat:
        ans+=taste[i]

print(ans)
