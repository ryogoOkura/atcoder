from collections import defaultdict
import math

class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

    def __str__(self):
        return '\n'.join(f'{r}: {m}' for r, m in self.all_group_members().items())

def main(): ## できてない
    n,k=map(int,input().split())
    a=[list(map(int,input().split())) for _ in range(n)]
    # canSwapRow[i][j]=True   i行とj行を交換可能
    canSwapRow=[[1 if i<j else 0 for j in range(n)] for i in range(n)]
    canSwapCol=[[1 if i<j else 0 for j in range(n)] for i in range(n)]
    for row in range(n): # row
        for col in range(n): # col
            for tmp in range(row+1,n): # row
                if canSwapRow[row][tmp]==1:
                    if a[row][col]+a[tmp][col]>k:
                        canSwapRow[row][tmp]=0
            for tmp in range(col+1,n): # col
                if canSwapCol[col][tmp]==1:
                    if a[row][col]+a[row][tmp]>k:
                        canSwapCol[col][tmp]=0
    import numpy as np
    print(np.array(canSwapRow))
    print(np.array(canSwapCol))
    uf=UnionFind(n*2) # 0~n-1:row, n~2*n-1:col
    for i in range(n):
        for j in range(i+1,n):
            if canSwapRow[i][j]:
                uf.union(i,j)
            if canSwapCol[i][j]:
                uf.union(n+i,n+j)
    print(uf)
    ans=1
    for i in uf.roots():
        ans*=math.factorial(uf.size(i))
    return ans

if __name__=='__main__':
    ans=main()
    print(ans)
