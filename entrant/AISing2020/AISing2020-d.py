## 最初のmodをどうにか高速にやりたい → modの性質を使う
## xiのpopcount（1の数）はxのpopcount+1または-1
n=int(input())
x_str=input()
x_popcount=x_str.count('1')
dp=[0]*(x_popcount+1)
for i in range(1,x_popcount+1):
    popcount=format(i,'b').count('1')
    dp[i]=dp[i%popcount]+1
# print(dp)
# x=int(x_str,2)
if x_popcount>1:
    pows_minus=[pow(2,i,(x_popcount-1)) for i in range(n)]
    # x_minus=x%(x_popcount-1)
    x_minus=0
    for i in range(n):
        if x_str[i]=='1':
            x_minus+=pows_minus[n-1-i]
pows_plus=[pow(2,i,(x_popcount+1)) for i in range(n)]
# x_plus=x%(x_popcount+1)
x_plus=0
for i in range(n):
    if x_str[i]=='1':
        x_plus+=pows_plus[n-1-i]

for i in range(len(x_str)):
    ## xi=xi mod popcount(x)+-1
    xi=-1
    if x_str[i]=='1':
        if x_popcount>1: ## else: xi=-1
            xi=(x_minus-pows_minus[n-1-i])%(x_popcount-1)
    else:
        xi=(x_plus+pows_plus[n-1-i])%(x_popcount+1)
    if xi==-1:
        print(0)
    else:
        print(dp[xi]+1)


## TLE 考えてみたら下のやつと同じオーダーだった
# n=int(input())
# x=input()
# max_popcount=format(x,'b').count('1')+1
# f=[0]*n
# for i in range(1,max_popcount):
#     popcount=format(i,'b').count('1')
#     f[i]=f[i%popcount]+1
# # print(f)
# for i in range(len(x)):
#     if x[i]=='1':
#         x_changed=x[:i]+'0'+x[i+1:]
#     else:
#         x_changed=x[:i]+'1'+x[i+1:]
#     num_changed=int(x_changed,2)
#     # print(x_changed,num_changed)
#     popcount=format(num_changed,'b').count('1')
#     if num_changed<max_popcount:
#         print(f[num_changed])
#     else:
#         print(f[num_changed%popcount]+1)

## TLE
# n=int(input())
# x=input()
# f={0:0,1:1,2:1,3:2}
# # print(f)
# for i in range(len(x)):
#     if x[i]=='1':
#         x_changed=x[:i]+'0'+x[i+1:]
#     else:
#         x_changed=x[:i]+'1'+x[i+1:]
#     num_changed=int(x_changed,2)
#     add=[]
#     tmp=num_changed
#     while tmp not in f:
#         popcount=format(tmp,'b').count('1')
#         add.append(tmp)
#         tmp%=popcount
#     while len(add)>0:
#         cnt=f[tmp]
#         tmp=add.pop()
#         f[tmp]=cnt+1
#     print(f[num_changed])
