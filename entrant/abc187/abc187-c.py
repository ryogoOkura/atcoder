
def main():
    n=int(input())
    s=set()
    ss=set()
    for _ in range(n):
        si=input()
        if si[0]=='!':
            ss.add(si)
        else:
            s.add(si)
    ans='satisfiable'
    for ssi in ss:
        if ssi[1]=='!':
            if ssi[1:] in ss:
                ans=ssi[1:]
                break
        else:
            if ssi[1:] in s:
                ans=ssi[1:]
                break
    return ans

if __name__=='__main__':
    ans=main()
    print(ans)
