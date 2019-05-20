n=int(input())
a=list(map(int,input().split()))
xorSum=[a[0] for _ in range(n)]
for i in range(1,n):
    xorSum[i]=xorSum[i-1]^a[i]

ans=1
# a[i]とa[i+1]の間を最初に分ける場所とする
for i in range(n-1):
    beauty=xorSum[i]
    index=i
    width=1
    while True:
        print(index,width,end='   ')
        print(beauty, xorSum[index+width]^xorSum[index])
        if beauty==(xorSum[index+width]^xorSum[index]):
            if index+width==n-1:
                ans+=1
                print('OK')
                    break
            # ここで分岐が必要
            index+=width
            width=1
        else:
            width+=1
            if index+width==n:
                break

print(ans%1000000007)
