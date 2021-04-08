#program to implement Modus ponens and Modus Tollens

#taking p and q from user
p=[bool(int(i)) for i in input('Enter the p in 1 0 form: ').split()]
q=[bool(int(i)) for i in input('Enter the q in 1 0 form: ').split()]

#for Modus Ponens
print('\n\t\tModus Ponens\n')
print('\t p\t q\t p implies q\t (p implies q) ^ p')
for i in range(len(p)):
    implies=( (not p[i]) or q[i] )
    print('\t',p[i],'\t',q[i],'\t',implies,'\t\t', implies & p[i])

#Modus Tollens
print('\n\n\t\tModus Tollens\n')
print('\t p\t q\t p implies q\t ~q\t (p implies q) ^ ~q')
for i in range(len(p)):
    implies=( (not p[i]) or q[i] )
    print('\t',p[i],'\t',q[i],'\t',implies,'\t\t',not q[i],'\t\t', implies & ( not q[i] ) )
    