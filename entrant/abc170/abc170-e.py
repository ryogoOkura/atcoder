n,q=map(int,input().split())
ab=[list(map(int,input().split())) for _ in range(n)]
cd=[tuple(map(int,input().split())) for _ in range(q)]
for ci,di in cd:
    ab[ci-1][1]=di
    ab.sort(key=lambda x:-x[0])
    ab.sort(key=lambda x:x[1])
    max=[]
    index=0
    for i in range(n):
        if ab[i][1]>index:
            max.append(ab[i][0])
            index=ab[i][1]
    # print(ab)
    print(min(max))
