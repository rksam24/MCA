'''
Program to check wheter a given string is palindrome or not
condition: using recursion
'''
        
#function to check if string is palindrome or not
def palindrome(string):
    if string=='':# if string is not empty then it return true
        return True
    #check if first and last character is same if its same
    #then fuction call for second and last second last charcter
    elif string[0]==string[-1]: 
        return palindrome(string[1:-1])
    else:
        return False #return False if both above condition is not true

#execution program start from here
def main():
    string=input('Enter the string')#taking string from user
    #calling function to check string is palindrome if its return True  else its not
    if palindrome(string)==True: 
        print(string ,' is palindrome')
    else:
        print(string,' is not palindrome')
main()
