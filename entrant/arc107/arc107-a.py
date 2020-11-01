
def main():
    p=998244353
    a,b,c=map(int,input().split())
    ans=(a*(a+1)//2)%p
    ans=(ans*b*(b+1)//2)%p
    ans=(ans*c*(c+1)//2)%p
    return ans

if __name__=='__main__':
    ans=main()
    print(ans)
