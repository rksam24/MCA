def main():
    num=int(input("Enter the number: "))
    checkPrime(num)

def checkPrime(num):
    flag=0
    if (num>1):
        for i in range(2,num):
            if (num % i) == 0:
                flag=1
                break
        if(f==0):
            print(num,"is a prime number")
        else:
            print(num,"is not a prime number")
                
    else:
        print(num,"is not a prime number")

main()
