
def main():
    n,k=map(int,input().split())
    ans=0
    for i in range(2,2*n+1): # i=c+d
        if 2<=k+i<=2*n: # k+i=a+b
            cdCnt=i-1 if i<=n+1 else 2*n-i+1
            abCnt=k+i-1 if k+i<=n+1 else 2*n-(k+i)+1
            ans+=abCnt*cdCnt
    return ans

if __name__=='__main__':
    ans=main()
    print(ans)
