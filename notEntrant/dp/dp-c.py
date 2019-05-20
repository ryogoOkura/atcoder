n=int(input())
action=[list(map(int,input().split())) for _ in range(n)]
# happy[i][j] i日目にaction j を選んだ場合の幸福度の最大値
happy=[[0,0,0]for _ in range(n+1)]
for i in range(1,n+1):
    for j in range(3):
        for k in range(3):
            if j!=k:
                happy[i][j]=max(happy[i][j],happy[i-1][k]+action[i-1][j])
# print(happy)
print(max(happy[n]))
