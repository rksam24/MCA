'''
Program ro reverse the string
condition: use recursion
'''

#function to reverse the string
def reverse(string):
    if string=='':#when string is empty. return empty string
        return ''
    else:
        # all the function again with string start with 2 character and add fist value to that function
        return reverse(string[1:])+string[0] 

#execution of program start from here
def main():
    string=input('Enter the string: ')#taking string as input
    print('reverse of string =', reverse(string)) #all the function to print reverse of string
main()
