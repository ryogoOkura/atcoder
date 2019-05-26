def mymin(a,b):
    if a==-1:
        return b
    return min(a,b)

n,q=map(int,input().split())
stx=[list(map(int,input().split())) for _ in range(n)]
d=[int(input()) for _ in range(q)]

stop=[-1 for _ in range(q)]
for i in range(q):
    for j in range(n):
        s,t,x=stx[j]
        # print(i,'人目',j,'工事',d[i],s,t,x)
        if s-0.5 <= x+d[i] <= t-0.5:
            stop[i]=mymin(stop[i],x)
# print(stop)
for s in stop:
    print(s)
