
def main():
    inputList=[] #create a empty list for input value in string
    #asking for number of items in the list
    num=int(input('Enter the no of items in list'))
    #entering items in list
    print('Enter the list')
    for i in range(num):
        #taking input from user from input function and using append()to add item in list
        inputList.append(int(input())) 
    #display the list
    print('List is:',inputList)
    #print the cumulativeList
    print('cumulative List:',cumulativeList(inputList))



def cumulativeList(inputList):
    outputList=[]
    cumulativeSum=0
    """
iterate item in inputList and them in cumulativeSum
and append it the list outputList
"""
    for i in inputList:
        cumulativeSum += i 
        outputList.append(cumulativeSum)
    return outputList #return the outputList

main()
