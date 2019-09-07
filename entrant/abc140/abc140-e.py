# すべての(L,R)について行うので順番は任意
# TLE
n=int(input())
p=list(map(int,input().split()))
ans=0

for l in range(n-1):
    if p[l]>p[l+1]:
        pre1st,pre2nd=p[l],p[l+1]
    else:
        pre1st,pre2nd=p[l+1],p[l]
    ans+=pre2nd
    for r in range(l+2,n):
        if pre1st<p[r]:
            pre1st,pre2nd=p[r],pre1st
        else:
            if pre2nd<p[r]:
                pre2nd=p[r]
        ans+=pre2nd

print(ans)

# TLE
# n=int(input())
# p=list(map(int,input().split()))
# ans=0
# for width in range(1,n):
#     for i in range(n-width):
#         tmp=p[i:i+width+1]
#         # print(tmp)
#         tmp.sort()
#         ans+=tmp[-2]
# print(ans)
