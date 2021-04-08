
def main():
    percentage=float(input("Enter the percentage"))
    grade(percentage)

def grade(p):
    if(p>=90):
        print("Grade:A+")
    elif(p>=80):
        print("Grade:A")
    elif(p>=70):
        print("Grade:B")
    elif(p>=60):
        print("Grade:C")
    elif(p>=50):
        print("Grade:D")
    elif(p>=40):
        print("Grade:E")
    else:
        print("Fail")

if __name__=='__main__':
    main()
