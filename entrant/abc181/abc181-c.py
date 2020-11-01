
def main():
    n=int(input())
    xy=[tuple(map(int,input().split())) for _ in range(n)]
    ans='No'
    for i in range(n):
        xi,yi=xy[i]
        for j in range(i+1,n):
            xj,yj=xy[j]
            for k in range(j+1,n):
                xk,yk=xy[k]
                if (xi-xj)*(yi-yk)==(xi-xk)*(yi-yj):
                    ans='Yes'
                    break

    return ans

if __name__=='__main__':
    ans=main()
    print(ans)
