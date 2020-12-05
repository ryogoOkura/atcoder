
def main():
    n=int(input()) # len(t)
    t=input()
    ans=0
    if n==1:
        if t[0]=='1':
            ans=10**10*2
        else:
            ans=10**10
    else:
        cnt=0 # 110の繰り返し回数
        flg=0 # 1:(1)10, 2:1(1)0, 3:11(0)
        for i in range(n):
            if t[i]=='1':
                if flg==3 or flg==0:
                    flg+=1
                elif flg==1 or flg==4:
                    flg=2
                elif flg==2:
                    flg=-1
                    break
            else:
                if flg==2 or flg==0 or flg==1:
                    flg=3
                    cnt+=1
                else:
                    flg=-1
                    break
        # print(cnt,flg)
        if flg==-1:
            ans=0
        elif flg==3:
            ans=10**10-cnt+1
        else: # 最後の繰り返しに0がない
            ans=10**10-cnt
    return ans

if __name__=='__main__':
    ans=main()
    print(ans)
