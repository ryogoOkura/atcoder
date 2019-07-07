n,k=map(int,input().split())
ab=[tuple(map(int,input().split())) for i in range(n-1)]
print(ab)
next=[[] for i in range(n)]
for ai,bi in ab:
    ai,bi=ai-1,bi-1
    next[ai].append(bi)
    next[bi].append(ai)
print(next)
