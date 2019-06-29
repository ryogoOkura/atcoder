# def getPath(start,goal,prev):
#     path=[]
#     now=goal
#     path.append(now)
#     while True:
#         path.append(prev[now])
#         if prev[now]==start:
#             break
#         now=prev[now]
#     path.reverse()
#     return path

import numpy as np
MAX_VAL=1000000007
n,m=map(int,input().split())
uv=[tuple(map(int,input().split())) for _ in range(m)]
s,t=map(int,input().split())
s,t=s-1,t-1

move=np.zeros((n,n))
for ui,vi in uv:
    ui,vi=ui-1,vi-1
    move[ui][vi]=1
# print(move)
kenkenpa=np.dot(np.dot(move,move),move)

visited=[False for _ in range(n)]
cost=[MAX_VAL for _ in range(n)]
cost[s]=0
# prev=[-1 for _ in range(n)]
# prev[s]=s
now=s
while True:
    min=MAX_VAL
    next=-1
    visited[now]=True
    for i in range(n):
        if not visited[i]:
            if kenkenpa[now][i]==1:
                tmpCost=cost[now]+1
                if cost[i]>tmpCost:
                    cost[i]=tmpCost
                    # prev[i]=now
                if min>cost[i]:
                    min=cost[i]
                    next=i
    if next==-1:
        break
    elif next==t:
         break
    now=next
# print(cost)
# print(prev)
if cost[t]==MAX_VAL:
    print(-1)
else:
    print(cost[t])
