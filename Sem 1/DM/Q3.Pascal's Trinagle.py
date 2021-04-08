#program for Pascal Triangle

#function to findout factorial of number
def fact(num):
    if num==1 or num==0:# if that number is 1 then return that number
        return 1
    else:
        return num*(fact(num-1)) #return factorial for number using recursion

#program execute from here
def main():
    row=int(input("Enter number for Pascal's trinagle: "))
    #loop to print parcals triangle
    for i in range (row):
        #inner loop to print spaces
        for j in range(row-i):
            print(end=' ')
        #loop to print values of parcal's triangle
        for l in range(i+1):
            C=fact(i)/(fact((i-l))*fact(l)) #find the values of parcal's triangle
            print(int(C),end=' ')#print the values
        print()#for next line after each line

main()