x,n=map(int,input().split())
p=list(map(int,input().split()))
p.sort()
if n==0:
    print(x)
else:
    if x in p:
        i=1
        while True:
            if not x-i in p:
                print(x-i)
                break
            if not x+i in p:
                print(x+i)
                break
            i+=1
    else:
        print(x)
