'''
program for 
a.Identity laws
b. Domination laws
c. Double negation laws
'''
#taking p from user
print('Enter p in 1 0 form with space')
p=[bool(int(i)) for i in input().split()]

#checking Identity law
print('\nIdentity Law')
print('1. p ^ T = p')
print('\tp \t T\t p ^ T')
#loop for Identity law
for i in p:
    print('\t',i,'\t',True,'\t',i & True)
print('2. p V F = p')
print('\tp \t F\t p V F')
#loop for identity law
for i in p:
    print('\t',i,'\t',False,'\t',i | False)

#checking for domination law
print('\nDomination law')
print('1. p V T = T')
print('\t p\t T\t p V T')
#loop for domination law
for i in p:
    print('\t',i,'\t',True,'\t',i | True)
print('2. p ^ F = F')
print('\t p\t F\t p ^ F')
#loop for domination law
for i in p:
    print('\t',i,'\t',False,'\t',i & False)

#checking for Double negation law
print('\nDouble negation laws')
print('~(~p) = p')
print('\t p\t ~(~p)')
#loop for double negation law
for i in p:
    print('\t',i,'\t', (not (not i)))
