class UnionFind:
    def __init__(self,n):
        self.parent=[i for i in range(n)]
        self.rank=[0 for _ in range(n)]

    def find(self,x):
        if self.parent[x]==x:
            return x
        else:
            rootx=self.find(self.parent[x])
            self.parent[x]=rootx
            return rootx

    def union(self,x,y):
        rootx=self.find(x)
        rooty=self.find(y)
        if self.rank[rootx]<self.rank[rooty]:
            self.parent[rootx]=rooty
        else:
            self.parent[rooty]=rootx
            if self.rank[rootx]==self.rank[rooty]:
                self.rank[rootx]+=1

n,m=map(int,input().split())
xyz=[list(map(int,input().split())) for _ in range(m)]
uf=UnionFind(n)
for x,y,z in xyz:
    x,y=x-1,y-1
    uf.union(x,y)

# print(uf.parent)
for i in range(n):
    uf.find(i)
print(len(set(uf.parent)))

# n,m=map(int,input().split())
# xyz=[list(map(int,input().split())) for _ in range(m)]
# set=[-1 for _ in range(n)]
# i=0
# for x,y,z in xyz:
#     x,y=x-1,y-1
#     if set[x]==-1 and set[y]==-1:
#         set[x]=i
#         set[y]=i
#         i+=1
#     elif set[x]==-1:
#         set[x]=set[y]
#     elif set[y]==-1:
#         set[y]=set[x]
# print(i+set.count(-1))
