## 15とかも３＊３＋３＊２になるのでできる
def main():
    n=int(input())
    if n==2:
        ans='impossible'
        print(ans)
        return
    if n%2==0:
        print(n//2)
        for i in range(n//2):
            ans=[2,2*i+1,2*(n-i)-1]
            print(*ans)
        return
    sq=-1
    for i in range(3,315,2): # 二乗が含まれるかどうか
        if n%(i**2)==0:
            sq=i
            break
    if sq==-1:
        print('impossible')
        return
    size=n//(sq**2) # sq個ごとのセットの数
    print(sq)
    ans=[sq*size for _ in range(sq*size+1)]
    add=[2*i+1 for i in range(sq)]
    for i in range(sq):
        for j in range(sq*size):
            ans[j+1]=2*j*sq+add[(i+j)%(sq)]
        print(*ans)
        # print(sum(ans))
    return

if __name__=='__main__':
    main()
