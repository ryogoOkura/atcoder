s=input()
ans='keyence'
i=0 # index of s
index=0 # index of ans
isCut=0
canRestart=0
restart=0
lenS=len(s)
while i<lenS:
    # print(i,index,end='=>')
    if isCut==1: # 切られたあと
        if index>6: # 7=len(ans)
            if canRestart:
                canRestart=0
                isCut=-1
                i=restartI
                index=restartIndex
            else:
                break
        else:
            if s[i]==ans[index]:
                index+=1
            else:
                if canRestart:
                    canRestart=0
                    isCut=-1
                    i=restartI
                    index=restartIndex
                else:
                    break
    elif isCut==-1: # 切られている途中
        if s[i]==ans[index]:
            # 切り方を変えるときはiとindexを戻す
            restartIndex=index
            restartI=i
            canRestart=1
            isCut=1
            index+=1
    else: # 切られる前
        if s[i]==ans[index]:
            index+=1
        else:
            isCut=-1
    i+=1
    # print(i,index,isCut)
if (index<=6)|(i<lenS)|(isCut==-1): # 7=len(ans)
    print('NO')
else:
    print('YES')
