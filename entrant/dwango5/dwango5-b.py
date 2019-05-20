import math

n,k=map(int,input().split())
a=list(map(int,input().split()))
added_a=[0]
for i in range(n):
    added_a.append(added_a[i]+a[i])
# print(added_a)
beauty=[[]]
for i in range(n+1):
    for j in range(i+1,n+1):
        beauty[0].append(added_a[j]-added_a[i])
print(beauty[0])
beauty[0].sort()
beauty[0].reverse()
tmp=0
max_exponent=math.floor(math.log(beauty[0][0])/math.log(2))
for i in range(max_exponent+1):
    beauty.append([])
    print(beauty[i])
    cnt=0
    for j in range(len(beauty[i])):
        if beauty[i][j]>=2**(max_exponent-i):
            cnt+=1
            beauty[i+1].append(beauty[i][j]-2**(max_exponent-i))
    if cnt>=k:
        tmp+=2**(max_exponent-i)
    else:
        beauty[i+1]=beauty[i]

print(tmp)
