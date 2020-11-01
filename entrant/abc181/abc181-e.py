
def main():
    n,m=map(int,input().split())
    h=list(map(int,input().split()))
    w=list(map(int,input().split()))
    h.sort()
    h.append(h[n-1])
    w.sort()
    dim_h=[0 for i in range(n)]
    for i in range(1,n):
        dim_h[i]=h[i]-h[i-1]
    # print(dim_h)
    index=0
    ansLeft=0
    ansRight=sum([dim_h[i] if i%2==0 else 0 for i in range(n)])
    ans=[]
    for wi in w:
        while index<n and wi>h[index]:
            if index%2==1:
                ansLeft+=dim_h[index]
                ansRight-=dim_h[index+1]
            index+=1
        # print(h[:index]+[wi]+h[index:])
        # print(index,ansLeft,abs(h[index]-wi),ansRight)
        if index%2==1:
            ans.append(ansLeft+abs(h[index-1]-wi)+ansRight)
        else:
            ans.append(ansLeft+abs(h[index]-wi)+ansRight)
    return min(ans)

if __name__=='__main__':
    ans=main()
    print(ans)
