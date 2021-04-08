""""
program for Given a list of 'n' number i.e 1 to n, print even and odd number
eg: i/p:n=10
o/p: even number are: 2,4,6,8,10
od number are: 1,3,5,7,9
"""

def main():
    n=int(input('Enter the number: '))#taking input from user
    list1=[]#creating a empty list
    for i in range (1,n+1): # looping for add value in list from 1 to n eg:[1,2,3..]
        list1.append(i) #add the value in list from 1 to n
    print('List is ', list1)
    oddEvenNumber(list1,n)#calling function to print even and odd number

def oddEvenNumber(list1,n):
    ''' purpose: this function is desigen to print odd and even number
input:
    list1: take list as input
output:
    print even and odd numbers
'''
    even=[]#create a empty list for even number
    odd=[]#create a empty list for odd number
    for i in list1: #iterating each number in list
        if i%2==0: #check condition 
            even.append(i)#add the item in list if its divide by 2 i.e. if its even
        else:
            odd.append(i)##add the item in list if its not divide by 2 i.e. if its odd
    print('Even number from 1 to',n,'are ',end='')#print statement
    print(*even,sep=',') # print even number
    print('Total even number from 1 to',n,'is ',len(even))#print total even number
    print()#for next line
    print('Odd number from 1 to',n,'are ',end='')#print statement
    print(*odd,sep=',')# print odd number
    print('Total odd number from 1 to',n,'is ',len(odd)) #print total odd number

main()
