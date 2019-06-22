n=int(input())
x=[0 for _ in range(n)]
y=[0 for _ in range(n)]
for i in range(n):
    x[i],y[i]=map(int,input().split())
sx=sorted(x)
sy=sorted(y)
candidateX=[0 for _ in range(sx[-1])]
candidateY=[0 for _ in range(sy[-1])]
for i in range(n):
    candidateX[sx[i]]+=1
    candidateY[sy[i]]+=1



print(x)
