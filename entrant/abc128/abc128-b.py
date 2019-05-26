n=int(input())
sp=[list(input().split()) for _ in range(n)]
for i in range(n):
    sp[i][1]=int(sp[i][1])
    sp[i].append(i+1)
# print(sp)
sp.sort(key=lambda x:(x[0],-x[1]))
# print(sp)
for i in range(n):
    print(sp[i][2])
