#proggram to find maximum and minimum from vector

def main():
    #taking input from user for demension of vector
    d=int(input('Enter the number of element in vector: '))

    #taking input form user from user
    print('Enter the vector')
    vector=[int(input()) for i in range (d)]

    #print the vector
    print('vector is :')
    print(*vector,sep=',')

    maxMin(vector)#call function to findout the max and min from vector.

def maxMin(vector):#create function to findout max and min from vector
    maximum=vector[0]#declare variable for max
    #loop for maximum from vector
    for i in vector:
        if i>maximum: maximum=i

    minimum=vector[0]#declare variable for min
    #loop for minimum from vector
    for j in vector:
        if j<minimum: minimum=j
    #print maximum and minimum from vector
    print("Max=",maximum)
    print("Min=",minimum)

main()
