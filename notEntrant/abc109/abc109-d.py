# どこも1回しか動かせないから偶奇のみで考えて良い
#  奇数のところから奇数のところへ移せば良い
# 経路がかぶってはいけない
#  右下に移していくだけでいいのでは
import numpy as np
h,w=map(int,input().split())
a=[list(map(int,input().split())) for _ in range(h)]
move=[]
# a_odd_flag=[[a[i][j]%2 for j in range(w)]for i in range(h)]
# i,j=0,0
# while np.sum(a_odd_flag)>1:
#     sumOfRow=np.sum(a_odd_flag,axis=1)
#     while sumOfRow[i]==0:
#         i+=1
#         j=0
#     while a_odd_flag[i][j]==0:
#         j+=1
#     # print(i,j,'\n',np.array(a_odd_flag))
#     if j<w-1:
#         move.append((i,j,i,j+1))
#         a_odd_flag[i][j]^=1
#         a_odd_flag[i][j+1]^=1
#     else:
#         if i<h-1:
#             move.append((i,j,i+1,j))
#             a_odd_flag[i][j]^=1
#             a_odd_flag[i+1][j]^=1
#         else:
#             break
for i in range(h):
    for j in range(w):
        if a[i][j]%2:
            if j<w-1:
                move.append((i,j,i,j+1))
                a[i][j+1]+=1
            elif i<h-1:
                move.append((i,j,i+1,j))
                a[i+1][j]+=1
print(len(move))
for x,y,x2,y2 in move:
    print(x+1,y+1,x2+1,y2+1)
