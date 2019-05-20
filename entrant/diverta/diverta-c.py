n=int(input())
s=[input() for _ in range(n)]
isFinishA=[s[i][-1]=='A' for i in range(n)]
isStartB=[s[i][0]=='B' for i in range(n)]
ans=0
for si in s:
    wasA=False
    for sij in si:
        if sij=='B':
            if wasA:
                ans+=1
        wasA=(sij=='A')

# fromBtoA=0
# fromB=0
# toA=0
# for i in range(n):
#     if isFinishA[i]:
#         if isStartB[i]:
#             fromBtoA+=1
#         else:
#             toA+=1
#     else:
#         if isStartB[i]:
#             fromB+=1
#
# if fromBtoA==0:
#     ans+=min(fromB,toA)
# else:
#     if fromB+toA>0:
#         ans+=fromBtoA+min(fromB,toA)
#     if fromB+toA==0:
#         ans+=fromBtoA-1
# # print(fromB,toA,fromBtoA)
# print(ans)


cnt=[isFinishA.count(True),isStartB.count(True)]
ans+=min(cnt)
fromBtoA=0
for i in range(n):
    if isFinishA[i] and isStartB[i]:
        fromBtoA+=1

if cnt[0]==cnt[1]==fromBtoA:
    if cnt[0]!=0:
        ans-=1
print(ans)
