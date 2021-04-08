"""
This program takes an interger number 'n' and print
the pattern below in 'n' rows
5 4 3 2 1
4 3 2 1
3 2 1
2 2
1          """

def main():
    row = int(input("Enter Number of Rows: "))#take input from user
    pattern(row)#calling function to print pattern
    
def pattern(row):
    """Purpose: This function is designed to print the desired pattern
Input: row:take an interger value as input
output:print the desired pattern
"""
    for i in range(row, 0,-1):#looping for row
        '''here intial value of i because when row is 1 it print 5 value which total number of row or row-0
in second row 4 value which row-1 and so on. and 0 is end value and -1 is step which mean value of i decrease by 1
eg: if i=5 then next time i=4 then  and so on '''
        for j in range(i, 0, -1):
            ''' value of j is start with value of i eg: if i=5 then start value of j=5
0 is end value(0 not include when j=0 loop is stop) and -1 is step'''
            print(j, end="  ") #print value of j eg:when j=5 it print 5 then next time 4 and so on 
        print() #ending the line
    
main()
