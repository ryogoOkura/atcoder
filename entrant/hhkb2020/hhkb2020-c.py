
def main():
    n=int(input())
    p=list(map(int,input().split()))
    used=set()
    ans=0
    for i in range(n):
        used.add(p[i])
        while ans in used:
            ans+=1
        print(ans)
    return

if __name__=='__main__':
    main()
