def main():
    num=int(input('Enter the number'))#take the input number from user

    x=sqdNumbers(num)#calling the Function for square of each digit and assigen it to variable x
    print('Square of each of each number (from left digit to right digit)')#print statement
    print(*x,sep=',')#print the square of each digit

    sqdNumber_result=sumOfSqdNumber(x)#calling function for sum of square of digit and assign it to variable sqdNumber_result
    print('Sum of square of each digit =',sqdNumber_result)#print the sum of square of digit


#function sum to findout the square of each digit of number
def sqdNumbers(num):
    sqdnumber=[] # create empty list to store the the square of each digit
    while num>0: #while loop for find out square of each digit
        reminder=num%10 #find out reminder of num to find out the last digit of number
        #square the last digit/reminder of number then add/append that number to list
        sqdnumber.append(reminder**2)
        num=num//10#divide the number by 10 so that when loop repeat last digit of number remove
    return sqdnumber[::-1] #return the reverse of list which contain square of each digit
    
#function to findout the sum of sqaure of each digit of number
def sumOfSqdNumber(x):
    sqdNumber_result=0#declare the variable to store sum of square of each digit
    for i in x:#looping to findout the result
        sqdNumber_result=sqdNumber_result+i #add square of each digit of number to sqdNumber_result
    return sqdNumber_result #return the final result

main()
