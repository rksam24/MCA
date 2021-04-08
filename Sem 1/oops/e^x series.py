'''
Program to find tge sum of nth terms of given series
e^x = 1+x/1!+x^2/2!-x^3/3!+.........
'''
def main():
    n=int(input('Enter the nth term: '))#take input from user for nth term
    x=int(input("Enter the X value: "))#take input from user for values of
    findSum(n,x)#calling function to find out sum of series

def findSum(n,x):
    #declare variable sum
    sum=1 # first term of series is 1 that's why sum=1
    for i in range(1,n):#loop for nth terms
        #factorial part
        fact = 1
        if i >= 1:
            for j in range (1,int(i)+1):# loop to find out factorial part of a term
                fact = fact * j
        #addition part
        sum=sum+(x**i)/fact#adding the terms
    #result
    print("Sum of nth terms",sum)#print the sum of series

main()
