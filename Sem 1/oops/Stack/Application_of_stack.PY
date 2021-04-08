class stack:
    #constructor
    def __init__(self):
        self.stacks=[]
        
    #Function to push element in stack
    #paramater: element which is push to stack
    #return nothing
    def push(self,element):  
        #push element to stack
        self.stacks.append(element)

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

#in class stackApplication whenever is stk is used there stk is object of class stack which is used to use the function of class stack
class stackApplication:
    #constructor
    def __init__(self,exp,varDict=dict()):
        self.exp=exp.replace(" ","")
        self.postfixed='' #empty string that will contain resultant postfix expression
        self.varDict=varDict #dict containing variable values

    #function to check parenthesis in expression
    #return bool value like True or False
    def checkParenthesis(self,stk):
        #iterating in expression
        for i in self.exp:
            #if bracket start push bracket to stack
            if i in '([{':
                stk.push(i)
            
            #if bracket close then check if last element of stack conatin same type of open bracket
            #ex: if close is ')' then if check if oprn bracket is '(' if yes then it pop '('
            # return false if close and open bracket not same type
            elif i==')':
                if stk.totalElement()==0:return False
                if stk.peek()=='(':stk.pop()
                else: return False
            elif i==']':
                if stk.totalElement()==0: return False
                if stk.peek()=='[': stk.pop()
                else: return False
            elif i=='}':
                if stk.totalElement()==0: return False
                if stk.peek()=='{': stk.pop()
                else: return False
            
        #check if stack is empty or not if empty then return true othewise return false
        if stk.totalElement()==0: return True
        else: return False
    
    #function to convert infix to postfix
    #return postfix expression
    def infixToPostfix(self,stk):
        #dict contain Precedence order
        pre={'{':1,  '}':1,  '[':1,  ']':1,  '(':1,  ')':1,
        '+':2,  '-':2,  '*':3,  '/':3,  '%':3,  '@':3,  '^':4
        }
        #iterating in expression
        for i in self.exp:
            #when i is number or char add it to postfixed string
            if i.isalpha():
                self.postfixed+=i
            #when i is opening bracket add it to stack
            elif i in '([{':
                stk.push(i)
            #when i is closing bracket
            elif i in ')]}':
                #pop element from stack
                topElement=stk.pop()
                #asign bracket for while loop
                if i==')': bracket='('
                elif i==']': bracket='['
                elif i=='}': bracket='{'

                #while loop to add  operator to postfixed string
                while topElement!=bracket:
                    self.postfixed+=topElement
                    topElement=stk.pop()
            else:
                #loop for adding opertaor to string from stack
                while (not stk.totalElement()==0) and (pre[stk.peek()] >= pre[i]):
                    self.postfixed+=(stk.pop())
                #push operator to stack
                stk.push(i)
        #loop to add remain operator to postfixeed string
        while not stk.totalElement()==0:
            self.postfixed+=stk.pop()
        
        return self.postfixed

    #function to evaluate the postfix expression
    #return result of postfix expression
    def evaluatePostfix(self,stk):
       #iterating in expression
        for i in self.exp:
            #if i is number
            if i.isalpha():
                stk.push(i)
            #when i is operator
            elif i in '+-*/%^@':
                if i=="^":i='**'
                elif i=='@': i='//'
                try:
                    temp=stk.pop()                  # pop element from stack and storing it into tempary variable
                    if temp.isnumeric(): a = temp   #check if temp is number if yes then assign that number to a
                    else: a=self.varDict[temp]      #if temp is not number fetch its value from dict
                    
                    temp=stk.pop()                  # pop element from stack and storing it into tempary variable
                    if temp.isnumeric(): b=temp     #check if temp is number if yes then assign that number to b
                    else: b=self.varDict[temp]      #if temp is not number fetch its value from dict
                    stk.push(str( eval( b + i + a ) ))
                except:
                    return "Expression is incorrect!!!"
        #when there is insufficient number of ooperator
        if stk.totalElement()>1 or (not stk.peek().isnumeric()):
            return "Exprssion is incorrect!!!"
        else:
            return stk.pop()

#driver code
def main():
    while(True):
        print('\n***********************************************************************************************')
        #Displaying what operations this program can perform
        print('-->To check parenthesis Enter 1 \n-->To Convert Infix to Postfix Enter 2 \n-->To Evaluate Postfix Expression Enter 3 \n-->For Exit Enter 4')
        option=input('Enter Your choice : ') #user choice to perform an operation
        print('\n***********************************************************************************************')
        if option in '1234': #checking if option is valid
            if option=='4': #when exit option is selected
                exit()

            #taking expression from user only char and variable if number is enter loop repeat until exp without number enter
            while(True):
                print("Note:Reminder use '%' , Division(for decimal answer) use '/' ")
                print("Division(without decimal answer) use '@' , Exponentiation ---> '^'")
                exp=input('\nEnter the expression in varaible(donot use number)\n')
                for x in exp:
                    flag=True
                    if x.isnumeric():
                        flag = False
                        break
                if flag==True:
                    break
            
            print('\n***********************************************************************************************')
            #create object of stack class
            stk=stack()

            if option=='1':
                operation=stackApplication(exp)
                #calling function to check parentesis are missing or not
                if operation.checkParenthesis(stk)==True:
                    print('\nParentisis are correct')
                else:
                    print('\nParentisis are missing!!')

            elif option=='2':
                operation=stackApplication(exp)
                if operation.checkParenthesis(stk)==False:
                    print('\nParentisis are missing')
                else:
                    #calling function to convert infix to postfix
                    print("\nPostfix expression:\n",operation.infixToPostfix(stk))

            elif option=='3':
                #taking value of variable
                varDict=dict()
                print('Enter the values of variables:\n')

                #iterating in expression
                for i in exp:
                    if i not in varDict:
                        if i.lower()>='a' and i.lower()<='z':
                            varDict[i]=input(f'{i}: ')
                        
                operation=stackApplication(exp,varDict)
                #calling function to evalute function
                result= operation.evaluatePostfix(stk)
                print(f"Result of {exp} is \n {result}")
        else:
            print("Invalid option!! try again")

if __name__=="__main__":
    main()