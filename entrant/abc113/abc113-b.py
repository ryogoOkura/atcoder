'''
問題文
ある国で、宮殿を作ることになりました。
この国では、標高がxメートルの地点での平均気温はT−x×0.006度です。
宮殿を建設する地点の候補はN個あり、地点iの標高はHiメートルです。
joisinoお姫様は、これらの中から平均気温がA度に最も近い地点を選んで宮殿を建設するようにあなたに命じました。
度に最も近い地点を選んで宮殿を建設するようにあなたに命じました。
宮殿を建設すべき地点の番号を出力してください。
ただし、解は一意に定まることが保証されます。
制約
1≤N≤1000
0≤T≤50
−60≤A≤T
0≤Hi≤105
入力は全て整数
解は一意に定まる
'''

n=int(input())
t,a=map(int, input().split())
h=list(map(int,input().split()))
min_gap=999
for i in range(n):
    tmp=t-0.006*h[i]
    if(abs(tmp-a)<min_gap):
        min_gap=abs(tmp-a)
        min_i=i

print(min_i+1)
