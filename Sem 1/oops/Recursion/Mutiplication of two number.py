'''
Program to multipy 2 number
condition:
1.without using multipication operator
2.using recursion
'''
def mult(a,b):
    if b==0: # when value of b is 0 then return 0
        return 0
    else:
        return a+mult(a,b-1) # add value of each time whrn function is call
    
    
#Main part of program program start from here
'''
here a and b is number
result is multiplication result of a and b
'''
def main():
    #taking two muber from user
    a=int(input('Enter first number with space'))
    b=int(input('Enter second number with space'))

    #check different case for multipication and call function acc. to that
    #the number a and b is become +ve to for parameter of function
    #if result of a and b is -ve thenn it add later when function retrn result
    if a==0 or b==0: # if any one number is 0 result is zero
        result=0
    elif a<0 and b>0: # if a is -ve and and b is +ve.
        result=-(mult(-(a),b)) #result will be -ve, call the function for multiplication
    elif a>0 and b<0:
        result=-(mult(-(b),a))
    elif (a<0 and b<0):
        if -(a)>-(b): # if number a is greater then b then it remain same otherwise swap a and b when calling function
            result=mult(-(a),-(b))
        else:
            result=mul(-(b),-(a))
    else:
        if a>b: #if number a is greater then b then it remain same otherwise swap a and b when calling function
            result=mult(a,b)
        else:
            result=mult(b,a)
    print('Multiplication of',a,'and',b,'is',result)
main()


    
