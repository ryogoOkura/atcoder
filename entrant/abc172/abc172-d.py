n=int(input())
## これのループを入れ替えたものを考える
# ans=0
# for i in range(1,n):
#     for j in range(1,n):
#         if i%j==0:
#             ans+=i
# print(ans)
ans=0
for j in range(1,n+1):
    ## j+2j+...+[n/j]j
    tmp=n//j
    ans+=tmp*(tmp+1)*j//2
print(ans)


# def factorization(n):
#     arr = []
#     temp = n
#     for i in range(2, int(-(-n**0.5//1))+1):
#         if temp%i==0:
#             cnt=0
#             while temp%i==0:
#                 cnt+=1
#                 temp //= i
#             arr.append([i, cnt])
#
#     if temp!=1:
#         arr.append([temp, 1])
#
#     if arr==[]:
#         arr.append([n, 1])
#
#     return arr
#
# n=int(input())
# ans=1
# if n==1:
#     print(ans)
# else:
#     for i in range(2,n+1):
#         arr=factorization(i)
#         tmp=1
#         for arri in arr:
#             tmp*=arri[1]+1
#         ans+=tmp*i
#         # print(arr)
#         # print(tmp,ans)
# print(ans)
