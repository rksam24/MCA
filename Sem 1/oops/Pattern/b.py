"""
This program takes an interger number 'n' and print
the pattern below in 'n' rows
        1
      2 1 2
    3 2 1 2 3
  4 3 2 1 2 3 4
5 4 3 2 1 2 3 4 5 """

def main():
    row = int(input("Enter Number of Rows: "))#take input from user
    pattern(row)#calling function to print pattern

def pattern(row):
    """Purpose: This function is designed to print the desired pattern
Input: row:take an interger value as input
output:print the desired pattern
"""
    for i in range(1,row+1):#looping for row
        #problem divied into three part
        '''first part : spaces
every row has row-i space eg: if there is 5 row in pattern then in first row the
space is 5-1=4, in second row space is 5-2=3 and so on.  '''

        for j in range(1,row-i+1):#looping for space
            print(" ",end="  ")#print space
        '''second part: first triangle
eg:    1
      21
     321
    4321
   54321
   in this in first for there is 1 value and in second row there is 2 value and so on.
   i.e number of value in each row is equal to row so range is (i,0,-1) i is row value
   0 is end value and -1 is step. '''
        for k in range(i,0,-1):
            print(k,end="  ") #print the value of k eg: if i=2 first print 2 and k in same line
        '''third part: second triangel
eg:

2
234
2345
'''
        for l in range(2,i+1):
            '''
            as inital value of l is 2 because first we start print from 2 then innext line 2 3
            up to i+1 that when row is 1 range value 1+1=2 then it don't execute for loop and i=2 i.e
            in second row it range become 2+1=3 then print 3 and so on. '''
            print(l,end="  ")
        print() #use to go next line
   


main()
