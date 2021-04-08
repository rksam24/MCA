"""
This program takes an interger number 'n' and print
the pattern below in 'n' rows
* * * * * * *
  * * * * *
    * * *
      *
"""

def main():
    row = int(input("Enter Number of Rows: "))#take input from user
    pattern(row)#calling function to print pattern
    
def pattern(row):
    """Purpose: This function is designed to print the desired pattern
Input: row:take an interger value as input
output:print the desired pattern
"""
    for i in range(row,0,-1):#looping for row
         #problem divied into two part
        '''first part : spaces
every row has row-i space eg: if row=4 then space is row-i i.e 4-4=0 in first row
then in second row space is row-i i.e 4-3=1 space and so on.
then range for for loop is (row-i)''' 
        for j in range(row-i):#for loop for spaces
            print(' ', end='  ')#prints space
        '''second part: remaing * part
eg:
*******
 *****
  ***
   *
in this when row is 4 then no of star in first row/no.of column is 7
and when row is 5 then no of star in first row/no.of column is 9
i.e no of star in first row/no.of column is 2*-1 then range for
for loop is (0,2*1-1).
'''
        for j in range(2*i-1):#for loop to print *
            print('*',end='  ')#every time loop repeat * print
        print()#ending line after each row

main()
