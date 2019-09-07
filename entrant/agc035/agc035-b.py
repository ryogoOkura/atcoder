n,m=map(int,input().split())
sides=[(0,0) for _ in range(m)]
for i in range(m):
    ai,bi=map(int,input().split())
    ai,bi=ai-1,bi-1
    sides[i]=[ai,bi]

sides.sort(key=lambda x:(x[0],x[1]))
# print(sides)

if m%2==0:
    ans=-1
    for j in range(2**m):
        cnt=[0 for _ in range(n)]
        for i in range(m):
            cnt[sides[i][(j>>i)%2]]+=1
        canMake=True
        for k in range(n):
            if cnt[k]%2!=0:
                canMake=False
        if canMake:
            ans=j
            break
    if ans==-1:
        print(-1)
    else:
        for i in range(m):
            ai,bi=sides[i][:]
            if (j>>i)%2!=0:
                ai,bi=bi,ai
            print(ai+1,bi+1)
else:
    print(-1)


# # 辺の番号,　頂点の番号,　カウント,　辺の組
# def calc(i,j,cnt,ans):
#     # print(ans)
#     if i==m:
#         if cnt[j]%2==0:
#             answers.append(ans)
#     else:
#         ai,bi=sides[i]
#         if j==ai:
#             cnt[ai]+=1
#             calc(i+1,j,cnt,ans+[(ai,bi)])
#             cnt[ai]-=1
#             cnt[bi]+=1
#             calc(i+1,j,cnt,ans+[(bi,ai)])
#         else:
#             if cnt[j]%2==0:
#                 calc(i,j+1,cnt,ans)
#
#
# if m%2==0:
#     answers=[]
#     calc(0,0,[0 for _ in range(n)],[])
#     if len(answers)==0:
#         print(-1)
#     else:
#         for ai,bi in answers[0]:
#             print(ai+1,bi+1)
# else:
#     print(-1)
