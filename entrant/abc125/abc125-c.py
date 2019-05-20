def gcd(a,b):
    if a*b<0:
        return -a*b
    while b!=0:
        tmp=a%b
        a=b
        b=tmp
    return a

# def gcd_list(numbers):
#     # print(numbers)
#     g=numbers[0]
#     for i in range(n-1):
#         g=gcd(g,numbers[i])
#     return g
#
# n=int(input())
# a=list(map(int,input().split()))
# gcd_without_i=[gcd_list(a[:i]+a[i+1:]) for i in range(n)]
# # print(gcd_without_i)
# print(max(gcd_without_i))

n=int(input())
a=list(map(int,input().split()))
# gcd_lhs[i]=gcd(a[0],...,a[i-1])
gcd_lhs=[-1 for _ in range(n)]
# gcd_rhs[i]=gcd(a[i+1],...,a[n-1])
gcd_rhs=[-1 for _ in range(n)]
gcd_lhs[1]=a[0]
gcd_rhs[n-2]=a[n-1]
for i in range(1,n):
    gcd_lhs[i]=gcd(gcd_lhs[i-1],a[i-1])
    gcd_rhs[n-1-i]=gcd(gcd_rhs[n-i],a[n-i])

gcd_without_i=[gcd(gcd_lhs[i],gcd_rhs[i]) for i in range(n)]
print(max(gcd_without_i))
