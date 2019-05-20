s=input()
length=len(s)
s_list=[int(s[i]) for i in range(length)]
s_dimlist=[s[i+1]==s[i] for i in range(length-1)]
# print(s_dimlist)
pre=0
isDone=True
cnt=0
for i in range(length-1):
    if s_dimlist[i]:
        if isDone:
            pre=i
            isDone=False
        else:
            cnt+=i-pre
            isDone=True
if not isDone:
    cnt+=length-1-pre
    # print(pre,length)
print(cnt)
