# できなかった
# 2^r<=lとなるrについて、r+1個の頂点を用意し、N=r+1(l<=10^6<2^20よりN<=20)とする
# そして頂点iから頂点i+1へ、長さ0と長さ2^iの辺を張る
# さて、こうして作ったグラフの頂点 t から頂点 N に長さ X の辺を張れば、長さ X, X + 1, ..., X + 2^(t−1) −1のパスを 1 本ずつ作ることができます。よって、t = N − 1, ..., 1 の順に見て、L − 2^(t−1) ≥ 2^r なら頂点 t から頂点 N に長さ L − 2^(t−1) の辺を張り、L を 2^(t−1) だけ減らし、そうでなければ何もしないことを繰り返せばよいです。
import math
l=int(input())
n=math.floor(math.log2(l))
edge=[]
for i in range(n):
    edge.append((i+1,i+2,0))
    edge.append((i+1,i+2,2**i))
i=n-1
while l>2**n:
    m=l-2**i
    if m>=2**n:
        edge.append((i+1,n+1,m))
        l=m
    i-=1
print(n+1,len(edge))
for a,b,c in edge:
    print(a,b,c)
