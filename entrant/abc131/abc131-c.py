def gcd(a, b):
	while b:
		a, b = b, a % b
	return a
a,b,c,d=map(int,input().split())
a-=1
bIka=b-b//c-b//d+b//(c*d//gcd(c,d))
aMiman=a-a//c-a//d+a//(c*d//gcd(c,d))
print(bIka-aMiman)

# a,b,c,d=map(int,input().split())
# cnt=0
# for i in range(a,b+1):
#     if i%c!=0 and i%d!=0:
#         cnt+=1
#         print(i)
# print(cnt)
