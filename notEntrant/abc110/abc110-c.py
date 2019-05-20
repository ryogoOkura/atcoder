'''
問題文
英小文字のみからなる文字列 S,T が与えられます。
文字列 S に対して、次の操作を何度でも行うことができます。

操作: 2つの異なる英小文字 c1, c2 を選び、S に含まれる全ての c1 を c2 に、c2 を c1 に置き換える

0 回以上操作を行って、S を T に一致させられるか判定してください。

制約
1≤|S|≤2×10^5
|S|=|T|S,
T は英小文字のみからなる
'''
import numpy as np

s=input()
t=input()
s_cnt=np.zeros(26)
s_letterPlace=[[] for _ in range(26)]
for i,si in enumerate(s):
    num=ord(si)-ord('a')
    s_cnt[num]+=1
    s_letterPlace[num].append(i)

s_multiLetter=[]
for cnt,place in zip(s_cnt,s_letterPlace):
    if cnt>1:
        s_multiLetter.append(place)

t_cnt=np.zeros(26)
t_letterPlace=[[] for _ in range(26)]
for i,ti in enumerate(t):
    num=ord(ti)-ord('a')
    t_cnt[num]+=1
    t_letterPlace[num].append(i)

t_multiLetter=[]
for cnt,place in zip(t_cnt,t_letterPlace):
    if cnt>1:
        t_multiLetter.append(place)
# print(len(s_multiLetter))
# print(len(t_multiLetter))

flag=1
if len(s_multiLetter)!=len(t_multiLetter):
    flag=0
elif len(s_multiLetter)==0 & len(t_multiLetter)==0:
    flag=1
elif len(s_multiLetter)*len(t_multiLetter)==0:
    flag=0
else:
    for s_place in s_multiLetter:
        if(flag==1):
            for t_place in t_multiLetter:
                if(s_place==t_place):
                    flag=1
                    break
                else:
                    flag=0

print('Yes' if flag==1 else 'No')
#'''
