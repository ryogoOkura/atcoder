## (x+y)^2+(y+z)^2+(z+x)^2==2n
## 3この平方数の和
n=int(input())
dict={}
i,j,k=1,1,1
while (i+j)**2+(j+k)**2+(k+i)**2<=2*n:
    while (i+j)**2+(j+k)**2+(k+i)**2<=2*n:
        # print('\t',i,j,k)
        while (i+j)**2+(j+k)**2+(k+i)**2<=2*n:
            tmp=(i+j)**2+(j+k)**2+(k+i)**2
            tmp//=2
            if tmp not in dict:
                dict[tmp]=0
            dict[tmp]+=1
            # print(i,j,k)
            k+=1
        k=1
        j+=1
    j=1
    i+=1
# print(dict)
for i in range(1,n+1):
    if i in dict:
        print(dict[i])
    else:
        print(0)









# n=int(input())
# for i in range(n):
#     tmp=i
#     while tmp%4==0:
#         tmp=tmp//4
#     if tmp%8!=7:
#
