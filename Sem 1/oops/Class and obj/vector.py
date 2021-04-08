class vector:
    #contructor of class contain attribute of class
    def __init__(self,vector1,vector2):
        self.vector1=vector1
        self.vector2=vector2
    
    #function to add the two vector
    def addVector(self):
        self.sumVector=[] #list contain add result of two vector
        for i in range(len(self.vector1)): # loop to add vector
            self.sumVector.append(self.vector1[i]+self.vector2[i])
        return self.sumVector
    
    #function to subtract two vectors
    def subtarctVector(self):
        self.subVector=[] #list contain add subtact of two vector
        for i in range(len(self.vector1)): # loop to subtract vector
            self.subVector.append(self.vector1[i]-self.vector2[i])
        return self.subVector
    
    #function to multiply two vector
    def MultiplyVector(self):
        self.mulVector=[] #list contain multiply result of two vector
        for i in range(len(self.vector1)): # loop to multiply vector
            self.mulVector.append(self.vector1[i]*self.vector2[i])
        return self.mulVector
    
def main():
    vectorSize=int(input('Enter the Size: '))
    #taking two vector from user
    print('Enter Vector 1 element')
    vector1=[int(input()) for i in range(vectorSize)]
    print('Enter Vector 2 element')
    vector2=[int(input()) for i in range(vectorSize)]

    #printing the vector
    print('Vector 1: ',vector1)
    print('Vector 2: ',vector2)

    #create obj vec for class vector
    vec=vector(vector1,vector2)
    print("\nChoose one option:\n1. Addition of two vector\n2. Subtract two vector\n3. Multiplication of two vector\n4. Exit ")
    while(True):
        choice=input('\nEnter your choice from above\n')
        if choice=='1':
            print('Addition of two vector: ',vec.addVector()) #calling function to add two vector
            break
        elif choice=='2':
            print('Subtract two Vector: ',vec.subtarctVector()) #calling function to subtract two vector
            break
        elif choice=='3':
            print('Multiply two vector(Element by element product): ',vec.MultiplyVector()) #calling function to multiply two vector
            break
        elif choice=='4': 
            exit #exit the code
        else:
            print('Invaild choice!! try again')

if __name__ == '__main__':
    main()
    