
def main():
    p=10**9+7
    h,w=map(int,input().split())
    s=[input() for _ in range(h)]
    cnt=[[0 for _ in range(w)]for _ in range(h)]
    cnt[0][0]=1
    for hi in range(h):
        for wi in range(w):
            if s[hi][wi]=='.':
                now=cnt[hi][wi]
                # 右を探す
                wj=wi+1
                rFrag=False
                if wj<w:
                    if s[hi][wj]=='.':
                        rFrag=True
                while rFrag:
                    cnt[hi][wj]+=now
                    wj+=1
                    if wj>=w:
                        rFrag=False
                    elif s[hi][wj]=='#':
                        rFrag=False
                # 下を探す
                hj=hi+1
                dFrag=False
                if hj<h:
                    if s[hj][wi]=='.':
                        dFrag=True
                while dFrag:
                    cnt[hj][wi]+=now
                    hj+=1
                    if hj>=h:
                        dFrag=False
                    elif s[hj][wi]=='#':
                        dFrag=False
                # 右下を探す
                hj,wj=hi+1,wi+1
                rdFrag=False
                if hj<h and wj<w:
                    if s[hj][wj]=='.':
                        rdFrag=True
                while rdFrag:
                    cnt[hj][wj]+=now
                    hj+=1
                    wj+=1
                    if hj>=h:
                        rdFrag=False
                    elif wj>=w:
                        rdFrag=False
                    elif s[hj][wj]=='#':
                        rdFrag=False
    ans=cnt[h-1][w-1]%p
    # print(cnt)
    return ans

if __name__=='__main__':
    ans=main()
    print(ans)
