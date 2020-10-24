def main():
    n=int(input())
    for i in range(1,26): # 5^26 > 10^18
        tmp=n-5**i
        if tmp<1: # 次のiでもtmp<1になる
            break
        j=0
        while tmp>1 and j!=-1:
            if tmp%3==0:
                tmp=tmp//3
                j+=1
            else:
                j=-1
        if j>0:
            print(j,i)
            return
    print(-1)
    return

if __name__=='__main__':
    main()
