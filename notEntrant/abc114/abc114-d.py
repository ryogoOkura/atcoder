# 75=3*5*5
# N=a^2*b^4*c^4 | a^14+b^4 | a^24*b^2 | a^74
n=int(input())

# 素因数分解していく
cntPrimeFactor=[0 for _ in range(n+1)]
for i in range(2,n+1):
    tmp=i
    for j in range(2,i+1):
        while tmp%j==0:
            cntPrimeFactor[j]+=1
            tmp//=j # //整数の商

def num(m):
    return len(list(filter(lambda x:x>=m,cntPrimeFactor)))

print(
    num(74)
    +num(24)*(num(2)-1)
    +num(14)*(num(4)-1)
    +num(4)*(num(4)-1)*(num(2)-2)//2 # 4,4,2の組み合わせの数
    )
