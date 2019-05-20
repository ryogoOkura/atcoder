n,x=map(int,input().split())

thickness=[1]
patty=[1]
for i in range(1,n):
    thickness.append(2*thickness[i-1]+3)
    patty.append(2*patty[i-1]+1)

def pattyCnt(n,x):
    if n==0:
        return 0 if x<=0 else 1
    elif x<=1+thickness[n-1]:
        return pattyCnt(n-1,x-1)
    else:
        return patty[n-1]+1+pattyCnt(n-1,x-2-thickness[n-1])

print(pattyCnt(n,x))


# def makeBurger(n):
#     if n==1:
#         return [1,3,1]
#     else:
#         burger=makeBurger(n-1)
#         newBurger=[*burger,1,*burger]
#         newBurger[0]+=1
#         newBurger[-1]+=1
#         return newBurger
# burger=makeBurger(n)
# size=0
# index=0
# cnt=0
# while size<=x:
#     layerSize=burger[index]
#     if index%2:
#         if size+layerSize>x:
#             cnt+=x-size
#             break
#         else:
#             cnt+=layerSize
#     size+=layerSize
#     index+=1
# print(cnt)

# def makeBurger(n):
#     if n==1:
#         return 'bpppb'
#     else:
#         burger=makeBurger(n-1)
#         return 'b'+burger+'p'+burger+'b'
#
# burger=makeBurger(n)
# cnt=0
# for i in range(x):
#     if burger[i]=='p':
#         cnt+=1
# print(cnt)

# burger='bpppb'
# for i in range(1,n):
#     burger='b'+burger+'p'+burger+'b'
#
# cnt=0
# for i in range(x):
#     if burger[i]=='p':
#         cnt+=1
# print(cnt)

#'''
