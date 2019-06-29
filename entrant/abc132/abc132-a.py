s=input()
chr={s[0]:1}
for si in s[1:]:
    if si in chr:
        chr[si]+=1
    else:
        chr[si]=1
# print(chr)
if len(chr)==2 and 2 in chr.values():
    print('Yes')
else:
    print('No')
