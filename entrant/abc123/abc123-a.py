a=[int(input()) for i in range(5)]
k=int(input())
flag=1
for i in range(5):
    for j in range(i+1,5):
        if a[j]-a[i]>k:
            flag=0
            break
if flag:
    print('Yay!')
else:
    print(':(')
