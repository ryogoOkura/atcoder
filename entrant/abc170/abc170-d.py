n=int(input())
a=list(map(int,input().split()))
a.sort()
aMax=a[-1]
isAns=[0]*(aMax+1) ## 1=ans 2=multiple or plural
for ai in a:
    isAns[ai]+=1
    if isAns[ai]==1:
      for j in range(2*ai,aMax+1,ai):
        isAns[j]+=2

print(isAns.count(1))

## WA
# n=int(input())
# a=list(map(int,input().split()))
# a.sort()
# isAns=[True]*n
# for i in range(n-1):
#     if isAns[i]:
#         for j in range(i+1,n):
#             if isAns[j]:
#                 if a[j]%a[i]==0:
#                     isAns[j]=False
# if n>1:
#     if a[0]==a[1]:
#         isAns[0]=False
# print(sum(isAns))



## dame
# n=int(input())
# a=list(map(int,input().split()))
# a.sort(reverse=True)
# ans=1
# for i in range(n-1):
#     flg=True
#     for j in range(n-1,i,-1):
#         if a[i]%a[j]==0:
#             flg=False
#             break
#     if flg:
#         ans+=1
# if n>1:
#     if a[-1]==a[-2]:
#         ans-=1
# print(ans)
