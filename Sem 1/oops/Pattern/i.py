"""
This program takes an interger number 'n' and print
the pattern below in 'n' rows
* * * * * * *
  *       *
    *   *
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
    for i in range(row,0, -1):#looping for row
        #problem divied into two part
        '''first part : spaces
every row has row-i space eg: if row=4 then space is row-i i.e 4-4=0 in first row
then in second row space is row-i i.e 4-3=1 space and so on.
then range for for loop is (row-i)''' 
        for j in range(0,row-i):#for loop for spaces
            print(" ", end=" ")#prints space
        '''second part: remaing part including space b/w *
eg:
*******
 *   *
  * *
   *
in this when row is 4 then no of star in first row/no.of column is 7
and when row is 5 then no of star in first row/no.of column is 9
i.e no of star in first row/no.of column is 2*-1 then range for
for loop is (1,2*1). 
       '''
        for j in range(1, 2*i):#for loop to print *
            if i==row or j==1 or j==2*i-1:
        #i=row print* i.e first row first time i=row, j=1 and j=2*i-1 print * i.e when for loop repeat first time and last time 
                print("*", end=" ")
            else:
                print(" ", end=" ") #when above condition not met  space is given i.e space b/w *'s
        print()#ending line after each row

main()
