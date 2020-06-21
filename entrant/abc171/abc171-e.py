n=int(input())
a=list(map(int,input().split()))
# for i in range(n):
#     print(format(a[i],'08b'))
# print()
tmp=a[0]
for i in range(1,n):
    tmp=tmp^a[i]
for i in range(n):
    print(tmp^a[i],end=' ')
