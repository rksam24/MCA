class queue:
    def __init__(self,size):
        self.size=size
        self.list1=[]
        self.front=0
        self.rear=-1

    def enqueue(self,element):
        if (self.front==0 and self.rear==(self.size-1)) or  (self.rear+1==self.front and self.rear!=-1):
            print(" QUEUE IS FULL ")
            print('rear->',self.rear)
            print('front->',self.front)
        elif (self.front < self.rear and (self.rear==self.size-1)) or self.front<self.rear:
            if self.rear+1==self.size:
                self.rear=0
            else:
                self.rear+=1    
            self.list1[self.rear]=element
            
        elif self.rear>self.front:
            self.rear+=1
            self.list1[self.rear]=element       
        else:
            self.rear+=1
            self.list1.insert(self.rear,element)
            print('rear->',self.rear)
            print('front->',self.front)   
    def dequeue(self):
        if self.rear==-1 or (self.front==self.size and len(self.list1)==0) or self.rear+1==self.front :
            print("empty queue")
            self.rear=-1
            self.front=0
            print('rear->',self.rear)
            print('front->',self.front)
        elif self.rear<self.front:
            if self.front==self.size:
                self.front=0
                self.list1[self.front]=None
                self.front+=1
            else:
                self.list1[self.rear+1]=None
                self.front+=1    
        elif (self.front<self.rear and (self.rear!=self.size-1)):

            self.list1[self.front] = None 
            self.front+=1      
        else:
            self.list1[self.front]=None
            self.front+=1
            print('rear->',self.rear)
            print('front->',self.front)
    def display(self):
        print('rear->',self.rear)
        print('front->',self.front)
        print(self.list1)



def main():
    size=int(input("what is the size of queue"))
    obj=queue(size)

    size=5
    obj=queue(size)
    obj.enqueue(1)
    print(obj.display())
    obj.enqueue(2)
    print(obj.display())
    obj.enqueue(3)
    print(obj.display())
    obj.enqueue(4)
    print(obj.display())
    obj.enqueue(5)
    print(obj.display())
    obj.enqueue(6)
    print(obj.display())
    obj.dequeue()
    print(obj.display())
    obj.dequeue()
    print(obj.display())
    obj.enqueue(7)
    print(obj.display())
    obj.enqueue(8)
    print(obj.display())
    obj.enqueue(9)
    print(obj.display())
    obj.enqueue(10)
    print(obj.display())
    obj.enqueue(11)
    print(obj.display())
    obj.dequeue()
    print(obj.display())
    obj.dequeue()
    print(obj.display())
    obj.dequeue()
    print(obj.display())
    obj.dequeue()
    print(obj.display())
    obj.dequeue()
    print(obj.display())
    obj.dequeue()
    print(obj.display())
    obj.enqueue(12)
    print(obj.display())
    obj.enqueue(13)
    print(obj.display())
    obj.enqueue(14)
    print(obj.display())
    obj.enqueue(15)
    print(obj.display())
    obj.dequeue()
    print(obj.display())
    obj.dequeue()
    print(obj.display())
    obj.enqueue(16)
    print(obj.display())
    obj.enqueue(17)
    print(obj.display())
    obj.dequeue()
    print(obj.display())          
main()