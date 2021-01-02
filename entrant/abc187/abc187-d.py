
def main():
    n=int(input())
    ab=[tuple(map(int,input().split())) for _ in range(n)]
    aoki=0
    effect=[]
    for i in range(n):
        ai,bi=ab[i]
        aoki+=ai
        effect.append(ai*2+bi)
    effect.sort(key=lambda x:-x)
    # print(aoki,effect)
    ans=0
    for i in range(n):
        aoki-=effect[i]
        ans+=1
        if aoki<0:
            break
    return ans

if __name__=='__main__':
    ans=main()
    print(ans)
