# 奇数番目と偶数番目の要素の数を調べて計算（TLE)
'''
n=int(input())
v=input().split()
vodd=[]
veven=[]
for i in range(n):
    if i%2:
        veven.append(int(v[i]))
    else:
        vodd.append(int(v[i]))

voddNum=[vodd[0]]
voddCnt=[0]
j=0
for i,odd in enumerate(vodd):
    if voddNum[j]!=odd:
        for k,num in enumerate(voddNum):
            if num==odd:
                j=k
                break
        else:
            j=k+1
            voddNum.append(odd)
            voddCnt.append(0)
    voddCnt[j]+=1
voddSet=list(zip(voddCnt, voddNum))
#voddSet=list(reversed(sorted(voddSet,key=lambda x:x[0])))
voddSet.sort(key=lambda x:x[0])
voddSet.reverse()
# print(vodd)
# print(voddNum)
# print(voddCnt)
# print(voddSet)


vevenNum=[veven[0]]
vevenCnt=[0]
j=0
for i,even in enumerate(veven):
    if vevenNum[j]!=even:
        for k,num in enumerate(vevenNum):
            if num==even:
                j=k
                break
        else:
            j=k+1
            vevenNum.append(even)
            vevenCnt.append(0)
    vevenCnt[j]+=1
vevenSet=list(zip(vevenCnt, vevenNum))
#vevenSet=list(reversed(sorted(vevenSet,key=lambda x:x[0])))
vevenSet.sort(key=lambda x:x[0])
vevenSet.reverse()
# print()
# print(veven)
# print(vevenNum)
# print(vevenCnt)
# print(vevenSet)


changeCnt=len(vodd)+len(veven)
if voddSet[0][1]==vevenSet[0][1]:
    if len(voddSet)==1 & len(vevenSet)==1:
        changeCnt-=len(vodd)
    elif len(voddSet)==1:
        changeCnt-=vevenSet[0][0]
    elif len(vevenSet)==1:
        changeCnt-=voddSet[0][0]
    else:
        if voddSet[1][0]>vevenSet[1][0]:
            changeCnt=changeCnt-voddSet[1][0]-vevenSet[0][0]
        else:
            changeCnt=changeCnt-voddSet[0][0]-vevenSet[1][0]
else:
    changeCnt+=-voddSet[0][0]-vevenSet[0][0]

print(changeCnt)
#'''

# 0個の要素と辞書を利用して計算量をへらす
# changeCntの数え方にミスを発見
n=int(input())
v=map(int,input().split())
vodd={-1:0}
veven={-1:0}
for i,vi in enumerate(v):
    if i%2:
        if(vi in veven):
            veven[vi]+=1
        else:
            veven[vi]=1
    else:
        if(vi in vodd):
            vodd[vi]+=1
        else:
            vodd[vi]=1
veven=list(veven.items())
veven.sort(key=lambda x:-x[1])
vodd=list(vodd.items())
vodd.sort(key=lambda x:-x[1])
if veven[0][0]==vodd[0][0]:
    a=veven[0][1]+vodd[1][1]
    b=veven[1][1]+vodd[0][1]
    changeCnt=n-a if a>b else n-b
else:
    changeCnt=n-veven[0][1]-vodd[0][1]

print(changeCnt)

#'''
