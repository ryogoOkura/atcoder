a,b,k=map(int,input().split())
ao=[]
for i in range(a,0,-1):
    if a%i==0:
        ao.append(i)
bo=[]
for i in range(b,0,-1):
    if b%i==0:
        bo.append(i)
# print(ao,bo)
i,j,n=0,0,0
ans=0
while n<k:
    if ao[i]==bo[j]:
        n+=1
        ans=ao[i]
        i+=1
    elif ao[i]>bo[j]:
        i+=1
    else:
        j+=1
print(ans)
