nCr = {}
def cmb(n, r):
    if r == 0 or r == n: return 1
    if r == 1: return n
    if (n,r) in nCr: return nCr[(n,r)]
    nCr[(n,r)] = cmb(n-1,r) + cmb(n-1,r-1)
    return nCr[(n,r)]

n=int(input())
s=list(map(int,input().split()))
cnt=[0 for i in range(max(s))]
for si in s:
    cnt[si-1]+=1
# print(cnt)

isYes=True
for i in range(n//2+n%2):
    # print(cnt[-1*(i+1)],cmb(n,i))
    if cnt[-1*(i+1)]>cmb(n,i):
        isYes=False
        break
if isYes:
    print('Yes')
else:
    print('No')
