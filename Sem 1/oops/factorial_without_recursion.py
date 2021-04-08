'''
Program to findout factorial of number without recursion
eg: i/p: 5
o/p:factorial=120
'''

def main():
    num=int(input("Enter the number: ")) #take the number from user as input
    if num<0:#checking if number is -ve if its -ve then factorial not exit for that number
        print("Factorial doesn't exist for negative numbers")
    else:
        #call the function to findout for factorial of number and print it
        print("Factorial of", num, "is",fact(num))        

#function to find out factorial of number
def fact(num):
    fact=1 #declare variable to store factorial of number
    for i in range(1,num+1): #loop for factorial
        fact=fact*i # to find factorial.first time loop fact=1*1 then fact=1*2,then fact=2*3, then fact=6*4 and soon
    return fact #return factorial for number
        
        

main()

