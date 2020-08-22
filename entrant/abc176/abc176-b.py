def main():
    n=input()
    sum=0
    for ni in n:
        sum+=int(ni)
    # print(sum)
    if sum%9==0:
        ans='Yes'
    else:
        ans='No'
    return ans

if __name__=='__main__':
    ans=main()
    print(ans)
