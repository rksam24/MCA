def main():
    a=int(input('Enter the first number'))
    b=int(input('Enter the second number'))
    a,b=swap(a,b)
    print('After swap')
    print('first number',a)
    print('Second number',b)



def swap(a,b):
    c=a
    a=b
    b=c
    return a,b
main()
