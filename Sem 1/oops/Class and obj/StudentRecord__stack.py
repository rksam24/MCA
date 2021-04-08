class student:
    #constructor
    def __init__(self,name,rollNo):
        self.name=name
        self.rollNo=rollNo

    #defining __str__()
    def __str__(self):
        return 'Name: '+self.name+', Roll NO: '+str(self.rollNo)
    
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
    def pop(self):o
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
            

#driver code
def main():
    #list containing objectname of class student
    obj=[]
    #loop to create object name for student class
    for i in range( int( input('Enter number of student: ') ) ):
        obj.append('stu'+str(i))

    #create stk (object) of class stack
    stk=stack()
    #taking size of stack from user
    stack.size=int( input('Enter the size of stack: ') )

    #loop to creates objects of class student and push it to stack
    for i in obj:
        i=student(input('\nEnter the name: '), int( input('Enter the Roll No.: ') ))

        #calling function to push element to stack
        push=stk.push(i)
        #if stack is full print the statement in if block
        if push==False:
            print("Stack is full!! can't add more student record")
        else:
            #when stack is not full
            print('Pushing element in stack  -----> {} '.format(push) )

    #poping the element from stack
    print("\nPopping element -----> '{}' is popped".format( stk.pop() ))
    print("Popping element -----> '{}' is popped".format( stk.pop() ))

    #peeking top element of stack
    print("\n Top element in stack -----> '{}' is the top element ".format( stk.peek() ))

    #calling function for total number of element in stack
    print("\nTotal elements in stack -----> {}".format( stk.totalElement() ))

main()