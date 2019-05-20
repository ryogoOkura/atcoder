class UnionFind:
    def __init__(self,n):
        self.parent=[i for i in range(n)]
        self.rank=[0 for _ in range(n)]
        # 親への重み
        self.weight=[0 for _ in range(n)]

    def find(self,x):
        if self.parent[x]==x:
            return x
        else:
            # 重みをrootまでに変える
            self.weight[x]+=self.weight[self.parent[x]]
            # rootにつなぎ替える
            y=self.find(self.parent[x])
            self.parent[x]=y
            return y

    def union(self,x,y,w):
        rootx=self.find(x)
        rooty=self.find(y)
        # yのrootにxのrootをつなぐ
        if self.rank[rootx] < self.rank[rooty]:
            self.parent[rootx]=rooty
            self.weight[rootx]=w-self.weight[x]+self.weight[y]
        else:
            self.parent[rooty]=rootx
            self.weight[rooty]=w-self.weight[y]+self.weight[x]
            if self.rank[rootx]==self.rank[rooty]:
                self.rank[rootx]+=1

n=int(input())
uvw=[list(map(int,input().split())) for _ in range(n-1)]
uf=UnionFind(n)
for u,v,w in uvw:
    u,v,w=u-1,v-1,w
    uf.union(u,v,w)

# print(uf.parent)
# print(uf.weight)
for w in uf.weight:
    print(w%2)


# n=int(input())
# sides=[list(map(int,input().split())) for _ in range(n-1)]
# sides=[[side[0]-1,side[1]-1,side[2]%2]for side in sides]
# # print(sides)
# color=[-1 for _ in range(n)]
# color[sides[0][0]]=0
# while True:
#     u,v,w=sides.pop(0)
#     # print(u,v,w)
#     if color[u]==-1 and color[v]==-1:
#         sides.append([u,v,w])
#     elif color[v]==-1:
#         # print('u=',color[u],w)
#         color[v]=(color[u]^w)
#     elif color[u]==-1:
#         # print('v=',color[v],w)
#         color[u]=(color[v]^w)
#     if len(sides)==0:
#         break
# # print(color)
# for c in color:
#     print(c)
