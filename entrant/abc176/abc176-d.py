from collections import deque
import math

def solve3(s_flag,h,w,goal_h,goal_w,que):
    while True:
        visited=set()
        while que:
            ch,cw=que.popleft()
            visited.add((ch,cw))
            ## 現在地のコスト
            now=s_flag[ch][cw]
            for d_h,d_w in [(1,0),(0,1),(0,-1),(-1,0)]:
                ## 迷路の外に出ない
                if ch+d_h<0 or h-1<ch+d_h:
                    continue
                if cw+d_w<0 or w-1<cw+d_w:
                    continue
                ## 進行方向のコスト
                dest=s_flag[ch+d_h][cw+d_w]
                if dest!='#': ## 道
                    if dest>now:
                        s_flag[ch+d_h][cw+d_w]=now
                        que.append([ch+d_h,cw+d_w])
        jumping=set()
        for ch,cw in visited:
            now=s_flag[ch][cw]
            for d_h,d_w in [(1,0),(0,1),(0,-1),(-1,0)]:
                jump=[  (d_h+d_w,d_w+d_h),
                        (d_h-d_w,d_w-d_h),
                        (d_h*2,d_w*2),
                        (d_h*2+d_w,d_w*2+d_h),
                        (d_h*2-d_w,d_w*2-d_h),
                        (d_h*2+d_w*2,d_w*2+d_h*2),
                        (d_h*2-d_w*2,d_w*2-d_h*2)]
                for jump_h,jump_w in jump:
                    if ch+jump_h<0 or h-1<ch+jump_h:
                        continue
                    if cw+jump_w<0 or w-1<cw+jump_w:
                        continue
                    jumping.add((ch+jump_h,cw+jump_w))
        if len(jumping)==0:
            break
        for d_jump_h,d_jump_w in jumping:
            ## ワープ先のコスト
            dest_jump=s_flag[d_jump_h][d_jump_w]
            if dest_jump!='#' and dest_jump>now+1:
                s_flag[d_jump_h][d_jump_w]=now+1
                que.append([d_jump_h,d_jump_w])

    # for i in range(h):
    #     print(s_flag[i])
    return s_flag[goal_h][goal_w]


def solve2(s_flag,h,w,goal_h,goal_w,que):
    while que:
        ch,cw=que.popleft()
        ## 現在地のコスト
        now=s_flag[ch][cw]
        for d_h,d_w in [(1,0),(0,1),(0,-1),(-1,0)]:
            ## 迷路の外に出ない
            if ch+d_h<0 or h-1<ch+d_h:
                continue
            if cw+d_w<0 or w-1<cw+d_w:
                continue
            ## 進行方向のコスト
            dest=s_flag[ch+d_h][cw+d_w]
            if dest=='#': ## wall
                # jump=[(d_h*2,d_w*2)]
                # for tmp in range(1,3):
                #     jump.append((d_h*2+d_w*tmp,d_w*2+d_h*tmp))
                #     jump.append((d_h*2-d_w*tmp,d_w*2-d_h*tmp))
                jump=[  (d_h+d_w,d_w+d_h),
                        (d_h-d_w,d_w-d_h),
                        (d_h*2,d_w*2),
                        (d_h*2+d_w,d_w*2+d_h),
                        (d_h*2-d_w,d_w*2-d_h),
                        (d_h*2+d_w*2,d_w*2+d_h*2)]
                for jump_h,jump_w in jump:
                    if ch+jump_h<0 or h-1<ch+jump_h:
                        continue
                    if cw+jump_w<0 or w-1<cw+jump_w:
                        continue
                    ## ワープ先のコスト
                    dest_jump=s_flag[ch+jump_h][cw+jump_w]
                    if dest_jump!='#' and dest_jump>now+1:
                        s_flag[ch+jump_h][cw+jump_w]=now+1
                        que.append([ch+jump_h,cw+jump_w])
            else: ## 道
                if dest>now:
                    s_flag[ch+d_h][cw+d_w]=now
                    que.append([ch+d_h,cw+d_w])
    # for i in range(h):
    #     print(s_flag[i])
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
    ans=solve3(s_flag,h,w,dh,dw,que)
    if ans==math.inf:
        ans=-1
    return ans

if __name__=='__main__':
    ans=main()
    print(ans)
