#program for tautology,Contradication and Contingency

print('Enter p in 1 0 form with space')
p=[bool(int(i)) for i in input().split()]
print('Enter q in 1 0 form with space')
q=[bool(int(i)) for i in input().split()]

#for tauology
print("\nToutology for p")
print('\t p\t ~p\t p V ~p')
#loop fro tauology
for i in p:
    print('\t',i,'\t',bool(~i),'\t',i | (not i))

#for Contradiction
print('\nContradiction for p')
print('\t p\t ~p\t p ^ ~p')
#loop for contradication
for i in p:
    print('\t',i,'\t',not i,'\t',i & (not i))

#for contingency
print('\nContingency')
print('\t p\t q\t p V q')
#loop for contingency
for i in range(len(p)):
    print('\t',p[i],'\t',q[i],'\t',p[i] | q[i])