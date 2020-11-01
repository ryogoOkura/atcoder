
def main():
    n=int(input())
    ans='White' if n%2==0 else 'Black'
    return ans

if __name__=='__main__':
    ans=main()
    print(ans)
