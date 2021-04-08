"""
This program takes an interger number 'n' and print
the pattern below in 'n' rows
    #
   ##
  ###
 ####
#####
"""
def main():
    row = int(input("Enter Number of Rows: "))#take input from user
    pattern(row)#calling function to print pattern
    
def pattern(row):
    """Purpose: This function is designed to print the desired pattern
Input: row:take an interger value as input
output:print the desired pattern
"""
    for i in range(row):#looping for row
        for j in range(row-1-i):#loop for space
            print(' ', end='  ')#print space
        for k in range(i+1):# loop for print #
            print("#", end='  ') #print #
        print()

main()
