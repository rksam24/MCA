#program for Deepcopy of list

#function to copy original list into copy list(to make deep copy)
def copy1(originalList,copyList=list()):
    if originalList==[]:#when list is empty return the copy list
        return copyList
    elif type(originalList[0]) is list:
        copyList.append(copy1(originalList[0],copyList=list()))
        return copy1(originalList[1:],copyList)
    else:
        copyList.append(originalList[0])#add value from original list to copy list
        return copy1(originalList[1:],copyList)#call the function again to copy remain element


#function to create list from user input
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

#program execution start from here
def main():
    print("Enter the list with space in each element(even space before and after '[' and ']' for nested list)")
    print('Example: 1 2 [ 3 [ 4 ] 5 ] 6 \n')
    userInput=input('enter the list: ').split() #take input from user
    originalList=nested(userInput) # call the function to create the list from user input
    print('List =',originalList)#print the list user give

    #call the function to copy list
    copyList=copy1(originalList)
    #print copy list after copy original list
    print('copyList=',copyList)

    #to check deepcopy work
    ind=int(input('\nEnter the index of nested list for change its element: '))#ask index of nested list from user to change
    if (ind>len(originalList)-1) or (type(originalList[ind]) is not list) : #checking if at that index element is list or not and user index is not out bound
        print('Invalid index for nested list') #print this statement if enter index is not list  
    else:
        originalList[ind][0]=input('\n enter the element ') #changing the element
    
    print('\nAfter change the originalList')
    print('originalList=',originalList)#print original list after make change
    print('copyList',copyList)#print copy list after make change in original list to check its shallow copy or not
    
main()
