from collections import deque
import math

def solve2(s_flag,h,w,goal_h,goal_w,que):
    while que:
        ch,cw=que.popleft()
        now=s_flag[ch][cw]
        for dh,dw in [(1,0),(0,1),(0,-1),(-1,0)]:
            if ch+dh<0 or h-1<ch+dh:
                continue
            if cw+dw<0 or w-1<cw+dw:
                continue
            dist=s_flag[ch+dh][cw+dw]
            if dist=='#': ## wall
                jump=[(dh*2,dw*2)]
                for tmp in range(1,3):
                    jump.append((dh*2+dw*tmp,dw*2+dh*tmp))
                    jump.append((dh*2-dw*tmp,dw*2-dh*tmp))
                for jump_h,jump_w in jump:
                    if ch+jump_h<0 or h-1<ch+jump_h:
                        continue
                    if cw+jump_w<0 or w-1<cw+jump_w:
                        continue
                    dist_jump=s_flag[ch+jump_h][cw+jump_w]
                    if dist_jump!='#' and dist_jump>now+1:
                        s_flag[ch+jump_h][cw+jump_w]=now+1
                        que.append([ch+jump_h,cw+jump_w])
            else:
                if dist>now:
                    s_flag[ch+dh][cw+dw]=now
                    que.append([ch+dh,cw+dw])
    return s_flag[goal_h][goal_w]

def solve(s_flag,h,w,ch,cw,jump_cnt):
    # print(ch,cw,jump_cnt)
    # print(s_flag)
    if s_flag[ch][cw]==-1:
        return [(ch,cw,jump_cnt)]
    s_flag[ch][cw]=1 ## 1:visited
    for dh,dw in [(1,0),(0,1),(0,-1),(-1,0)]:
        if ch+dh<0 or h-1<ch+dh:
            continue
        if cw+dw<0 or w-1<cw+dw:
            continue
        if s_flag[ch+dh][cw+dw]==2: ## 2:wall
            jump=[(dh*2,dw*2)]
            for tmp in range(1,3):
                jump.append((dh*2+dw*tmp,dw*2+dh*tmp))
                jump.append((dh*2-dw*tmp,dw*2-dh*tmp))
            for jump_h,jump_w in jump:
                if ch+jump_h<0 or h-1<ch+jump_h:
                    continue
                if cw+jump_w<0 or w-1<cw+jump_w:
                    continue
                if s_flag[ch+jump_h][cw+jump_w]<=0:
                    route=solve(s_flag,h,w,ch+jump_h,cw+jump_w,jump_cnt+1)
                    if route:
                        return [(ch,cw,jump_cnt)]+route
        elif s_flag[ch+dh][cw+dw]<=0: ## 0:road -1:goal
            route=solve(s_flag,h,w,ch+dh,cw+dw,jump_cnt)
            if route:
                return [(ch,cw,jump_cnt)]+route


def main():
    h,w=map(int,input().split())
    ch,cw=map(int,input().split())
    ch,cw=ch-1,cw-1
    dh,dw=map(int,input().split())
    dh,dw=dh-1,dw-1
    s=[input() for i in range(h)]
    ## .=0 #=2 visited=1 goal=-1
    # s_flag=[[0 if s[i][j]=='.' else 2 for j in range(w)] for i in range(h)]
    # s_flag[ch][cw]=1
    # s_flag[dh][dw]=-1
    # ans=solve(s_flag,h,w,ch,cw,0)
    # if not ans:
    #     ans=-1
    # else:
    #     ans=ans[-1][2]
    # return ans
    ## .=inf #=# visited=cost
    s_flag=[[math.inf if s[i][j]=='.' else '#' for j in range(w)] for i in range(h)]
    s_flag[ch][cw]=0
    que=deque([[ch,cw]])
    ans2=solve2(s_flag,h,w,dh,dw,que)
    if ans2==math.inf:
        ans2=-1
    return ans2

if __name__=='__main__':
    ans=main()
    print(ans)
