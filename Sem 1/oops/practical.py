








"""
Q2. This program takes an interger number 'n' and print
the pattern below in 'n' rows
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5 """

"""Purpose: This function is designed to print the desired pattern
Input: row:take an interger value as input
patternType: type of pattern
output:print the desired pattern
"""
def pattern(row,patternType):
    if patternType=='1':
        for i in  range(row):
            for j in range(i+1):
                print(i**2 ,end="  ")
            #end=' ' is for so that its print in same line
            print() #ending of the line
    if patternType=='2':
        for i in range(row):#looping for row
            for j in range(i+1):
                print(i+1 ,end="  ")
            #end=' ' is for so that its print in same line
            print() #ending of the line



def main():
   n=int(input("Enter the number of row"))
   print("""Pattern 1. 
1
4 9
16 25 36
pattern 2. 
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
    """)
   patternType=input("Pattern type: ")
   pattern(n,patternType)


    
main()
