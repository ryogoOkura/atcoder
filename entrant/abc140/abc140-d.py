n,k=map(int,input().split())
s=input()
isSame=[True if s[i]==s[i+1] else False for i in range(n-1)]
ans=isSame.count(True)
# print(ans)
ans=ans+2*k
if ans>n-1:
    ans=n-1
print(ans)
