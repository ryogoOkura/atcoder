# できなかった
# a1,...,anがdivisorで割り切れる、すなわちdivisorはMの約数である
n,m=map(int,input().split())

divisors=[]
for i in range(1,int(m**0.5)+1):
    if m%i==0:
        divisors.append(i)
        if i!=m//i:
            divisors.append(m//i)

divisors.sort(key=lambda x:-x)
# print(divisors)
for d in divisors:
    if d<=m//n:
        print(d)
        break
