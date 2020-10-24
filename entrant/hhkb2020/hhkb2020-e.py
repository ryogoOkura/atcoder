# 参考　https://note.nkmk.me/python-union-find/
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
        return {r: self.members(r) for r in self.roots()}

    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())

# UFで通してる人　https://atcoder.jp/contests/hhkb2020/submissions/17318811
def main(): #TLE　
    h,w=map(int,input().split())
    uf_h=[UnionFind(h) for _ in range(w)] # 列のuf
    uf_w=[UnionFind(w) for _ in range(h)] # 行のuf
    s=[input() for _ in range(h)]
    all=0
    for hi in range(h):
        for wi in range(w):
            if s[hi][wi]=='.':
                all+=1
                if wi+1<w and s[hi][wi]==s[hi][wi+1]: # 右もランプおける
                    uf_w[hi].union(wi,wi+1)
                if hi+1<h and s[hi][wi]==s[hi+1][wi]: # 下もランプおける
                    uf_h[wi].union(hi,hi+1)
    # for hi in range(h):
    #     print('h',hi,uf_w[hi].all_group_members())
    # for wi in range(w):
    #     print('w',wi,uf_h[wi].all_group_members())
    ## ちょっと遅い
    # ans=0
    # for hi in range(h):
    #     for wi in range(w):
    #         if s[hi][wi]=='.':
    #             # print(f'({hi},{wi}),h_size={uf_h[wi].size(hi)},w_size={uf_w[hi].size(wi)},ans={ans}')
    #             size=uf_h[wi].size(hi) + uf_w[hi].size(wi) -1
    #             # (2**(このマスを光らせうるマスの個数)-1)*2**(残りのランプをおけるマスの個数)
    #             ans+=(pow(2,size,p)-1)*pow(2,all-size,p)

    ans=pow(2,all,p)*all
    for hi in range(h):
        for wi in range(w):
            if s[hi][wi]=='.':
                # print(f'({hi},{wi}),h_size={uf_h[wi].size(hi)},w_size={uf_w[hi].size(wi)},ans={ans}')
                size=uf_h[wi].size(hi) + uf_w[hi].size(wi) -1
                # 2**(このマスを光らせられない、ランプをおけるマスの個数)
                ans-=pow(2,all-size,p)
    return ans%p

p=10**9+7

if __name__=='__main__':
    ans=main()
    print(ans)
