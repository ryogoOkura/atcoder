n=int(input())
a=list(map(int,input().split()))
ans=1
if 0 in a:
    ans=0
else:
    for ai in a:
        ans*=ai
        if ans>10**18:
            ans=-1
            break
print(ans)
