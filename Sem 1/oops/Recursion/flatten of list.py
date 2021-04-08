'''
function to flatten the list
i/p: [1,[2,3],4]
o/p: [1,2,3,4]
'''
def flatten(lists,outputlist=list()):
    #loop to add value to input list to output list to make it one dimensional list 
    for i in lists: 
        if type(i) is list:#when the element of list is a list function call again
            flatten(i)
        else:
           outputlist.append(i) # add value to output list
    return outputlist# return output list

#function to create nested list from user
def nested(userInput,inputList=list()):
    if userInput==[]:#check if input list is empty return the desire list
        return inputList
    elif userInput[0]==']': # check if first element of input list is  ] 
        userInput.pop(0) #remove first element from input list
        return inputList #return the desire list
    elif userInput[0]=='[': # check if first element of list is [
        userInput.pop(0) #remove first element from input list
        #call the function for nested list
        inputList.append(nested(userInput,inputList=list()))
        #call the function to add the element to outer list again  then return it
        return nested(userInput,inputList)
    else:
        inputList.append(userInput[0]) #add the element to list 
        userInput.pop(0)#remove first element from input list
        #call the function to add remaining element  then return it
        return nested(userInput,inputList)

#execution of program start from here
def main():
    print("Enter the list with space in each element(even space before and after '[' and ']' for nested list)")
    print('Example: 1 2 [ 3 [ 4 ] 5 ] 6 \n')
    userInput=input('Enter the list: ').split() #take input from user
    inputList=nested(userInput) # call the function to create the list from user input
    print('Before flatten list are:')
    print('List =',inputList)# print list befor flatten
    print('\nAfter flatten list are:')
    print('List=',flatten(inputList))#print list after flatten

main()