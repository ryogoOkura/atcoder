# うまく効率化できなかった
# 2 6=>4 (1,6)*2,(2,3)*2
# 3 12=>18 (1,1,12)*3,(1,2,6)*6,(1,3,4)*6,(2,2,3)*3

# import math
# def comb(a,b): # aCb
#     return math.factorial(a)//math.factorial(a-b)//math.factorial(b)
def comb(a,b):
    b=min(b,a-b)
    result=1
    for i in range(a,a-b,-1):
        result*=i
    for i in range(1,b+1):
        result//=i
    return result

n,m=map(int,input().split())
divisor={}
tmp=m
# for i in range(2,m+1):
#     while tmp%i==0:
#         tmp//=i
#         divisor.setdefault(i,0)
#         divisor[i]+=1
#         if tmp==1:
#             break
i=2
while i*i<=m:
    while tmp%i==0:
        tmp//=i
        divisor.setdefault(i,0)
        divisor[i]+=1
    i+=1
if tmp>1:
    divisor[tmp]=1
# print(divisor)
cnt=1
for key in divisor:
    c=divisor[key]
    cnt*=comb(c+n-1,c)
print(cnt%1000000007)
