# できなかった
# 最大値から負の数をすべ引いたもの　から　最小値から正の数をすべて引いたもの　を引く
n=int(input())
a=list(map(int,input().split()))
a.sort()
min=a[0]
max=a[-1]
ans=[]
for a in a[1:-1]:
    if a>0:
        ans.append([min,a])
        min-=a
    else:
        ans.append([max,a])
        max-=a
ans.append([max,min])
print(max-min)
for x,y in ans:
    print(x,y)

# n=int(input())
# a=list(map(int,input().split()))
# ans=[]
# for i in range(n-1):
#     a.sort()
#     num=a.pop()
#     num2=a.pop(0)
#     if i%2:
#         ans.append((num,num2))
#         a.append(num-num2)
#     else:
#         ans.append((num2,num))
#         a.append(num2-num)
# print(a[0])
# for num,num2 in ans:
#     print(num,num2)
