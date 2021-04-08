#program for shallow copy of list

#function to copy original list into copy list(to make shallow copy)
def copy1(originalList,copyList=list()):
    if originalList==[]: #when list is empty return the copy list
        return copyList
    else:
        copyList.append(originalList[0])#add value from original list to copy list
        return copy1(originalList[1:],copyList) #call the function again to copy remain element
        

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


#main body of program. Execution of program start from here
def main():
    print("Enter the list with space in each element(even space before and after '[' and ']' for nested list)")
    print('Example: 1 2 [ 3 [ 4 ] 5 ] 6 \n')
    userInput=input('enter the list: ').split() #take input from user
    originalList=nested(userInput) # call the function to create the list from user input
    
    copyList=copy1(originalList)#call the function to copy list

    print('List2=',copyList)#print copy list after copy original list
    
    #to check shallow copy work
    ind=int(input('\nEnter the index of nested list for change its first element: '))#ask index of nested list from user to change
    if (ind>len(originalList)-1) or (type(originalList[ind]) is not list) : #checking if at that index element is list or not and user index is not out bound
        print('Invalid index for nested list') #print this statement if enter index is not list  
    else:
        originalList[ind][0]=input('\n enter the element ') #changing the element
    
    print('\nAfter change the list1')
    print('List1=',originalList) #print original list after make change
    print('List2',copyList)#print copy list after make change in original list to check its shallow copy or not
    
main()
