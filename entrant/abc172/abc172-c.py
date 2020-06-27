n,m,k=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
a_added=[0]
b_added=[0]
for i in range(n):
    a_added.append(a_added[i]+a[i])
for i in range(m):
    b_added.append(b_added[i]+b[i])

ans=0
j=m
for i in range(n+1):
    if a_added[i]>k:
        break
    while b_added[j]>k-a_added[i]:
        j-=1
    ans=max(ans,i+j)
print(ans)

# n,m,k=map(int,input().split())
# a=list(map(int,input().split()))
# b=list(map(int,input().split()))
# ## dp(i,j,w) ai,bj,weight
# dp=[[[0 for _ in range(k+1)]for _ in range(m+1)]for _ in range(n+1)]
#
# for i in range(n+1):
#     for j in range(m+1):
#         for w in range(k+1):
#             tmpA=dp[i][j][w]
#             tmpB,tmpC,tmpD=0,0,0
#             tmpE,tmpF,tmpG=0,0,0
#             if i<n:
#                 if w>a[i]:
#                     tmpB=dp[i][j][w-a[i]]+1
#                 if j>0:
#                     tmpC=dp[i+1][j-1][w]
#                     if j<m and w>b[j]:
#                         tmpD=dp[i+1][j-1][w-b[j]]+1
#                 dp[i+1][j][w]=max(tmpA,tmpB,tmpC,tmpD,dp[i+1][j][w])
#             if j<m:
#                 if w>b[j]:
#                     tmpE=dp[i][j][w-b[j]]+1
#                 if i>0:
#                     tmpF=dp[i-1][j+1][w]
#                     if i<n and w>a[i]:
#                         tmpG=dp[i-1][j+1][w-a[i]]+1
#                 dp[i][j+1][w]=max(tmpA,tmpE,tmpF,tmpG,dp[i][j+1][w])
#             if i<n and j<m:
#                 dp[i+1][j+1][w]=max(tmpA,tmpB,tmpC,tmpD,tmpE,tmpF,tmpG,dp[i+1][j+1][w])
# print(dp[n][m][k])

# n,m,k=map(int,input().split())
# a=list(map(int,input().split()))
# b=list(map(int,input().split()))
# i,j=0,0
# ai,bj=0,0
# while True:
#     if len(a)<=i:
#         ai=10**9+7
#     else:
#         ai=a[i]
#     if len(b)<=j:
#         bj=10**9+7
#     else:
#         bj=b[j]
#     if k<ai and k<bj:
#         break
#     if ai<bj:
#         k-=ai
#         i+=1
#     else:
#         k-=bj
#         j+=1
#     # print(i,j,k)
# print(i+j)
