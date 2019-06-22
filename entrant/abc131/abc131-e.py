def cmb(n, r):
    if n - r < r: r = n - r
    if r == 0: return 1
    if r == 1: return n

    numerator = [n - r + k + 1 for k in range(r)]
    denominator = [k + 1 for k in range(r)]

    for p in range(2,r+1):
        pivot = denominator[p - 1]
        if pivot > 1:
            offset = (n - r) % p
            for k in range(p-1,r,p):
                numerator[k - offset] /= pivot
                denominator[k] /= pivot

    result = 1
    for k in range(r):
        if numerator[k] > 1:
            result *= int(numerator[k])

    return result
n,k=map(int,input().split())
isExist=True
# 1つの頂点を根とした木の距離が2の頂点対の数
if k > (n-2)*(n-1)//2:
    isExist=False
if isExist:
    side=cmb(n,2)-k
    print(side)
    cnt=0
    for i in range(n):
        for j in range(i+1,n):
            if cnt>=k or j==n-1:
                print(i+1,j+1)
            else:
                cnt+=1
else:
    print(-1)
