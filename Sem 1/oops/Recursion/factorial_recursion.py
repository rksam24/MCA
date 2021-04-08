''' Program to
    a) print factorial of all number from 1 to N
    b) print factorial of number from  N to 1
'''
def main():
    n=int(input("Enter the number: "))#take the number from user as input
    
    print('\nA.Print factorial of all number from 1 to',n)#print statement
    print('B.Print factorial of number from',n,'to 1')#print statement
    ch=input('Choose one option from above: ')#taking input from user for choice

    numlist=[i+1 for i in range(n)] #create list containing number from 1 to n

    #call the function for list containing factorial of number from 1 to n and assign it to factlist
    factlist=factoriallist(numlist)

    #to check the choice
    if ch=='A' or ch=='a':
        print("\nFactorial from 1 to",n,"are:") #print satement
        print(*factlist,'\n',sep=',')#print factorial from 1 to n number
    elif ch=='B' or ch=='b':
        print("\nFactorial from",n,"to 1 are:") #print satement
        print(*factlist[::-1],sep=',')#print factorial from n to 1 number
    else:
        print('Invalid choice') #print this statement when user enter invalid choose
    
#function for create list containig factorial from 1 to n number
def factoriallist(numlist):
    '''create list containing factorial from 1 to number
       inside list function fact(num) is call whenever loop repeat for number in
       list numlist to findout factorial for that particular number then add/append
       that factorial to new list factlist
    '''
    factlist=[fact(i) for i in numlist]
    return factlist #return the the list containing factorial from 1 to n number
    
#function to findout factorial of number
def fact(num):
    if num==1:# if that number is 1 then return that number
        return num
    else:
        return num*(fact(num-1)) #return factorial for number using recursion
    '''
whenever program execute return num*(fact(num-1)) function is call
ex: assume num=5
then program go to return statement num *(fact(num-1)) which is also written
5* fact(4) then function fact call for num 4 i.e fact(4) that statement become
5*4*fact(3) then again for num 3 , fact(3) statement become 5*4*3*fact(2)
then for num 2 statement become 5*4*3*2 fact(1) then num 1 i.e fact(1) num is return
and statement become 5*4*3*2*1 and we get result 120
'''

main()
