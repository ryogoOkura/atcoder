
def main():
    n=int(input())
    ans=16*27*25*7*11*13*17*19*23*29+1
    # for i in range(2,n+1):
    #     print(ans%i)
    return ans

if __name__=='__main__':
    ans=main()
    print(ans)
