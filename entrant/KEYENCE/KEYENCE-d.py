n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))

aIndexed=list(enumerate(a))
aIndexed.sort(key=lambda x:x[1])
aIndexed.reverse()
bIndexed=list(enumerate(b))
bIndexed.sort(key=lambda x:x[1])
bIndexed.reverse()

import numpy as np
map=np.zeros(n*m).reshape((n,m))
for i in range(n*m,0,-1):
    print(i)
print(aIndexed)
print(map)
