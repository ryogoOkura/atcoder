n=int(input())
a=list(map(int,input().split()))
aDict={}
for key in set(a):
    aDict[key]=0
for ai in a:
    aDict[ai]+=1

canPuton=False
if len(aDict)==1:
    if 0 in aDict.keys():
        canPuton=True

elif len(aDict)==2:
    if 0 in aDict.keys():
        if n%3==0:
            canPuton=True
            for key in aDict:
                if key==0:
                    if aDict[key]!=n//3:
                        canPuton=False
                else:
                    if aDict[key]!=2*n//3:
                        canPuton=False

elif len(aDict)==3:
    a,b,c=aDict.keys()
    if n%3==0:
        if (a^b)==c:
            canPuton=True
            for key in aDict.keys():
                if aDict[key]!=n//3:
                    canPuton=False
if canPuton:
    print('Yes')
else:
    print('No')
