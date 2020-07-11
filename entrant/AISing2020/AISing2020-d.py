## xiのpopcount（1の数）はxのpopcount+1または-1
n=int(input())
x=input()
f={0:0,1:1,2:1,3:2}
# for i in range(2,n):
#     f[2**i]=1
# print(f)
for i in range(len(x)):
    if x[i]=='1':
        x_changed=x[:i]+'0'+x[i+1:]
    else:
        x_changed=x[:i]+'1'+x[i+1:]
    num_changed=int(x_changed,2)
    add=[]
    tmp=num_changed
    while tmp not in f:
        popcount=format(tmp,'b').count('1')
        add.append(tmp)
        tmp%=popcount
    while len(add)>0:
        cnt=f[tmp]
        tmp=add.pop()
        f[tmp]=cnt+1
    print(f[num_changed])

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
