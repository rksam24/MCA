

def main():
    print("welcome")
    print("main function")
    a=int(input("Enter First Number:"))
    b=int(input("Enter Second Number:"))
    c=int(input("Enter third Number:"))
    compare(a,b,c)


def compare(a,b,c):
    if (a==b==c):
        print("All number are equal")
    elif (a>b):
        if(a>c):
            print(a,"is greatest number")
        else:
            print(c,"is greatest number")
    elif (b>c):
            print(b,"is greatest number")
    else:
        print(c,"is greatest number")

if __name__=='__main__':
    main()

