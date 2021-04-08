'''
program to take input for nested list

variable name and explain
userInput: its input which we take from user
inputList: its the list we create from user input
nested(): its the which convert userInput to inputList
'''

#function to create nested list from user input
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

print("Enter the list with space in each element(even space before and after '[' and ']' for nested list)")
print('Example: 1 2 [ 3 [ 4 ] 5 ] 6 \n')
userInput=input('enter the list: ').split() #take input from user
inputList=nested(userInput) # call the function to create the list from user input
print('List =',inputList)#print the list user give
