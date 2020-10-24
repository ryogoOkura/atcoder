import random

def main():
    n=13
    all=set([i for i in range(26)])
    s=['' for _ in range(n)]
    check=[set() for _ in range(26)] # check[i] = chr(i)から始まる文字のうち使われているもの
    s[0]+='a'
    for wi in range(1,n):
        s[0]+=chr(ord('a')+wi)
        check[wi-1].add(wi)
    for hi in range(1,n):
        up=s[hi-1][0]
        up=ord(up)-ord('a')
        left=random.choice(list(all-check[up]))
        check[up].add(left)
        s[hi]+=chr(ord('a')+left)
        for wi in range(1,n):
            up=s[hi-1][wi]
            up=ord(up)-ord('a')
            if all-(check[up]|check[left])==set():
                print(hi,wi)
                return
            now=random.choice(list(all-(check[up]|check[left])))
            s[hi]+=chr(ord('a')+now)
            check[up].add(now)
            check[left].add(now)
            left=now
    for si in s:
        print(si)

    ## check
    check=[[0 for _ in range(26)] for _ in range(26)]
    for i in range(n-1):
        for j in range(n-1):
            now,r,d=s[i][j],s[i][j+1],s[i+1][j]
            now,r,d=ord(now)-ord('a'),ord(r)-ord('a'),ord(d)-ord('a')
            check[now][r]+=1
            check[now][d]+=1
            if check[now][r]>1 or check[now][d]>1:
                print(i,j)
    return

# def main():
#     n=5
#     print(n)
#     print('abcde')
#     print('fghij')
#     print('klmno')
#     print('pqrst')
#     print('uvwxy')
#     return

def main():
    n=13
    print(n)
    print('abcdefghijklm')
    print('iwhnewkxlwbqw')
    print('ksswtlofxmfvw')
    print('mjqjvhvnvrkio')
    print('psmhfcszgbgeg')
    print('lcmyuepusyxdm')
    print('sinatmcntorsu')
    print('vmonpbjmqcleo')
    print('adyngnyerwgje')
    print('upkurxsxpzidl')
    print('cpnffhawiyzaf')
    print('criiaqycumvjt')
    print('zcxqxarqzsbif')


if __name__=='__main__':
    main()
