
def main():
    n=int(input())
    xy=[tuple(map(int,input().split())) for _ in range(n)]
    ans=0
    for i in range(n):
        xi,yi=xy[i]
        tmp1=yi+xi
        tmp2=yi-xi
        for j in range(i+1,n):
            xj,yj=xy[j]
            tmp3=yj+xj
            tmp4=yj-xj
            if (tmp1<=tmp3 and tmp2>=tmp4) or (tmp1>=tmp3 and tmp2<=tmp4):
                ans+=1

    return ans

if __name__=='__main__':
    ans=main()
    print(ans)
