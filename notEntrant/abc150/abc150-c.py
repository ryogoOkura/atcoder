import itertools
n=int(input())
p=list(map(int,input().split()))
q=list(map(int,input().split()))
l=[i+1 for i in range(n)]
p_num=-1
q_num=-1
for i,peri in enumerate(itertools.permutations(l,n)):
    peri=list(peri)
    if p_num==-1:
        flag=True
        for j in range(n):
            if peri[j]!=p[j]:
                flag=False
                break
        if flag:
            p_num=i
    if q_num==-1:
        flag=True
        for j in range(n):
            if peri[j]!=q[j]:
                flag=False
                break
        if flag:
            q_num=i
    if p_num!=-1 and q_num!=-1:
        break
if p_num>q_num:
    print(p_num-q_num)
else:
    print(q_num-p_num)
