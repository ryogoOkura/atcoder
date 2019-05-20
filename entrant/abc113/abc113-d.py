# h:横線の列数 w:縦線の本数 k:ゴールする縦線
h,w,k=map(int, input().split())

# 以下の計算結果から、フィボナッチ数列であることがわかる
# existRight=[0 for _ in range(w-1)] # 右はしに横棒がある場合の数
# nonexistRight=[0 for _ in range(w-1)] # 右端に横棒がない場合の数
# nonexistRight[0]=1
# for i in range(1,w-1):
#     existRight[i]=nonexistRight[i-1]
#     nonexistRight[i]=existRight[i-1]+nonexistRight[i-1]

# patternSize[w-1]:縦軸w本のときのパターン数
# patternSize[-2],[-1]の対応のためのpatternSize[w],[w+1]
patternSize=[1for _ in range(w+2)]
patternSize[1]=2
for i in range(2,w):
    patternSize[i]=patternSize[i-1]+patternSize[i-2]

# 動的計画法
# a(h,x): h列目を通過した直後にx行目にいる場合の数とする
a=[[0for _ in range(w)]for _ in range(h+1)]
a[0][0]=1
for i in range(1,h+1):
    for j in range(0,w):
        # i-1行j列からの場合の数の漸化式
        if j!=0:
            a[i][j-1]+=a[i-1][j]*patternSize[j-2]*patternSize[w-1-j-1]
        a[i][j]+=a[i-1][j]*patternSize[j-1]*patternSize[w-1-j-1]
        if j!=w-1:
            a[i][j+1]+=a[i-1][j]*patternSize[j-1]*patternSize[w-1-j-2]

# import numpy as np
# print(np.array(a))
print(a[h][k-1]%1000000007)
