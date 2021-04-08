''' 
Program to count number of elements in string
conditioin: use recursion
'''
#function to findout the length of string
def length(string):
    if string=='': #when list is empty return 0
        return 0
    else:
        #return the length and within return, function is call with string start with second character 
        return 1+length(string[1:]) 
        
#execution of program start from here
def main():
    string=input('Enter the string :') #taking string as input
    print('length of ',string,'=', length(string)) #call function to call to get length of string

main()
