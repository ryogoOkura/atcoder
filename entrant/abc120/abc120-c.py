# s=input()
# flag=1
# length=len(s)
# while flag:
#     l=len(s)
#     if l<=1:
#         break
#     for i in range(1,l):
#         if s[i-1]!=s[i]:
#             s=s[:i-1]+s[i+1:]
#             break
#         elif i==l-1:
#             flag=0
# print(length-len(s))

# s=input()
# flag=1
# length=len(s)
# s_flag=[1 for _ in range(length)]
# while flag:
#     l=sum(s_flag)
#     if l<=1:
#         break
#     comp=0
#     while s_flag[comp]==0:
#         comp+=1
#     # print(s_flag,comp)
#     for i in range(comp+1,length):
#         if s_flag[i]:
#             if s[comp]!=s[i]:
#                 s_flag[comp]=0
#                 s_flag[i]=0
#                 break
#             else:
#                 comp=i
#                 if i==length-1:
#                     flag=0
# print(length-sum(s_flag))

s=input()
length=len(s)
cnt=[0,0]
for i in range(length):
    if s[i]=='0':
        cnt[0]+=1
    else:
        cnt[1]+=1
print(min(cnt)*2)
