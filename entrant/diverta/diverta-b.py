r,g,b,n=map(int,input().split())
boxSize=[r,g,b]
boxSize.sort(key=lambda x:-x)
# print(boxSize)
maxCnt=[n//boxSize[i]+1 for i in range(3)]
# print(maxCnt)
ans=0
if boxSize[1]==1:
    for cnt0 in range(maxCnt[0]):
        ans+=n-cnt0*boxSize[0]+1
else:
    for cnt0 in range(maxCnt[0]):
        for cnt1 in range(maxCnt[1]):
            reg=n-cnt0*boxSize[0]-cnt1*boxSize[1]
            if reg<0:
                break
            if reg%boxSize[2]==0:
                ans+=1
print(ans)
