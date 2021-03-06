'''Program to find the sum of squared N natural numbers ( recursive )
eg:
1^2 +2^2+ 3^2+......+N^2
'''

#find to find sum up all the squares from 1 to n
def squareNumberSum(num):
    if num==1: # base case if num is 1 is return
        return num
    else:
        return (num**2) + squareNumberSum(num-1) # return the sum of all square


def main():
    print('To find sum of \n1^2 +2^2+ 3^2+......+N^2')
    num=int(input('\nEnter the N: ')) #taking input from user
    print('Sum from 1^2 to {}^2 == {}'.format(num, squareNumberSum(num) )) #call funtion to print sum of series

main()