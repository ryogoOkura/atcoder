# 全探索してソート　TLE
# x,y,z,k=map(int,input().split())
# a=list(map(int,input().split()))
# b=list(map(int,input().split()))
# c=list(map(int,input().split()))
# beauty=[0 for _ in range(x*y*z)]
# index=0
# for i in range(x):
#     for j in range(y):
#         for l in range(z):
#             beauty[index]=a[i]+b[j]+c[l]
#             index+=1
# beauty.sort(key=lambda x:-x)
# # print(beauty)
# for i in range(k):
#     print(beauty[i])

# 優先度付きキューぽいもの　WA
# x,y,z,k=map(int,input().split())
# a=list(map(int,input().split()))
# b=list(map(int,input().split()))
# c=list(map(int,input().split()))
# a.sort(key=lambda x:-x)
# b.sort(key=lambda x:-x)
# c.sort(key=lambda x:-x)
# len=min(x*y*z,3000)
# beauty=[0 for _ in range(5000)]
# beauty[0]=a[0]+b[0]+c[0]
# index=1
# indexsum=1
# size=[x,y,z]
# while index<len:
#     imax=min(indexsum+1,x)
#     for i in range(imax):
#         jmax=min(indexsum+1-i,y)
#         for j in range(jmax):
#             if indexsum-i-j < z:
#                 num=a[i]+b[j]+c[indexsum-i-j]
#                 beauty[index]=num
#                 index+=1
#                 # print(num)
#     indexsum+=1
# beauty.sort(key=lambda x:-x)
# # print(beauty)
# for i in range(k):
#     print(beauty[i])

# # aでi番目、bでj番目、cでl番目のとき、i*j*l>kならk番目以下にはならないことを利用　AC
# x,y,z,k=map(int,input().split())
# a=list(map(int,input().split()))
# b=list(map(int,input().split()))
# c=list(map(int,input().split()))
# a.sort(key=lambda x:-x)
# b.sort(key=lambda x:-x)
# c.sort(key=lambda x:-x)
# beauty=[]
# index=0
# for i in range(x):
#     for j in range(y):
#         for l in range(z):
#             if (i+1)*(j+1)*(l+1)<=k:
#                 beauty.append(a[i]+b[j]+c[l])
#             else:
#                 break
# beauty.sort(key=lambda x:-x)
# for i in range(k):
#     print(beauty[i])

# 優先度付きキューを用いる TLE
x,y,z,k=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=list(map(int,input().split()))
a.sort(key=lambda x:-x)
b.sort(key=lambda x:-x)
c.sort(key=lambda x:-x)
# queue=[beauty, indexa, indexb, indexc]
queue=[(a[0]+b[0]+c[0],0,0,0)]
canAdd=[[[1 for _ in range(z)]for _ in range(y)]for _ in range(x)]
beauty=[0 for _ in range(k)]
for index in range(k):
    queue.sort(key=lambda x:-x[0])
    # print(queue)
    beauty[index],indexa,indexb,indexc=queue[0]
    queue.pop(0)
    for da,db,dc in [(1,0,0),(0,1,0),(0,0,1)]:
        nexta,nextb,nextc=indexa+da,indexb+db,indexc+dc
        if nexta<x and nextb<y and nextc<z and (nexta+1)*(nextb+1)*(nextc+1)<=k:
            if canAdd[nexta][nextb][nextc]:
                beau=a[nexta]+b[nextb]+c[nextc]
                # sortされた位置に挿入すれば間に合う？
                queue.append((beau,nexta,nextb,nextc))
                canAdd[nexta][nextb][nextc]=0
for i in range(k):
    print(beauty[i])
