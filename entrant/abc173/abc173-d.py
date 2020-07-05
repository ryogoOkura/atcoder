n=int(input())
a=list(map(int,input().split()))
a.sort(reverse=True)
# print(sum(a[:-1]))
if n==1:
    print(0)
else:
    ans=sum(a[1:n//2])+a[n//2-1]
    # print(ans)
    if n%2==1:
        ans+=a[n//2]
    # print(ans)
    ans+=sum(a[:n//2-1])
    print(ans)
