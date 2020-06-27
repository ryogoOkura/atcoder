s=input()
t=input()
len_s=len(s)
ans=0
for i in range(len_s):
    if s[i]!=t[i]:
        ans+=1
print(ans)
