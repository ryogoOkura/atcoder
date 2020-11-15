class Bit:
    def __init__(self, n):
        self.size = n
        self.tree = [0] * (n + 1)

    def sum(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s

    def add(self, i, x):
        while i <= self.size:
            self.tree[i] += x
            i += i & -i

class RangeUpdate:
    def __init__(self, n):
        self.p = Bit(n + 1)
        self.q = Bit(n + 1)

    def add(self, s, t, x):
        t += 1
        self.p.add(s, -x * s)
        self.p.add(t, x * t)
        self.q.add(s, x)
        self.q.add(t, -x)

    def sum(self, s, t):
        t += 1
        return self.p.sum(t) + self.q.sum(t)*t - self.p.sum(s) - self.q.sum(s)*s

def main2(): # こっちのが遅い？
    n,w=map(int,input().split())
    stp=[list(map(int,input().split())) for _ in range(n)]
    maxT=sorted(stp,key=lambda x:-x[1])[0][1]
    bit=RangeUpdate(maxT)
    for i in range(n):
        si,ti,pi=stp[i]
        bit.add(si,ti-1,pi)
    ans='Yes'
    for i in range(maxT):
        tmp=bit.sum(i,i)
        if tmp>w:
            ans='No'
            break

def main1(): #TLE
    n,w=map(int,input().split())
    stp=[list(map(int,input().split())) for _ in range(n)]
    maxT=sorted(stp,key=lambda x:-x[1])[0][1]
    use=[0 for _ in range(maxT)]
    for i in range(n):
        si,ti,pi=stp[i]
        for j in range(si,ti):
            use[j]+=pi
            if use[j]>w:
                use[j]=w+1
    # print(use)
    ans='Yes'
    if w+1 in set(use):
        ans='No'
    return ans

def main(): # いもす法
    n,w=map(int,input().split())
    stp=[list(map(int,input().split())) for _ in range(n)]
    maxT=sorted(stp,key=lambda x:-x[1])[0][1]
    use=[0 for _ in range(maxT+1)]
    for i in range(n):
        si,ti,pi=stp[i]
        use[si]+=pi
        use[ti]-=pi
    for i in range(1,maxT+1):
        use[i]+=use[i-1]
    ans='Yes'
    for i in range(maxT+1):
        if use[i]>w:
            ans='No'
            break
    return ans

if __name__=='__main__':
    ans=main()
    print(ans)
