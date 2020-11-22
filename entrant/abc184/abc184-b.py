
def main():
    n,x=map(int,input().split())
    s=input()
    ans=x
    for si in s:
        if si=='o':
            ans+=1
        elif ans!=0:
            ans-=1
    return ans

if __name__=='__main__':
    ans=main()
    print(ans)
