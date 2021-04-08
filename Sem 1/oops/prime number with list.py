""""
program for Given a list of 'n' number i.e 1 to n, print prime numbers and total
number of prime number
eg: i/p:n=10
o/p: prime numbers : 2,3,5,7
total number of prime number are  4
"""

def main():
    n=int(input('Enter the a number: '))# take input from user for last number
    list1=[]#creating a empty list
    for i in range(1,n+1):# looping for add value in list from 1 to n eg:[1,2,3..]
        list1.append(i)#add the value in list from 1 to n
    primeNumber(list1,n)#print prime numbers

def primeNumber(list1,n):
    ''' purpose: this function is desigen to print odd and even number
input:
    list1: take list as input
    n:last number/vlaue in list
output:
    print prime number and total number of prime number
'''
    primeNumber=[]#create a list for prime numbers
    for i in list1: #iterating each number in list
        if i>1: #check condition 
            if i==2:#check condition
                primeNumber.append(i)#add number to list if number is 2
            else:
                flag=0 #delcare a variable flag and assign value 0
                for j in range(2,i):#looping to find out prime number
                    if (i % j) == 0:#checking condition for prime number
                        flag=1 # if condition value of flag change from 0 to 1
                        break#end the loop
                if flag==0:# check condition if value of flag 0 or not
                    primeNumber.append(i)#if flag=0 then that number add to list
    print('Prime Numbers from 1 to',n,'are: ', end='') #print statement
    print(*primeNumber,sep=',')#print prime number from 1 to n
    print('Total Prime number from 1 to',n,'are',len(primeNumber))
    #print total number of prime number

main()


