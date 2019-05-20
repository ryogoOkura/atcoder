h,w=map(int,input().split())
s=[]
for i in range(h):
    s.append(input())
sCnt=[[0 for _ in range(w)]for _ in range(h)]
from collections import deque
for i in range(h):
    for j in range(w):
        sij=s[i][j]
        c=0
        if sij=='#':
            c=1
            q=deque([(i,j)])
        else:
            c=-1
        if i>0:
            if s[i-1][j]!=sij:
                sCnt[i][j]+=c
        if i<h-1:
            if s[i+1][j]!=sij:
                sCnt[i][j]+=c
        if j>0:
            if s[i][j-1]!=sij:
                sCnt[i][j]+=c
        if j<w-1:
            if s[i][j+1]!=sij:
                sCnt[i][j]+=c


import numpy as np
print(np.array(sCnt))
