#Program from outer product of two matrix

def main():
    #taking length of vector
    n=int(input('Enter length of vector 1:'))
    m=int(input('Enter length of vector 2:'))
    
    #declaration of list for vector taking value from user
    print ("enter first vector elements:" )
    vector1=[int(input()) for i in range(n)]
    print ("enter second vector elements:")
    vector2=[int(input()) for i in range(m)]

    #list for outer product of two vector
    result=[[0 for j in range(m)] for i in range(n)]
    
    #print the vector 
    print('Two vector in matrix form are:')
    print ("First vector: ",vector1)
    print ("Second vector: ",vector2)
    
    #for outer product of two vector
    for i in range(n):# i run through each value of vector2 
        for j in range(0 , m):#j run through each value of vector1 matrix
            result[i][j] += vector1[i] * vector2[j]

    #print outer product
    print ( "Outer Product of two vector:" )
    for i in range(len(result)):
        for j in range(len(result[0])):
            print('\t',result[i][j],end=" ")
        print()
main()
