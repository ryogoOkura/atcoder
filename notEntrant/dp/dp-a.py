# https://atcoder.jp/contests/dp/tasks
# https://qiita.com/drken/items/dc53c683d6de8aeacf5a

n=int(input())
h=[0 for _ in range(n+1)]
h[1:]=list(map(int,input().split()))
h[0]=h[1]
# print(h)
cost=[0 for _ in range(n+1)]
for i in range(2,n+1):
    cost2=cost[i-2]+abs(h[i-2]-h[i])
    cost1=cost[i-1]+abs(h[i-1]-h[i])
    if cost2>cost1:
        cost[i]=cost1
    else:
        cost[i]=cost2
print(cost[n])
