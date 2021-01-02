from collections import defaultdict

class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1]*n # 根なら-size、子なら親の頂点（正の数になる）

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else: # 経路圧縮（親を根に更新）しつつ、根を探索
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.parents[x] > self.parents[y]: # sizeの大きいほうがx
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


def main():
    n=int(input())
    ab=[]
    uf=[UnionFind(n) for _ in range(n)]
    for i in range(n-1):
        ai,bi=map(int,input().split())
        ai,bi=ai-1,bi-1
        ab.append((ai,bi))
        for j in range(n):
            if ai!=j and bi!=j:
                uf[j].union(ai,bi)

    q=int(input())
    tex=[tuple(map(int,input().split())) for _ in range(q)]

    c=[0 for _ in range(n)]
    for ti,ei,xi in tex:
        ai,bi=0,0
        ei=ei-1
        if ti==1:
            ai,bi=ab[ei]
        else:
            bi,ai=ab[ei]
        for mem in uf[bi].members(ai):
            c[mem]+=xi

    for ci in c:
        print(ci)
    return

if __name__=='__main__':
    main()
