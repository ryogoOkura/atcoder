n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=list(map(int,input().split()))

pre=a[0]
ans=b[pre-1]
for i in range(1,n):
    now=a[i]
    ans+=b[now-1]
    if a[i]==pre+1:
        ans+=c[pre-1]
    pre=now
print(ans)
