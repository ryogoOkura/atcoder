a,b,t=map(int,input().split())
time=a
cnt=0
while time<=t+0.5:
    time+=a
    cnt+=b

print(cnt)
