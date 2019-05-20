# (a,b,c)は(a+b,b+c,c+a)に全単射
# (a+b,b+c,c+a)は(e,e,e)または(o,o,e)である必要がある
# import math
# n,k=map(int,input().split())
# kmulSize=math.floor((2*n)/k) # kの倍数の種類数
# # print('kmulSize',kmulSize)
# cnt=0
# for i in range(1,kmulSize+1): # k*i:1回使う数字
#     for j in range(1,kmulSize+1): # k*j:2回使う数字
#         if (k*i)%2==0:
#             if i==j:
#                 cnt+=1
#             else:
#                 if (k*i/2<=n)&(0<k*(2*j-i)/2<=n):
#                     cnt+=3
#             print('({0:>6},{1:>6},{1:>6}) ({2:>8},{3:>8},{3:>8})'.format(k*i,k*j, k*(2*j-i)/2,k*i/2),'cnt',cnt)
#
# print(cnt)

import math
n,k=map(int,input().split())
size=math.floor(n/k)
cnt=size*(size-1)*(size-2)+size*(size-1)*3+size
if k%2==0:
    size=math.floor(2*n/k)-size
    cnt+=size*(size-1)*(size-2)+size*(size-1)*3+size

print(cnt)
