n=int(input())
l=list(map(int,input().split()))
l.sort()
l.reverse()
sum=0
for i in range(1,n):
    sum+=l[i]

if sum>l[0]:
    print('Yes')
else:
    print('No')
