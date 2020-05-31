n=int(input())
ab=[list(map(int,input().split())) for _ in range(n)]
ab.sort(key=lambda x:x[0])
# print(ab)
if n%2==0:
    min=ab[n//2-1][0]+ab[n//2][0]
else:
    min=ab[n//2][0]
ab.sort(key=lambda x:-x[1])
if n%2==0:
    max=ab[n//2-1][1]+ab[n//2][1]
else:
    max=ab[n//2][1]
print(max-min+1)
