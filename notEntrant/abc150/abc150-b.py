n=int(input())
s=input()
flag=0
ans=0
for si in s:
    if si=='A':
        flag=1
    elif si=='B' and flag==1:
        flag=2
    elif si=='C' and flag==2:
        ans+=1
        flag=0
    else:
        flag=0
print(ans)
