# できなかった
# nコのコマでmコの地点を訪れる
# 指定された地点のみをスタート地点と考えて問題ない
# 右にのみ進むと考えて問題ない
# nコの範囲に分け、その合計幅の最小値を求める
# ※訪れていないN-1コの開区間を最大化すれば良い！！！
import math
n,m=map(int,input().split())
x=list(map(int,input().split()))
x.sort()
if n>=m:
    print(0)
else:
    dimX=[x[i]-x[i-1]for i in range(1,m)]
    # print(x,dimX)
    dimX.sort(key=lambda x:-x)
    ans=x[-1]-x[0]
    for i in range(n-1):
        ans-=dimX[i]
    print(ans)
