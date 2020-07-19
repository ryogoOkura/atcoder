import math
n,m=map(int,input().split())
a=list(map(int,input().split()))
half_a=[ai//2 for ai in a]
# print(half_a)
lcm=half_a[0]
for i in range(n-1):
    a,b=lcm,half_a[i+1]
    lcm=a*b//math.gcd(a,b)
# print(lcm)
pow_cnt=0
tmp=half_a[0]
while tmp%2==0:
    pow_cnt+=1
    tmp=tmp//2
flag=True
for ai in half_a[1:]:
    if ai%(2**pow_cnt)!=0:
        flag=False
        break
    elif  ai%(2**(pow_cnt+1))==0:
        flag=False
        break
if flag:
    print(math.ceil(m//lcm/2))
else:
    print(0)



# import math
# n,m=map(int,input().split())
# a=list(map(int,input().split()))
# half_a=list(set([ai//2 for ai in a]))
# half_a.sort()
# half_a_flag=[]
# for i in range(len(half_a)):
#     for j in range(i+1,len(half_a)):
#         if half_a[j]%half_a[i]==0:
#             half_a_flag.append(False)
#         else:
#             half_a_flag.append(True)
# half_a_flag.append(True)
# tmp=[]
# for i in range(len(half_a)):
#     if half_a_flag[i]:
#         tmp.append(half_a[i])
# half_a=tmp
# # print(half_a)
# lcm=-1
# for i in range(len(half_a)-1):
#     if half_a_flag[i]:
#         if lcm==-1:
#             lcm=half_a[i]
#         a,b=lcm,half_a[i+1]
#         lcm=a*b//math.gcd(a,b)
# if len(half_a)==1:
#     lcm=half_a[0]
# # print(lcm)
# oddcnt,evencnt=0,0
# for hi in half_a:
#     if hi!=1:
#         if hi%2==0:
#             evencnt+=1
#         else:
#             oddcnt+=1
# if evencnt>0 and oddcnt>0:
#     print(0)
# else:
#     print(math.ceil(m//lcm/2))
