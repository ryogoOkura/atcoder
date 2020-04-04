n,k=map(int,input().split())
tmp=n//k
a=n-k*tmp
b=abs(n-k*(tmp+1))
print(min(a,b))
