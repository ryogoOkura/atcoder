N,X=map(int,input().split())
x=list(map(int,input().split()))
diffx=[abs(X-x[i]) for i in range(N)]

def euclid(a,b):
    if b==0:
        return a
    else:
        return euclid(b,a%b)

gcd=diffx[0]
for i in range(1,N):
    gcd=euclid(diffx[i],gcd)
print(gcd)


# minDiff=min(diffx)
# isFinished=0
# for i in range(minDiff,0,-1):
#     if minDiff%i==0:
#         canDivide=1
#         for j in range(N):
#             if diffx[j]%i:
#                 canDivide=0
#                 break
#         if canDivide:
#             print(i)
#             isFinished=1
#             break
#     if isFinished:
#         break
