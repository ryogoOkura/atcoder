'''
問題文
Atcoder国にはN個の県があり、これらの県には合計で M個の市が属しています。
市iが誕生したのはYi年であり、県Piに属しています。
ただし、同じ年に誕生した市が複数存在することはないとします。
それぞれの市に12桁の認識番号を割り振ることとなりました。
市iが 県Piに属する市の中でx番目に誕生した市のとき、市iの認識番号の上6桁はPi、下6桁はxとなります。
ただし、Piやxが6桁に満たない場合は6桁になるまで0を左に追加するものとします。
全ての市の認識番号を求めてください。
ただし、市が1つも属さない県がある場合に注意してください。
制約
1≤N≤105
1≤M≤105
1≤Pi≤N
1≤Yi≤109
Yiは全て異なる
入力は全て整数
'''

n,m=map(int, input().split())
prefecture=[]
for i in range(m):
    pk,yk=map(int, input().split())
    prefecture.append([pk,yk,i])

prefecture.sort(key=lambda x:(x[0],x[1])) # x[0]:pで整理したうえでx[1]:yで整理
p_num=prefecture[0][0]
city_num=1
for i in range(m):
    if(prefecture[i][0]!=p_num):
        p_num=prefecture[i][0]
        city_num=1

    prefecture[i].append(city_num)
    city_num+=1

prefecture.sort(key=lambda x:x[2])

for i in range(m):
    print('{0:06d}{1:06d}'.format(prefecture[i][0], prefecture[i][3]))

# p=[]
# y=[]
# prefecture=[[] for j in range(n)]
# for i in range(m):
#     pk,yk=map(int, input().split())
#     p.append(pk)
#     y.append(yk)
#     prefecture[p[i]-1].append(y[i])
#
# for j in range(n):
#     prefecture[j].sort()
#
# for i in range(m):
#     print('{0:06d}{1:06d}'.format(p[i],prefecture[p[i]-1].index(y[i])+1))
