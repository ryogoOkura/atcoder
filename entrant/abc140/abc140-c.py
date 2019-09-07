n=int(input())
b=list(map(int,input().split()))

ans=b[0]+b[n-2]
for i in range(n-2): # bの要素数-1
    if b[i]<b[i+1]:
        ans+=b[i]
    else:
        ans+=b[i+1]

print(ans)
