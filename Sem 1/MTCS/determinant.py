#Program to find out Determinant of matrix

from copy import deepcopy

def main():
    #Taking input from user for order of matrix
    n=int(input("Enter the order of the matrix: "))

    #declare list for matrix and taking input from user for element of matrix
    print("Enter the elements of the matrix one by one:")
    A=[[int(input()) for i in range (n)] for j in range (n)]

    #print the matrix
    print('Matrix is:')
    for i in range(len(A)):
        for j in range(len(A[0])):
            print(A[i][j],end=" ")
        print()

    #print the determinant of matrix
    result = det(A)
    print('Determinant: ',result)

#function to find determinant of matrix
def det(A):
    row=len(A) #to find out number of row in matrix and assign it to row
    determinant=0#delcare variable which store determinate of matrix
    
    #checking if matrix is 2 X 2 and findout its determinate and return it
    if(row == 2):
        determinant = A[0][0]*A[1][1]-A[0][1]*A[1][0]
        return determinant
    else:
        #cofactor expansion to find out determinate of matrix
        #loop for doing cofactor expansion in first row of matrix
        for i in range(row):            
            cofactor=(-1)**i * A[0][i] * det(smallerMatrix(A,0,i))
            determinant +=cofactor
        return determinant #return determinate 

#function to remove column and row to matrix and return that matrix to find out determinate of that matrix
def smallerMatrix(matrix,row,column):
    #use deepcopy so that new matrix should not affect the original matrix
    newMatrix=deepcopy(matrix)
    newMatrix.remove(matrix[row])#remove the row from new matrix
    #loop to remove column from new matrix
    for i in range(len(newMatrix)):
        newMatrix[i].remove(newMatrix[i][column])
    return newMatrix #return new matrix


main()
