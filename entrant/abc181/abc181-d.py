import itertools

def main():
    s=input()
    cnt=[0 for _ in range(10)]
    for si in s:
        if cnt[int(si)]<3:
            cnt[int(si)]+=1
    likes=set()
    for i in range(0,1000,8):
        tmp=i
        likes.add(tmp)
    ans='No'
    if len(s)<3:
        if int(s)%8==0:
            ans='Yes'
        if int(s[::-1])%8==0:
            ans='Yes'
    else:
        for i in range(10):
            if cnt[i]>=1:
                for j in range(i,10):
                    if i==j and cnt[j]>=2:
                        for k in range(j,10):
                            if j==k and cnt[k]==3:
                                for a,b,c in itertools.permutations([i,j,k]):
                                    if a*100+b*10+c in likes:
                                        ans='Yes'
                                        break
                            elif j<k and cnt[k]>=1:
                                for a,b,c in itertools.permutations([i,j,k]):
                                    if a*100+b*10+c in likes:
                                        ans='Yes'
                                        break
                    elif i<j and cnt[j]>=1:
                        for k in range(j,10):
                            if j==k and cnt[k]>=2:
                                for a,b,c in itertools.permutations([i,j,k]):
                                    if a*100+b*10+c in likes:
                                        ans='Yes'
                                        break
                            elif j<k and cnt[k]>=1:
                                for a,b,c in itertools.permutations([i,j,k]):
                                    if a*100+b*10+c in likes:
                                        ans='Yes'
                                        break
    return ans

if __name__=='__main__':
    ans=main()
    print(ans)
