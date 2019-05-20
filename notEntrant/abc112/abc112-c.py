# できなかった
n=int(input())
data=[] # data[[x1,y1,h1],...,[xn,yn,hn]]
for i in range(n):
    (xi,yi,hi)=map(int, input().split())
    data.append([xi,yi,hi])

data.sort(key=lambda x:x[2])
data.reverse()

breakflg=False
for cx in range(101):
    if(breakflg):
        break
    for cy in range(101):
        h=abs(data[0][0]-cx)+abs(data[0][1]-cy)+data[0][2]
        flag=True
        for i in range(n):
            h_est=h-abs(data[i][0]-cx)-abs(data[i][1]-cy)
            if(h_est<0):
                h_est=0
            if(data[i][2]!=h_est):
                flag=False
                break
        if(flag):
            print(cx,cy,h)
            breakflg=True;
