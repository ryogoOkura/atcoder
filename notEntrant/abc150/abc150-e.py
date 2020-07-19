n=int(input())
c=list(map(int,input().split()))
p=10**9+7
ans=0
c.sort()
for i,ci in enumerate(c):
    if i<n-1:
        ans=(ans+pow(2,n+i,p)*ci*(pow(2,n-2-i,p)*n+1))%p
    else:
        ans=(ans+pow(2,n+i,p)*ci)%p
print(ans)
