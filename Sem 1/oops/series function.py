'''
Program to find tge sum of nth terms of given series
1-x^2/2!+x^4/4!-x^6/6!+.........x^n/n!
'''
def main():
    n=int(input('Enter the nth term: '))#take input from user for nth term
    x=int(input("Enter the X value: "))#take input from user for values of
    findSum(n,x)#calling function to find out sum of series
    
def findSum(n,x):
    #declare variable sum
    sum=1 # first term of series is 1 that's why sum=1
    for i in range(1,n): #loop for nth terms
        #factorial part
        for j in range (1,int(2*i)+1): # loop to find out factorial part of a term
            fact = 1 # declare variable fact and assign value 1
            fact = fact * j
        #addition part
        sum=sum+(-1**i)*(x**(2*i))/fact #adding the terms
        #(-1**1) because sum =1 and second term of series act as first term in loop
    #result
    print("Sum of nth terms",sum) #print the sum of series

main()
