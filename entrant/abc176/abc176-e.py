def main():
    h,w,m=map(int,input().split())
    target=[0]*m
    for i in range(m):
        th,tw=map(int,input().split())
        target[i]=(th-1,tw-1)
    lines=[0]*w
    rows=[0]*h
    for th,tw in target:
        lines[tw]+=1
        rows[th]+=1
    max_lines=max(lines)
    max_rows=max(rows)
    max_wi=[i for i,wi in enumerate(lines) if wi==max_lines]
    max_hi=[i for i,hi in enumerate(rows) if hi==max_rows]
    # print(max_rows,max_hi,max_lines,max_wi)
    ans=max_lines+max_rows-1
    for wi in max_wi:
        for hi in max_hi:
            if not (hi,wi) in target:
                ans+=1
                break
    return ans

if __name__=='__main__':
    ans=main()
    print(ans)
