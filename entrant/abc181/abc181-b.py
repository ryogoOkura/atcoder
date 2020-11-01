
def main():
    n=int(input())
    ans=0
    for i in range(n):
        ai,bi=map(int,input().split())
        ans+=(ai+bi)*(bi-ai+1)//2
    return ans

if __name__=='__main__':
    ans=main()
    print(ans)
