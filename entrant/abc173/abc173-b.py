n=int(input())
s=[input() for _ in range(n)]
ans={'AC':0,'WA':0,'TLE':0,'RE':0}
for si in s:
    ans[si]+=1
# print(ans)
for key in ans:
    print(f'{key} x {ans[key]}')
