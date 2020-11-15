import itertools

def main():
    n,k=map(int,input().split())
    t=[list(map(int,input().split())) for _ in range(n)]
    perm=itertools.permutations([i for i in range(1,n)])
    ans=[]
    for permi in perm:
        tmp=0
        now=0
        for j in permi:
            tmp+=t[now][j]
            now=j
        tmp+=t[now][0]
        # print(permi,tmp)
        ans.append(tmp)
    return ans.count(k)

if __name__=='__main__':
    ans=main()
    print(ans)
