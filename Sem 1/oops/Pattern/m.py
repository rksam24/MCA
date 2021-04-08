"""
This program takes an interger number 'n' and print
the pattern below in 'n' rows
$ $ $ $ $
  $ $ $ $
    $ $ $
      $ $
        $
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
        #problem divied into two part
        '''first part : spaces
every row has i space eg: if i= 0 in pattern then in first row the
space is 0, if i=1 in second row space is 2 and so on.  ''' 
        for j in range(i):#for loop for spaces
            print(' ', end=' ')#print space

        '''second part: number part
eg:$$$$$
    $$$$
     $$$
      $$
       $
       in first row no. of value is 5 and in second row no. of value is 4
       i.e each row has value of i+1 to number row. eg if row=4 and i=3 then it print $$$
       range for for loop is (i+1, row+1)'''
        for k in range(i+1, row+1):#for to print $
            print("$", end=' ')#print $ everytime loop repeat
        print()#ending of line for each row

main()
