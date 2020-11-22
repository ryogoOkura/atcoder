
def main():
    r1,c1=map(int,input().split())
    r2,c2=map(int,input().split())
    bslash=abs((r1+c1)-(r2+c2)) # \
    slash=abs((r1-c1)-(r2-c2)) # /
    # print(bslash,slash)
    ans=0
    if r1==r2 and c1==c2:
        ans=0
    elif bslash==0 or slash==0 or abs(r1-r2)+abs(c1-c2)<=3:
        ans=1
    else:
        ans=1
        if bslash%2==0 or bslash<=3 or slash%2==0 or slash<=3:
            ans+=1
        else:
            ans+=2
    return ans

if __name__=='__main__':
    ans=main()
    print(ans)
