#Program for Power set of given set

#function to findout power set
def power_set(givenSet):
    powerSet=[[]]
    #loop for subset
    for i in givenSet:
        newSubSet=[subset + [i] for subset in powerSet]
        powerSet.extend(newSubSet)
    return powerSet

#taking input for given set
print('Enter the value of set')
givenSet=[i for i in input().split()]
#print the power set
print('Power Set:\n',power_set(givenSet))