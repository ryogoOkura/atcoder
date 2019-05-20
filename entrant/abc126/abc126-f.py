m,k=map(int,input().split())
if m==0:
    if k==0:
        print('0 0')
    else:
        print(-1)
elif m==1:
    if k==0:
        print('0 0 1 1')
    else:
        print(-1)
else:
    if k>=2**m:
        print(-1)
    else:
        print(k,end=' ')
        for i in range(2**m):
            if i!=k:
                print(i,end=' ')
        print(k,end=' ')
        for i in range(2**m-1,-1,-1):
            if i!=k:
                print(i,end=' ')


# m,k=map(int,input().split())
# if k==0:
#     for i in range(2**(m+1)):
#         print(i//2,end=' ')
#     # a=[i//2 for i in range(2**(m+1))]
# elif k<4 and (m+1)%4==0:
#     print(k,end=' ')
#     for i in range(2**m):
#         if i!=k:
#             print(i,end=' ')
#     print(k,end=' ')
#     for i in range(2**m-1,-1,-1):
#         if i!=k:
#             print(i,end=' ')
# else:
#     print(-1)
