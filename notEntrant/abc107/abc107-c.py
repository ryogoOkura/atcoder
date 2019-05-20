n,k=map(int,input().split())
x=list(map(int,input().split()))
if (0 in x):
    k-=1
else:
    x.append(0)
    x.sort()

zeroPos=x.index(0)
leftLen=zeroPos
rightLen=len(x)-zeroPos-1
# print(leftLen,zeroPos,rightLen)
# print(x)
left=[]
right=[]
for turn in range(leftLen+1):
    if(turn>k):
        break
    if(k-turn<=rightLen):
        left.append(x[zeroPos-turn]*-2 + x[zeroPos+k-turn])
for turn in range(rightLen+1):
    if(turn>k):
        break
    if(k-turn<=leftLen):
        right.append(2*x[zeroPos+turn] + -1*x[zeroPos-k+turn])
minL=min(left)
minR=min(right)
# print(left,right)
print(minL if minL<minR else minR)


# time=[]
# def measureTime(i,regX,nowTime,nowPlace,direct,turnFlg):
#     if i<k:
#         if len(regX)>1:
#             newRegX=regX[:]
#             newRegX.pop(nowPlace)
#             print(regX,newRegX)
#             if (nowPlace>0) & ((direct==0)|(turnFlg!=1)):
#                 newTimeM=nowTime+abs(regX[nowPlace]-regX[nowPlace-1])
#                 # print('{},place={},time={}'.format(newRegX,nowPlace-1,newTimeM))
#                 if direct==1:
#                     turnFlg=1
#                 measureTime(i+1, newRegX, newTimeM, nowPlace-1, 0, turnFlg)
#             if (nowPlace<len(regX)-1) & ((direct==1)|(turnFlg!=1)):
#                 newTimeP=nowTime+abs(regX[nowPlace]-regX[nowPlace+1])
#                 # print('{},place={},time={}'.format(newRegX,nowPlace,newTimeP))
#                 if direct==0:
#                     turnFlg=1
#                 measureTime(i+1, newRegX, newTimeP, nowPlace, 1, turnFlg)
#         else:
#             if i==k:
#                 time.append(nowTime)
#     else:
#         time.append(nowTime)
#
# measureTime(0,x,0,x.index(0),-1,0)
# time.sort()
# print(time[0])
