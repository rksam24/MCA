""""
This program takes an interger number 'n' and print
the pattern below in 'n' rows
*  *  *  *  *
*           *
*           *
*           *
*  *  *  *  *
"""
def main():
    row = int(input("Enter Number of Rows: "))#take input from user
    pattern(row)#calling function to print pattern
    
def pattern(row):
    """Purpose: This function is designed to print the desired pattern
Input: row:take an interger value as input
output:print the desired pattern
"""
    for i in range(1,row+1) : #loop for row
        for j in range(1,row+1) : 
            if (i == 1 or i == row or
                j == 1 or j == row) : 
                print("*", end="  ")             
            else : 
                print(" ", end="  ")
        print() #ending line after each row
    '''logic for above loop:
in outer for loop range of i in (1,row+1) that mean start value for loop is 1
and it repeat until i=row then in inner for loop range of j in (1,row+1) that
mean start value for loop is 1 and it repeat until j=row then and inner loop
it check ifi=1,row or j=1,row . if value of i and j is equal to no of row then
it print * i.e in first row and last row. and when value of i and j is 1 then it
print * i.e in first and last column

'''
  
main()
