a=[int(input()) for _ in range(5)]
ar=[[i,a[i]%10] for i in range(5)]
ar.sort(key=lambda x:x[1])
i=0
while ar[i][1]==0:
    i+=1
    if i==4:
        break
k=ar[i][0]
time=0
for i in range(5):
    if i!=k:
        time+=a[i]
        if a[i]%10!=0:
            time+=10-a[i]%10
time+=a[k]
print(time)
