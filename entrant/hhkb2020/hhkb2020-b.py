
def main():
    h,w=map(int,input().split())
    s=[input() for _ in range(h)]
    ans=0
    for hi in range(h):
        for wi in range(w):
            if s[hi][wi]=='.':
                if wi+1<w:
                    if s[hi][wi+1]=='.':
                        ans+=1
                if hi+1<h:
                    if s[hi+1][wi]=='.':
                        ans+=1

    return ans

if __name__=='__main__':
    ans=main()
    print(ans)
