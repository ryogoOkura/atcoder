
def main():
    sx,sy,gx,gy=map(int,input().split())
    ans=sx+sy*(gx-sx)/(gy+sy)
    return ans

if __name__=='__main__':
    ans=main()
    print(ans)
