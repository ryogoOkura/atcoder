def main():
    n=int(input())
    a=list(map(int,input().split()))
    a_max=a[0]
    ans=0
    for ai in a[1:]:
        if ai<a_max:
            ans+=a_max-ai
        a_max=max(a_max,ai)
    return ans

if __name__=='__main__':
    ans=main()
    print(ans)
