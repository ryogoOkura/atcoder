# 何本の数直線上にあるかを求める　1<=ans<=n-1
# 少なくとも2点を通る直線のみ調べれば良い
# できなかった
# 少なくとも2点を満たす(p,q)について、全てに対しそれを満たすか調べれば良い
n=int(input())
xy=[list(map(int,input().split())) for _ in range(n)]
xy.sort(key=lambda x:(x[0],x[1]))
# print(xy)
if n<=2:
    print(1)
else:
    diff=[]
    for i in range(n):
        for j in range(i):
            diff.append((xy[i][0]-xy[j][0],xy[i][1]-xy[j][1]))

    ans=[]
    # print(set(diff))
    for p,q in set(diff):
        cnt=n
        for i in range(n):
            for j in range(i):
                if xy[i][0]-xy[j][0]==p and xy[i][1]-xy[j][1]==q:
                    cnt-=1
        ans.append(cnt)
    print(min(ans))
# n=int(input())
# xy=[list(map(int,input().split())) for _ in range(n)]
# xy.sort(key=lambda x:(x[0],x[1]))
# # print(xy)
# if n<=2:
#     print(1)
# else:
#     diff=[]
#     for i in range(n):
#         for j in range(i):
#             diff.append((xy[i][0]-xy[j][0],xy[i][1]-xy[j][1]))
#
#     ans=[]
#     # print(set(diff))
#     for p,q in set(diff):
#         intercept=[]
#         for i in range(n):
#             qxHIKUpy=q*xy[i][0]-p*xy[i][1]
#             intercept.append(qxHIKUpy)
#         # print(q,'x-',p,'y=',intercept)
#         cnt=len(set(intercept))
#         intercepts=sorted(enumerate(intercept),key=lambda x:x[1])
#         # print(intercepts)
#         i=0
#         x=xy[intercepts[0][0]][0]
#         intercept=intercepts[0][1]
#         for i in range(1,n):
#             if intercept==intercepts[i][1]:
#                 if x+p != xy[intercepts[i][0]][0]:
#                     cnt+=1
#             x=xy[intercepts[i][0]][0]
#             intercept=intercepts[0][1]
#
#         ans.append(cnt)
#     # print(ans)
#     print(min(ans))
