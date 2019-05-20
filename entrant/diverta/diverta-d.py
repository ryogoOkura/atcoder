def make_divisors(n):
    ans=0
    for i in range(1,int(n**0.5)+1):
        if n%i==0:
            if i>2:
                if n//i < i-1:
                    ans+=i-1
            if i!=n//i:
                if i < n//i-1:
                    ans+=n//i-1
    return ans

n=int(input())
print(make_divisors(n))

# n=int(input())
# ans=0
# for i in range(3,n+1):
#     if n%i==0:
#         ans+=i-1
# print(ans)

# n=int(input())
# ans=0
# for i in range(1,n):
#     if n//i==n%i:
#         ans+=i
