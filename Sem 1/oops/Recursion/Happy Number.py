def main():
    num=int(input('Enter the number'))#taking number from user as input
    
    if checkHappyNumber(num)==True: #calling the function and checking if its retuen true or not
        print(num,'is Happy Number') #print the statement if condition is true
    else:
        print(num,'is not Happy Number') #print the statement if condition is not true
        
#Function to check if number is Happy number or not. if its happy number than its true 
def checkHappyNumber(num):
    #calling the function for the sum of the squares of digits of number and assign it to variable result
    result=sumofSqdigit(num) 
    for i in range(10): #loop to check Happy number, loop only iterate 10 times
        if result==1:#checking the happy number. Happy number always end at 1
            return True #return True
        else:
            #if condition fail for Happy Number then check the again for Sum of square of digit of the number
            result=sumofSqdigit(result)

'''
purpose:compute the sum of the squares of digits of number
i/p: num= a number
o/p: return the sum of square of digit of number

eg: num=32
o/p: 13
'''   
def sumofSqdigit(num):
    result=0
    while num>0: #while loop for find out square of each digit
        reminder=num%10 #find out reminder of num to find out the last digit of number
        #square the last digit/reminder of number then add/append that number to list
        result=result+(reminder**2)
        num=num//10#divide the number by 10 so that when loop repeat last digit of number remove
    return result #return the reverse of list which contain square of each digit
    
main()
