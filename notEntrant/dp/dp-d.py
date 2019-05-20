# n,w=map(int,input().split())
# wv=[list(map(int,input().split())) for _ in range(n)]
# # value[i][j] i番目までで重さがj以下となるように選んだときの価値の最大値
# value=[[0 for _ in range(w+1)]for _ in range(n+1)]
# for i in range(n):
#     for j in range(w+1):
#         lastw=j-wv[i][0]
#         if lastw>=0:
#             value[i+1][j]=max(value[i][j],value[i][lastw]+wv[i][1])
#         else:
#             value[i+1][j]=value[i][j]
import numpy as np
n,w=map(int,input().split())
wv=[list(map(int,input().split())) for _ in range(n)]
value=np.zeros((n+1,w+1),dtype=int)
for i in range(n):
    wei=wv[i][0]
    value[i+1][:wei]=value[i][:wei]
    # np.maximum([1,-3,2],0) == [1,0,2]
    value[i+1][wei:]=np.maximum(value[i][wei:],value[i][:-wei]+wv[i][1])
# print(value)
print(value[n][w])
