s=input()
lhs=int(s[0])*10+int(s[1])
rhs=int(s[2])*10+int(s[3])
# print(lhs,rhs)
isLeftOK=(0<lhs<=12)
isRightOK=(0<rhs<=12)
if isLeftOK and isRightOK:
    print('AMBIGUOUS')
elif isLeftOK:
    print('MMYY')
elif isRightOK:
    print('YYMM')
else:
    print('NA')
