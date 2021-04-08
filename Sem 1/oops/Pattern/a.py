"""
This program takes an interger number 'n' and print
the pattern below in 'n' rows
    1
    1 2
    1 2 3
    1 2 3 4
    1 2 3 4 5 """

def main():
    row = int(input("Enter Number of Rows: "))#take input from user
    pattern(row)#calling function to print pattern


def pattern(row):
    """Purpose: This function is designed to print the desired pattern
Input: row:take an interger value as input
output:print the desired pattern
"""
    for i in range(row):#looping for row
        for j in range(i+1):#looping for column
            print(j+1,end="  ")
        #print the value of j eg:if j=0 then it print1 , if j=1 its print2 and so on
        #end=' ' is for so that its print in same line
        print() #ending line after each row
  

main()
