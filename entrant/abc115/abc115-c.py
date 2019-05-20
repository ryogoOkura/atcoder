n,k=map(int,input().split())
h=[]
for i in range(n):
    h.append(int(input()))

h.sort()
dim=[]
for i in range(n-k+1):
    dim.append(h[i+k-1]-h[i])
dim.sort()
print(dim[0])
