"""
This program takes an interger number 'n' and print
the pattern below in 'n' rows
   *
  * *
 *    *
*      *
 *    *
  *  *
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
    '''uperpart of pattern
eg:
   *
  * *
 *   *
*     *
'''
    for i in range(1,row+1): # loop for row
        #upperpart divied into two part
        '''first part : spaces
every row has row-i space eg: if there is 4 row in pattern then in first row the
space is 4-1=3, in second row space is 4-2=2 and so on. so range is (0,row-i) '''
        for j in range(0,row-i):#loop for space
            print(' ',end='')#print space
        '''second part: remaing part including space b/w *
eg:
   *
  * *
 *   *
*     *
in this when row is 4 then no.of column is 7
and when row is 5 then no.of column is 9
i.e no of star in first row/no.of column is 2*-1 then range for
for loop is (1,2*1). 
       '''
        for k in range(1,2*i): #for loop to print *
            if k==1 or k==2*i-1:
                print('*',end='')
            #k=1 and k=2*i-1 print * i. i.e when for loop repeat first time and last time 
            else:
                print(' ',end='')#when above condition not met  space is given i.e space b/w
        print() #ending line after each row

        '''lowerpart of part
eg:
 *   *
  * *
   *
'''
    for i in range(row-1,0,-1): #loop for row
        #lowerpart divied into two part
        '''first part : spaces
every row has row-i space eg: if there is 4 row in pattern then in first row the
space is 4-3=1, in second row space is 4-2=2 and so on. so range is (0,row-i) '''
        for j in range(0,row-i):#for loop for spaces
            print(' ', end='')#prints space
        '''second part: remaing part including space b/w *
eg:
 *   *
  * *
   *
'''
        for j in range(1, 2*i):#for loop to print *
            if j==1 or j==2*i-1:
                print('*', end='')
        #j=1 and j=2*i-1 print * i. i.e when for loop repeat first time and last time 
            else:
                print(' ', end='')#when above condition not met  space is given i.e space b/w
        print()#ending the line
 

main()
