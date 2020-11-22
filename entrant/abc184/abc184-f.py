
def main(): # もちろんTLEする
    n,t=map(int,input().split())
    a=list(map(int,input().split()))
    a.sort()
    # dp[i][w] : i番目まで選んで合計がw以下
    dp=[[0 for _ in range(t+1)]for _ in range(n+1)]
    for i in range(1,n+1):
        for w in range(t+1):
            if w>=a[i-1]:
                choice=dp[i-1][w-a[i-1]]+a[i-1]
                nochoice=dp[i-1][w]
                dp[i][w]=max(choice,nochoice)
            else:
                dp[i][w]=dp[i-1][w]
    # print(dp)
    ans=dp[n][t]
    return ans

if __name__=='__main__':
    ans=main()
    print(ans)
