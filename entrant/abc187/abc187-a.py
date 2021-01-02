
def main():
    a,b=map(int,input().split())
    s_a=a%10+(a//10)%10+a//100
    s_b=b%10+(b//10)%10+b//100
    # print(s_a,s_b)
    ans=s_b
    if s_a>=s_b:
        ans=s_a
    return ans

if __name__=='__main__':
    ans=main()
    print(ans)
