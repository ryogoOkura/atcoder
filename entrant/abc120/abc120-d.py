# できなかった
# 辺を消すのは難しいので、足していき逆順に出力すると良い
# UnionFind(グループ分けを木構造で管理するデータ構造)を使う
# ->2つの要素が同じグループに属するかどうかの判定や、グループ同士の併合がすばやく行える

# import numpy as np
# n,m=map(int,input().split())
# bridge=[list(map(int,input().split())) for _ in range(m)]
#
# bridgeGrid=[[0 for _ in range(n)]for _ in range(n)]
# count=[n*(n-1)//2]
# for i in range(m-1):
#     a,b=bridge[m-1-i]
#     bridgeGrid[a-1][b-1]=1
#     bridgeGrid[b-1][a-1]=1
#     # print(np.array(bridgeGrid))
#     cnt=0
#     for ai in range(n):
#         for bi in range(ai+1,n):
#             canReach=0
#             hop=0
#             # print(ai,bi)
#             if bridgeGrid[ai][bi]==0:
#                 stack=[ai]
#                 now=ai
#                 while len(stack)>0:
#                     # print(' ',stack)
#                     pre=now
#                     now=stack.pop(0)
#                     for j in range(pre):
#                         if bridgeGrid[now][j]:
#                             stack.append(j)
#                             if j==bi:
#                                 stack=[]
#                                 canReach=1
#                     if canReach:
#                         break
#                     for j in range(pre+1,n):
#                         if bridgeGrid[now][j]:
#                             stack.append(j)
#                             if j==bi:
#                                 stack=[]
#                                 canReach=1
#                     if canReach:
#                         break
#                     stack=list(dict.fromkeys(stack))
#                     hop+=1
#                     if hop>n*2:
#                         break
#                 if not canReach:
#                     cnt+=1
#                     # print(ai,bi,'*')
#     count.append(cnt)
# for i in range(m):
#     print(count[m-1-i])

class UnionFind:
    def __init__(self,n):
        self.parent=[i for i in range(n+1)]
        self.size=[1 for _ in range(n+1)]
    # 親(木構造の根)を返す
    def find(self,x):
        if self.parent[x]==x:
            return x
        else:
            self.parent[x]=self.find(self.parent[x])
            return self.parent[x]
    # 2つの木を併合
    def union(self,x,y):
        x=self.find(x)
        y=self.find(y)
        if x==y:
            return
        if self.size[x]<self.size[y]:
            x,y=y,x
        self.size[x]+=self.size[y]
        self.parent[y]=x

n,m=map(int,input().split())
bridge=[list(map(int,input().split())) for _ in range(m)]
bridge.reverse()
uf=UnionFind(n)
dis=n*(n-1)//2
ans=[dis]
for a,b in bridge:
    pa,pb=uf.find(a),uf.find(b)
    if pa!=pb:
        dis-=uf.size[pa]*uf.size[pb]
    ans.append(dis)
    uf.union(a,b)
for a in reversed(ans[:-1]):
    print(a)
