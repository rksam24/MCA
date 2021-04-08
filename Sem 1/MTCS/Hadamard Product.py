#program for Element-wise multipication(hadamard Product)

def main():
    #taking input from user for row and column of matrix
    m = int( input("enter rows of matrixs: "))
    n = int( input("enter column of matrixs: "))
    
    #declaration of list for matrix
    matrix1=[[0 for j in range  (0 , n)] for i in range (0 , m)]
    matrix2=[[0 for j in range  (0 , n)] for i in range (0 , m)]
    resultMatrix=[[0 for j in range  (0 , n)] for i in range (0 , m)]

    #taking input from user for elements of matrix A and B
    print ("\nEnter first matrix A elements:" )
    for i in range(0 , m):
        for j in range(0 , n):
            print('A[',i+1,'][',j+1,']=',end='')
            matrix1[i][j]=int (input())
    print ("\nEnter second matrix B elements:")
    for i in range(0 , m):
        for j in range(0 , n):
            print('B[',i+1,'][',j+1,']=',end='')
            matrix2[i][j]=int(input())
            
    #print the two matrix
    print('\nTwo matrix are:')
    print ("\nFirst Matrix")
    printMatrix(matrix1) #calling function to print matrix
    print ("\nSecond Matrix")
    printMatrix(matrix2) #calling function to print matrix

    #for multiplication of two matrix
    # i will run throgh each row of matrix1, matrix2
    for i in range(0 , m):
        # j will run through each column of matrix1,matrix2
        for j in range(0 , n):
            resultMatrix[i][j] += matrix1[i][j] * matrix2[i][j]

    #printing Hadamard Product(element by element) of two matrix
    print ( "\nHadamard Product(element by element) of two matrix:" )
    printMatrix(resultMatrix)


def printMatrix(matrix):#function to print matrix
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print('\t',matrix[i][j],end=" ")
        print()
	
main()
