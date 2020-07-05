n,k=map(int,input().split())
a=list(map(int,input().split()))
p=10**9+7
a_plus=[]
a_minus=[]
for ai in a:
    if ai<0:
        a_minus.append(ai)
    else:
        a_plus.append(ai)
if k-len(a_plus)>0 and (k-len(a_plus))%2==1: # ans<0
    a_plus.sort()
    a_minus.sort(reverse=True)
else:
    a_plus.sort(reverse=True)
    a_minus.sort()
# print(a_plus,a_minus)
cnt=k
ans=1
while cnt>=2 and len(a_plus)>=2 and len(a_minus)>=2:
    tmp_p=a_plus[0]*a_plus[1]
    tmp_m=a_minus[0]*a_minus[1]
    if tmp_p>tmp_m:
        ans=(ans*tmp_p)%p
        a_plus=a_plus[2:]
    else:
        ans=(ans*tmp_m)%p
        a_minus=a_minus[2:]
    cnt-=2
while cnt>=2 and len(a_plus)>=2:
    tmp_p=a_plus[0]*a_plus[1]
    ans=(ans*tmp_p)%p
    a_plus=a_plus[2:]
    cnt-=2
while cnt%2==1 and len(a_plus)>=1:
    ans=(ans*a_plus[0])%p
    a_plus=a_plus[1:]
    cnt-=1
while cnt>=2 and len(a_minus)>=2:
    tmp_m=a_minus[0]*a_minus[1]
    ans=(ans*tmp_m)%p
    a_minus=a_minus[2:]
    cnt-=2
if cnt>0:
    ans=(ans*a_minus[0])%p
    cnt-=1
print(ans)
