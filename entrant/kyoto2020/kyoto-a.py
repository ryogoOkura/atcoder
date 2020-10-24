def main():
    n=int(input())
    xy=[tuple(map(int,input().split())) for _ in range(n)]
    ans=0
    for i in range(1,n):
        ans+=abs(xy[i][0]-xy[i-1][0])+abs(xy[i][1]-xy[i-1][1])

    return ans

if __name__=='__main__':
    ans=main()
    print(ans)
