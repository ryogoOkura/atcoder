n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))

diff=[a[i]-b[i] for i in range(n)]
diff.sort()
# print(diff)
suma=[0 for i in range(n)]
sumb=[0 for i in range(n)]
suma[0]=a[0]
sumb[0]=b[0]
for i in range(n-1):
    suma[i+1]=suma[i]+a[i+1]
    sumb[i+1]=sumb[i]+b[i+1]
if suma[n-1]>sumb[n-1]:
    point=0
    cnt=0
    for i in range(n):
        if diff[i]>=0:
            break
        point+=diff[i]
        cnt+=1
    # print(point,cnt)
    i=-1
    if point<0:
        for i in range(n):
            point+=diff[n-1-i]
            if point>=0:
                break
    print(cnt+i+1)
else:
    print(-1)
