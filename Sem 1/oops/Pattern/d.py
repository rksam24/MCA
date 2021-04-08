"""
This program takes an interger number 'n' and print
the pattern below in 'n' rows
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5 """

def main():
    row = int(input("Enter Number of Rows: "))#take input from user
    pattern(row)#calling function to print pattern


def pattern(row):
    """Purpose: This function is designed to print the desired pattern
Input: row:take an interger value as input
output:print the desired pattern
"""
    for i in range(row):#looping for row
        for j in range(i+1):
            print(i+1 ,end="  ")
        #end=' ' is for so that its print in same line
        '''logic: eg: row=4
first time for loop execut i=0 then it go inner loop where start value of j=0 inner loop execute its statement
and print 1 which is value of i then j=1 but range for inner loop is i+1 (i=0)=1 then this for stop here then
value of i=1 , j=0 inner loop print 2 then j=1 it print 2 . and so on
'''
        print() #ending of the line
    
main()
