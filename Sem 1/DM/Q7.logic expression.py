#Program to implement ¬∀x P(x)  ≡ ∃x ¬P(x)
print('Enter P(x) s in 1 0 form with space')
x=[bool(int(i)) for i in input().split()]
#print p(x)
for i in range(len(x)):
    print('P(',i,') =',x[i])

#checking for ¬(∀xP(x)) ≡ ∃x(¬P(x))
print('\nTo Prove ¬∀x P(x) ≡ ∃x ¬P(x)')
print('\nLHS : \n ¬∀x P(x) = ¬(P(0)^P(1)^P(2)...)')

#evaluate LHS
LHS=x[0]
for i in range(1,len(x)):
    LHS = LHS & x[i]
print('¬∀x P(x)=', (not LHS) )

#evaluate RHS
print('\nRHS : \n ∃x ¬P(x) = (¬P(0)) V (¬P(1)) V (¬P(2))...)')
RHS=not x[0]
for i in range(1,len(x)):
    RHS = RHS | (not x[i])
print('∃x ¬P(x) =',RHS)