def sousa(k,hand,v):
    if k==0:
        # print(k,sum(hand),hand,v)
        ans.append(sum(hand))
        return
    if len(v)>0:
        # 左から取る
        sousa(k-1,hand+[v[0]],v[1:])
        # 右から取る
        sousa(k-1,hand+[v[-1]],v[:-1])

    if len(hand)>0:
        # 右に入れる
        hand.sort()
        sousa(k-1,hand[1:],v+[hand[0]])
        # 左に入れる
        sousa(k-1,hand[1:],[hand[0]]+v)



n,k=map(int,input().split())
v=list(map(int,input().split()))
ans=[0]
sousa(k,[],v)
# print(ans)
print(max(ans))
