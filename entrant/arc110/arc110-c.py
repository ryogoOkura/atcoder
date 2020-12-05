
def main():
    n=int(input())
    p=list(map(int,input().split()))
    # 正解の場所にいない（1回はスワップするため）
    # 2種類の昇順列の混合
    # 1から始まる方（p[0]を要素に含まない方）の列は、次の要素が1つ前の要素がいた位置になってるはず（１回ずつスワップするため）
    tmpA,tmpB=0,-1
    listA,listB=[],[]
    for i in range(n):
        pi=p[i]
        if i+1==pi:
            print(-1)
            return
        if tmpA>tmpB:
            if pi>tmpA:
                tmpA=pi
                listA.append([i,pi])
            elif pi>tmpB:
                tmpB=pi
                listB.append([i,pi])
            else:
                print(-1)
                return
        else:
            if pi>tmpB:
                tmpB=pi
                listB.append([i,pi])
            elif pi>tmpA:
                tmpA=pi
                listA.append([i,pi])
            else:
                print(-1)
                return
    # print(listA)
    # print(listB)
    if listA[0][0]==0:
        listA=listB.copy()
    pre_i=0
    for i,ai in listA:
        if pre_i+1!=ai:
            print(-1)
            return
        pre_i=i
    pre_i=0
    for i,ai in listA:
        for j in range(i,pre_i,-1):
            print(j)
        pre_i=i
    return

if __name__=='__main__':
    main()
