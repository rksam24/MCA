"""Program to remove duplicate value in list
eg: i/p:[1,2,1,6,4,4,6]
o/p:[1,2,6,4]
"""
def main():
    inputList=[] #create a empty list for input value in string
    #asking for number of items in the list
    num=int(input('Enter the no of items in list'))
    #entering items in list
    print('Enter the list') #print the statement
    for i in range(num): # loop to enter value in list
        #taking input from user from input function and using append()to add item in list
        inputList.append(input()) 
    #display the list before removing dupilcate
    print('List before removing duplicates values:',inputList)
    #calling removeDuplicate function
    removeDuplicate(inputList)
    #printing the list without duplicate value
    print('List without duplicate values:',removeDuplicate(inputList))
    


def removeDuplicate(inputList):
    ''' purpose: this function is desigen to remove duplicate value from
list
input:
    numbers: take list as input
    m:sum of pair
output:
    return list without duplicate values
'''
    # create a empty list for output list with no duplicate vlaues
    outputList=[]
    #iterate every item in list
    for i in inputList: #loop to remove duplicate values in list
        """checking the item of inputList if its in the ouputList then it skip the statement
and if its not in outputList then that item add in ouputlist
"""
        if i not in outputList:#check the condition
            outputList.append(i)#add item/value to outputList
    return outputList #return the output list

main()
