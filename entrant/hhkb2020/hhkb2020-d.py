p=10**9+7
def main(): #TLE
    n,a,b=map(int,input().split())
    if a<b:
        a,b=b,a
    # ans=pow(n-a+1,2)*pow(n-b+1,2) # それぞれの置き方（重なり無視）
    # ans-=pow(n-a+1,2)*pow(a-b+1,2) # 大きい方の中に小さい方が完全に収まる置き方
    # ans-=  # 一部のみ重なる置き方
    # print(ans)

    ans=pow(n-a+1,2)*pow(n-b+1,2) # それぞれの置き方（重なり無視）
    for k in range(n-a+1):
        h_up=min(k,b-1)
        h_down=min(n-a-k,b-1)
        h=h_up+a+h_down # aの上下にb-1伸ばした長さ（ぶつかったらそこまで）
        for l in range(n-a+1):
            w_left=min(l,b-1)
            w_right=min(n-a-l,b-1)
            w=w_left+a+w_right # aの左右にb-1伸ばした長さ（ぶつかったらそこまで）
            ans-=(h-b+1)*(w-b+1)
    return ans%p

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        ans=main()
        print(ans)
