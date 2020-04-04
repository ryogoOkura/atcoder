k=int(input())
# num から始まる digit 桁（num 含む）のルンルン数の個数を返す
def count(digit,num):
    if digit==1:
        return 1
    c=0
    if num!=0:
        c+=count(digit-1,num-1)
    c+=count(digit-1,num)
    if num!=9:
        c+=count(digit-1,num+1)
    return c

# num から始まる digit 桁（num 含む）のルンルン数の中で i 番目の ans を返す
def answer(digit,num,i,ans):
    # print(digit,num,i,ans)
    if digit==2:
        add=(i+num-2)
        if num==0:
            add+=1
        return ans*10+add
    if num!=0:
        c=count(digit-1,num-1)
        if c>=i:
            return answer(digit-1,num-1,i,ans*10+num-1)
        i-=c
    c=count(digit-1,num)
    if c>=i:
        return answer(digit-1,num,i,ans*10+num)
    i-=c
    if num!=9:
        c=count(digit-1,num+1)
        if c>=i:
            return answer(digit-1,num+1,i,ans*10+num+1)
    return 0

size=9
num=1
digit=2
while True:
    s=count(digit,num)
    if s+size>=k:
        break
    size+=s
    num+=1
    if num==10:
        num=1
        digit+=1
ans=0
if k<=9:
    ans=k
else:
    ans=answer(digit,num,k-size,num)
print(ans)
