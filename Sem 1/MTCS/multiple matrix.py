#program for multiplication two matrix

def main():
    #taking input from user for row and column for two matrix
    m = int( input("enter first matrix rows"))
    n = int( input("enter first matrix columns"))
    p = int( input("enter second matrix rows"))
    q = int( input("enter second matrix columns"))

    # checking if multipilication b/w two matrix possible or not if not then exit program
    if( n != p): 
        print ("matrice multipilication not possible...")
        exit()

   #declaration of list for matrix
    matrix1=[[0 for j in range  (0 , n)] for i in range (0 , m)]
    matrix2=[[0 for j in range  (0 , q)] for i in range (0 , p)]
    resultMatrix=[[0 for j in range  (0 , q)] for i in range (0 , m)]
 
    #taking input from user for elements of matrix A and B
    print ("enter first matrix A elements:" )
    for i in range(0 , m):
        for j in range(0 , n):
            print('A[',i+1,'][',j+1,']=',end='')
            matrix1[i][j]=int (input())    
    print ("enter second matrix B elements:")
    for i in range(0 , p):
        for j in range(0 , q):
            print('B[',i+1,'][',j+1,']=',end='')
            matrix2[i][j]=int(input())

    #print two matrix
    print('Two matrix are:')
    print ("First Matrix")
    printMatrix(matrix1) #calling function to print matrix
    print ("Second Matrix")
    printMatrix(matrix2) #calling function to print matrix

    #for multiplication of two matrix
    # i will run throgh each row of matrix1
    for i in range(0 , m):
        # j will run through each column of matrix 2
        for j in range(0 , q):
            # k will run throguh each row of matrix 2
            for k in range(0 , n):
                resultMatrix[i][j] += matrix1[i][k] * matrix2[k][j]
				
    #printing result/ multiplication of two matrix
    print ( "Multiplication of two matrices(A and B matirx):" )
    printMatrix(resultMatrix)


def printMatrix(matrix):#function to print matrix
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(matrix[i][j],end=" ")
        print()
	
main()
