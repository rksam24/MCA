"""
This program takes an interger number 'n' and print
the pattern below in 'n' rows
      *
    * * *
  * * * * *
* * * * * * *
"""
def main():
    row = int(input("Enter Number of Rows: "))#take input from user
    pattern(row)#calling function to print pattern
    
def pattern(row):
    """Purpose: This function is designed to print the desired pattern
Input: row:take an interger value as input
output:print the desired pattern
"""
    for i in range(1,row+1):
         #problem divied into three part
        '''first part : spaces
every row has row-i space eg: if there is 5 row in pattern then in first row the
space is 5-1=4, in second row space is 5-2=3 and so on.  '''
        for j in range(1,row+1-i): #loop for space
            print(" ",end="  ") #print space
        '''second part: first triangle
eg:    *
      **
     ***
    ****
   in this in first for there is 1 value and in second row there is 2 value and so on.
   i.e number of value in each row is equal to row so range i``s (i,0,-1) i is row value
   0 is end value and -1 is step. '''
        for k in range(i,0,-1):
            print("*",end="  ")
        '''third part: second triangel
eg:

*
**
***
'''
        for l in range(1,i):
            '''
            range for this for loop is (1,l) start value 1 and i row number when i=1
            for loop not execute and when i=2 it print * and when i=3 it print **
            and so on.
            '''
            print("*",end="  ")
        print()


main()
