class student:
    #constructor
    def __init__(self,name,rollNo):
        self.name=name
        self.rollNo=rollNo

    #defining __str__()e
    def __str__(self):
        return 'Name: '+self.name+'\nRoll NO: '+str(self.rollNo)+'\n'
    
class stack:
    size=0
    #constructor
    def __init__(self):
        self.stacks=[]
    
    #Function to push element in stack
    #stu is student record which add to stack
    #return push element
    def push(self,stu):
        #if length of stack is exceed size of stack return stack is full!!
        if len(self.stacks)>=stack.size:
            return False
        else:
            #push student detail to stack
            self.stacks.append(stu)
            return stu
    

    #function to pop the last/top element of stack
    #return pop element
    def pop(self):
        #when stack is empty return stack is empty
        if len(self.stacks)==0:
            return 'Stack is empty!!'
        else:
            return self.stacks.pop()
    
    #function to peek top element of stack
    #return the top element of stack
    def peek(self):
        #when stack is empty
        if len(self.stacks)==0:
            return 'Stack is empty!! No element to peek'
        else:
            return self.stacks[-1]

    #function to findout number of element in stack
    #return the total number of element in stack
    def totalElement(self):
        return len(self.stacks)


    #function to display the stack
    def display(self):
        return self.stacks
            

#driver code
def main():
    stk=stack()
    stack.size=int(input("Enter the Size of Stack: "))

    print('\n***********************************************************************************************')
    #for menu Driven
    while True:
        
        print("1. Add Student detail \n2. Remove Student detail \n3. See last entered student detail")
        print("4. See all student Detail\n5. To see Total number of Student\n6. Exit")
        option=input('Choose One option from above: ') #asking option from user
        print('\n***********************************************************************************************')

        if option=='6': exit()      #to exit program
        
        #to push detail of student to stack
        elif option=='1':
            stu=student(input("Enter the Student Name: "),int(input("Enter the Student RollNo.: ")))
            re=stk.push(stu)    #store return value of push function
            if not re:
                print("\nStack is Full!! Can't Push more student detail")
            else:
                print(f"\nAdded: \n{re}")

        #to pop element from stack  
        elif option=='2':
            print(f"Removed: \n{stk.pop()}")
        
        #to peek stack
        elif option=='3':
            print(f"Last entered student detail: \n{stk.peek()}")

        #to print to all student
        elif option=='4':
            print("Student Details:")
            
            #loop to print details
            for i in stk.display():
                print(i)

        #to see total number of student
        elif option=='5':
            print(f"Total Student: {stk.totalElement()}")

        #for invalide choice
        else:
            print("Enter the Invalid Option!!")

        print('\n***********************************************************************************************')

if __name__=="__main__":
    main()