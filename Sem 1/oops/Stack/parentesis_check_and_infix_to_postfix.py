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
        self.exps=exps
        self.postfixed=''

    """function to check parenthesis in expression
    parameters:
    stk object of class stack
    exp is expression taking form user like a+b+(c)
    return bool value like True or False
    """
    def checkParenthesis(self,stk):
        #looping in expression
            for i in self.exps:
                #if bracket start push bracket to stack
                if i == '(' or i=='[' or i=='{':
                    stk.push(i)
                
                #if bracket close then check if last element of stack conatin same type of open bracket
                #ex: if close is ')' then if check if oprn bracket is '(' if yes then it pop '('
                # return false if close and open bracket not same type
                elif i==')':
                    if stk.totalElement()==0:
                        return False
                    if stk.peek()=='(':
                        stk.pop()
                    else:
                        return False
                elif i==']':
                    if stk.totalElement()==0:
                        return False
                    if stk.peek()=='[':
                        stk.pop()
                    else:
                        return False
                elif i=='}':
                    if stk.totalElement()==0:
                        return False
                    if stk.peek()=='{':
                        stk.pop()
                    else:
                        return False
            
            #check if stack is empty or not if empty then return true othewise return false
            if stk.totalElement()==0:
                return True
            else:
                return False
    
    #function to convert infix to postfix
    #stk is object of class stack
    #return postfix expression
    def infixToPostfix(self,stk):
        #dict contain Precedence order
        pre={'{':1,  '}':1,  '[':1,  ']':1,  '(':1,  ')':1,
        '+':2,  '-':2,  '*':3,  '/':3,  '%':3,  '@':3,  '^':4
        }
        self.exps=self.exps.replace(" ","")
        #looping through expression
        for i in self.exps:
            #when i is number or char add it to postfixed string
            if (i>='0' and i<='9') or (i.lower()>='a' and i.lower()<='z'):
                self.postfixed+=i
            #when i is opening bracket add it to stack
            elif i=='(' or i=='[' or i=='{':
                stk.push(i)
            #when i is closing bracket
            elif i==')' or i==']' or i=='}':
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

#driver code
def main():
    exps=input('Enter the expression\n')
    stk=stack()
    exp=expression(exps)
    #calling function to check parentesis are missing or not
    if exp.checkParenthesis(stk)==True:
        print('Parentisis are correct')
    else:
        print('Parentisis are missing!!')
        exit()

    print("\nPostfix expression:\n",exp.infixToPostfix(stk))

main()