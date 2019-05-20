n,k=map(int,input().split())
s=input()
s_dimlist=[s[i+1]==s[i] for i in range(n-1)]
s_seqcnt=[]
if s[0]=='0':
    s_seqcnt.append(0)
pre=-1
for i in range(n-1):
    if not s_dimlist[i]:
        s_seqcnt.append(i-pre)
        pre=i
s_seqcnt.append(n-1-pre)
if s[n-1]=='0':
    s_seqcnt.append(0)
# print(s_dimlist)
# print(s_seqcnt)
width=2*k+1
length=len(s_seqcnt)
s_sum=[0 for i in range(length//2+length%2)]
s_ruiseki=[0 for i in range(length+1)]
s_ruiseki[0]=0
s_ruiseki[1]=s_seqcnt[0]
for i in range(1,length):
    s_ruiseki[i+1]=s_seqcnt[i]+s_ruiseki[i]
# print(s_ruiseki)
for i in range(length//2+length%2):
    num=0
    # # ver.1
    # for j in range(width):
    #     if 2*i+j>=length:
    #         break
    #     num+=s_seqcnt[2*i+j]
    # s_sum[i]=num
    # # ver.2
    # if 2*i+width-1>=length:
    #     s_sum[i]=sum(s_seqcnt[2*i:])
    #     break
    # else:
    #     s_sum[i]=sum(s_seqcnt[2*i:2*i+width])
    # ver.3
    if 2*i+width-1>=length:
        s_sum[i]=s_ruiseki[length]-s_ruiseki[2*i]
        break
    else:
        s_sum[i]=s_ruiseki[2*i+width]-s_ruiseki[2*i]
# print(s_sum)
print(max(s_sum))
