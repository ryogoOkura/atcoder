n,q=map(int,input().split())
a=list(map(int,input().split()))
x=[]
for i in range(q):
    x.append(int(input()))
for xi in x:
    takahashi=0
    a2=a.copy()
    diff=[a2[i]-xi for i in range(n)]
    # print(a2)
    while True:
        takahashi+=a2.pop()
        diff.pop()
        # print(a2)
        if len(a2)==0:
            break
        mDiff=min(diff,key=abs)
        index=diff.index(mDiff)
        a2.pop(index)
        diff.pop(index)
        if len(a2)==0:
            break
        # print(a2)
    print(takahashi)
