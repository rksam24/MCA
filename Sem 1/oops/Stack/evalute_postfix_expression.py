class stack:
    #constructor
    def __init__(self):
        self.stacks=[]
        
    #Function to push element in stack
    #ele is element which is push to stack
    #return nothing
    def push(self,ele):  
        #push element to stack
        self.stacks.append(ele)


    #function to pop the last/top element of stack
    #return pop element
    def pop(self):
        #when stack is empty return False
        if len(self.stacks)==0:
            return False
        else:
            return self.stacks.pop()
    
    #function to peek top element of stack
    #return the top element of stack
    def peek(self):
        #when stack is empty
        if len(self.stacks)==0:
            return False
        else:
            return self.stacks[-1]

    #function to findout number of element in stack
    #return the total number of element in stack
    def totalElement(self):
        return len(self.stacks)

class expression:
    #constructor
    def __init__(self,exps):
        self.exps=exps.replace(" ","")
    
    #function to evalulate postfix expression
    #stk (is object of class stack) is used to use function of class stack 
    def evaluatePostfix(self,stk):
        #looping in expression
        for i in self.exps:
            #if i is number
            if i in "0123456789":
                stk.push(i)
            #when i is operator
            elif (i in '+-*/%') or i =='**' or i=="//":
                try:
                    a=stk.pop()
                    b=stk.pop()
                    stk.push( str( eval(b+ i +a ) ) )
                except:
                    return "Expression is incorrect!!!"
        #when there is insufficient number of ooperator
        if stk.totalElement()>1:
            return "Exprssion is incorrect!!!"
        else:
            return stk.pop()

#driver code
def main():
    exps=input('Enter the expression(in number) in postfix order:\n')
    stk=stack()
    exp=expression(exps)
    result= exp.evaluatePostfix(stk)
    print(f"Result of {exps} is \n {result}")

main()