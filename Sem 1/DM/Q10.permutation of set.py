#program to find put permutation of given set

givenSet=[i for i in input('Enter element of set \n').split()]

#function to permutation of given set
def permuatation(givenSet):
    if len(givenSet)==1: #when thier is only 1 element
        return [givenSet] #only 1 permutation possible so return it
    #permuatation for n-1 element
    perms=permuatation(givenSet[1:])
    felemnt=givenSet[0] #first element of set
    resultSet=[] #list which will contain all permuation
    for perm in perms: #loop for get all permuatioin
        for i in range(len(perm)+1):
            resultSet.append(perm[:i]+[felemnt]+perm[i:])
    return resultSet #return the all permuation
print('\nPermutation of set: ')
#loop for print all permutation
for perm in permuatation(givenSet):
    print(perm)