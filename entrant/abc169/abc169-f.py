def saiki(i,k,sum): # aのi番目について、kコ目のa要素、これまでの和
    if i>=n:
        return
    if sum+a[i]==s:
        times[k]+=1
    elif sum+a[i]<s:
        saiki(i+1,k+1,sum+a[i])
    saiki(i+1,k,sum)

import numpy as np
n,s=map(int,input().split())
a=list(map(int,input().split()))
a.sort(key=lambda x:-x)
# print(a)
times=[0 for _ in range(n)]
saiki(0,1,0)
# print(times)
ans=0
for i in range(n):
    ans+=times[i]*2**(n-i)
    ans%=998244353
print(ans)

# ## 参考　https://funmatu.wordpress.com/2017/09/06/%E9%85%8D%E5%88%97%E8%A6%81%E7%B4%A0%E3%81%AE%E5%90%88%E8%A8%88%E5%80%A4%E3%81%8C%E3%82%BF%E3%83%BC%E3%82%B2%E3%83%83%E3%83%88%E5%80%A4%E3%81%AB%E3%81%AA%E3%82%8B%E6%A7%98%E3%81%AA%E7%B5%84%E3%81%BF/
# import numpy as np
# n,s=map(int,input().split())
# a=list(map(int,input().split()))
# a.sort()
#
# element=[]
# for i,ai in enumerate(a):
#     tmp=[1]*(n-1-i)
#     print(i,tmp)
#     element.append(np.array([0,ai]).reshape(-1,*tmp))
# print(element)
# print('---')
# res=0
# for e in element:
#     res=res+e
#     print('--')
#     print(res)
# print('---')
# combinations=np.argwhere(res==s)
# print(combinations)
#
# ans=0
# for c in combinations:
#     addedNum=sum(c)
#     if addedNum!=0:
#         ans+=2**(n-addedNum)
# print(ans)
