import itertools

k=int(input())
s=input()
print(len(list(itertools.combinations_with_replacement(range(k+1),len(s)))))
print((26**k)*len(list(itertools.combinations_with_replacement(range(k+1),len(s)))))
