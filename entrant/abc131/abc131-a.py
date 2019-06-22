s=input()
pre=' '
isBad=False
for si in s:
    if si==pre:
        isBad=True
    pre=si
if isBad:
    print('Bad')
else:
    print('Good')
