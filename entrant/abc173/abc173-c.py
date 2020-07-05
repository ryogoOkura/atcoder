h,w,k=map(int,input().split())
c=''
for i in range(h):
    c+=input()
# print(c)
# row_dot_cnt=[c.count() for _ in range(h)]
# col_dot_cnt=[0]*w
ans=0
for i in range(2**h): # 行
    i_bin=format(i,'06b')
    for j in range(2**w): # 列
        j_bin=format(j,'06b')
        cnt=0
        # print(i_bin,j_bin)
        for s in range(h):
            if i_bin[5-s]=='0':
                for t in range(w):
                    if j_bin[5-t]=='0' and c[s*w+t]=='#':
                        # print(s,t)
                        cnt+=1
        if cnt==k:
            ans+=1
            # print(f'        {cnt}   {ans}')
print(ans)
