'''
Program for
a. Demorgan’s laws
b. Associative laws
'''
#taking value of p,q and r from user
print('Enter p in 1 0 form with space')
p=[bool(int(i)) for i in input().split()]
print('Enter q in 1 0 form with space')
q=[bool(int(i)) for i in input().split()]
print('Enter r in 1 0 form with space')
r=[bool(int(i)) for i in input().split()]

#checking Demorgan's law
print('\nDemorgan’s laws')
print('1. ~(p ^ q) = ~p V ~q')
print('\t p\t q\t ~(p ^ q) \t ~p V ~q')
#loop for demorgan's law
for i in range(len(p)):
    print('\t',p[i],'\t',q[i],'\t',not ( p[i] &  q[i] ),end='' )
    print('\t\t', ( not p[i] ) | ( not q[i] ) )

print('\n2. ~(p V q) = ~p ^ ~q')
print('\t p\t q\t ~(p V q) \t ~p ^ ~q')
#loop for demorgan's law
for i in range(len(p)):
    print('\t',p[i],'\t',q[i],'\t',not ( p[i] or  q[i] ),end='' )
    print('\t\t', (not p[i] ) & ( not q[i] ) )

#checking Associative laws
print('\nAssociative laws')
print('1.(p ^ q) ^ r = p ^ (q ^ r)')
print('\t p\t q\t r\t (p ^ q) ^ r\t p ^ (q ^ r)')
#loop for Associative law
for i in range(len(p)):
    print('\t',p[i],'\t',q[i],'\t',r[i],'\t',( p[i] & q[i] ) & r[i],end='' )
    print('\t\t',p[i] & ( q[i] & r[i] ) )
print('\n2.(p V q) V r = p V (q V r)')
print('\t p\t q\t r\t (p V q) V r\t p V (q V r)')
#loop for Associative law
for i in range(len(p)):
    print('\t',p[i],'\t',q[i],'\t',r[i],'\t',( p[i] | q[i] ) | r[i],end='' )
    print('\t\t',p[i] | ( q[i] | r[i] ) )