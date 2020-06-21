n=int(input())
digit=0
for i in range(1,12):
    tmp=26**i
    if n<=tmp:
        digit=i
        break
    else:
        n-=tmp
# print(digit,n)
n-=1
ans=[]
for i in range(digit-1,-1,-1):
    tmp=26**i
    # print(n,tmp,n//tmp,n%tmp)
    ans.append(n//tmp)
    n%=tmp
# print(ans)
for ai in ans:
    print(chr(ai+97),end='')
