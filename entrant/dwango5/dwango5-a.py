'''
n=int(input())
tmp=list(map(int,input().split()))
a=[]
ave=0
for i in range(n):
    ave+=tmp[i]
    a.append([i,tmp[i]])

ave=ave/n # nで割ると精度が悪くなる可能性がある
a.sort(key=lambda x:(abs(ave-x[1]),x[0]))
# print(ave,a)
print(a[0][0])
'''

n=int(input())
tmp=list(map(int,input().split()))
a=[]
ave=0
for i in range(n):
    ave+=tmp[i]
    a.append([i,tmp[i]]) #a[[index,value]*n]

a.sort(key=lambda a:(abs(ave-n*a[1]),a[0]))
# print(ave,a)
print(a[0][0])
