n=int(input())
a,b=map(int,input().split())
p=list(map(int,input().split()))

cnt=[0 for _ in range(3)]
for pi in p:
    if pi<=a:
        cnt[0]+=1
    elif pi<=b:
        cnt[1]+=1
    else:
        cnt[2]+=1

print(min(cnt))
