import math
def main():
    n,x,t=map(int,input().split())
    ans=math.ceil(n/x)*t
    return ans

if __name__=='__main__':
    ans=main()
    print(ans)
