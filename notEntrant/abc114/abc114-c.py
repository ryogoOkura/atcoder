import math
n=int(input())
digitSize=2
while math.floor(n/(10**digitSize))>0:
    digitSize+=1
# print('digitSize={}'.format(digitSize))

shime=[[],[],[],[357,375,537,573,735,753]]
def makeShime(nowDigitSize):
    shime.append([])
    for num in shime[nowDigitSize-1]:
        for i in range(nowDigitSize): # 挿入箇所
            for j in (3,5,7): # 挿入する値
                newNum=math.floor(num/(10**i))*10+j
                newNum=newNum*(10**i)+num%(10**i)
                shime[nowDigitSize].append(newNum)
    shime[nowDigitSize]=list(set(shime[nowDigitSize]))
    shime[nowDigitSize].sort()
    if nowDigitSize<digitSize:
        makeShime(nowDigitSize+1)
makeShime(4)
# print(shime)
# for i in range(digitSize+1):
#     print(len(shime[i]),end=',')

i=0
sh=shime[digitSize]
le=len(shime[digitSize])
while True:
    if i>=le:
        break
    if n<sh[i]:
        break
    i+=1

cnt=i
for i in range(digitSize):
    cnt+=len(shime[i])
print(cnt)
