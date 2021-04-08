#program to find out sum of the diagonal element of matrix

def main():
    n = int( input("Enter Square matrix Size : ")) #asking number of rows from user for matrix

    #declaration of list for matrix
    matrix=[[0 for j in range  (0 , n)] for i in range (0 , n)] 
    #taking input from user for elements of matrix
    print ("Enter matrix elements:" )
    for i in range(0 , n):
        for j in range(0 , n):
            print('A[',i,'][',j,']=',end='')
            matrix[i][j]=int (input())

    #Print the matrix
    print("Matrix: ")
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(matrix[i][j],end=" ")
        print()

    diagonalSum(matrix)#call function for sum of diagonal element


def diagonalSum(matrix):#function to add diagonal element
    sum1=0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i==j: #checking element of matrix is diagonal element or not
                sum1=sum1+ matrix[i][j] #sum of diagonal element
    print ('Sum of the diagonal matrix:',sum1 )

    
main()
