def solve(a,b,c,cnt):
    if a==100 or b==100 or c==100:
        return cnt
    ans1,ans2,ans3=0,0,0
    if a!=0:
        ans1=a/(a+b+c)*solve(a+1,b,c,cnt+1)
    if b!=0:
        ans2=b/(a+b+c)*solve(a,b+1,c,cnt+1)
    if c!=0:
        ans3=c/(a+b+c)*solve(a,b,c+1,cnt+1)
    return ans1+ans2+ans3

def main():
    a,b,c=map(int,input().split())
    ans=solve(a,b,c,0)

    return ans

if __name__=='__main__':
    ans=main()
    print(ans)
