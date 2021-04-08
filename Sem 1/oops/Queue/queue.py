'''Queue class 
   Variables:
            --> simpleQueue             a list to store elements
            --> circularQueue           queue when reach at end try to add element then at start if position is if then add element there
            --> rear                    initially -1
            --> front                   initially -1
            --> size                    to store size of queue
   Functions:
            --> __init__                    constuctor
            --> enqueueSimpleQeue           to add element in circular queue
            --> dequeueSimpleQueue          to remove element in circular queue
            --> enqueueCircularQueue        to add element in circular queue
            --> dequeueCircularQueue        to remove element in circular queue
            --> TotalElement_SimpleQueue    to return total number of element in simple queue
            --> TotalElement_CircularQueue  to return total number of element in circular queue
            --> display                     to display queue
'''
class Queue:

    #constructor
    def __init__(self,size=0):
        self.simpleQueue=[]
        self.circularQueue=[None for _ in range (size)]
        self.rear=-1
        self.front=-1
        self.size=size
            
    #function to enqueue simple queue --> return enqueue element
    def enqueueSimpleQeue(self,element):
        #when queue is full
        if len(self.simpleQueue)==self.size:
            return "Queue is Full!! can't Enqueue"
        else:
            self.simpleQueue.append(element)
            return element

    #function dequeue simple queue  --> return dequeue element
    def dequeueSimpleQueue(self):
        #when queue is empty
        if len(self.simpleQueue)==0:
            return "Queue is empty!! can't Dequeue"
        else:
            return self.simpleQueue.pop(0)

    #function to get number of element in simple queue -->return number of element in queue
    def TotalElement_SimpleQueue(self):
        return len(self.simpleQueue)
    
    #function to enqueue in circular queue --> return enqueue element
    def enqueueCircularQueue(self,element):
        #when rear is more than size
        if self.rear>self.size-1:
            return "Queue is Full!! Can't add more element"
        
        #when queue is empty
        elif self.front ==-1 and self.rear==-1:
            self.rear=0
            self.front=0
            self.circularQueue[self.rear]=element
        
        #when rear is size-1 and front is not at 0 postion
        elif self.rear==self.size-1:
            if self.front!=0:
                self.rear=0
                self.circularQueue[self.rear]=element
            else:
                return "Queue is Full!! can't add more element"
        
        else:
            if self.circularQueue[self.rear+1]==None:
                self.rear+=1
                self.circularQueue[self.rear]=element
            else:
                return "Queue is Full!! can't add more element"

        return element
    
    #function to dequeue circular queue --> return dequeue element
    #temp is temporary variable to store value temporary
    def dequeueCircularQueue(self):
        #when didn't enqueue single time i.e when queue is empty
        if self.front==self.rear==-1:
            return "Queue is Empty!! can't Dequeue"

        #when front is size-1 and when rear=0
        elif self.front>=self.size-1 and self.rear!=0:
            temp=self.circularQueue[self.front]
            self.circularQueue[self.front]=None
            self.front=0
        
        #when front is at size -1 position and rear is at  position
        elif self.front>=self.size-1 and self.rear==0:
            temp=self.circularQueue[self.front]
            self.circularQueue[self.front]=None
            self.front=0

        else:
            #when queue is not empty
            if self.circularQueue[self.front]!=None:
                temp=self.circularQueue[self.front]
                self.circularQueue[self.front]=None
                self.front+=1

            else:
                return "Queue is empty!!"
        return temp

    #function to get total number of element in queue --> return total numbers of element in queue
    #count -- contain total number of element in queue
    def TotalElement_CircularQueue(self):
        count=0
        for i in self.circularQueue:
            if i != None: count+=1
        return count 

    #function to display simple queue --> return simple queue
    def displaySimpleQueue(self):
        return self.simpleQueue
    
    #function to display circular queue --> return circular queue
    def displayCircularQueue(self):
        Queues=''   #temp variable to store queue element
        if self.TotalElement_CircularQueue()==0:
            return False
        elif self.rear>=self.front:
            for i in range(self.front,self.rear+1):
                Queues=Queues+' '+self.circularQueue[i]
        else:
            for i in range(self.front,self.size):    
                Queues=Queues+' '+self.circularQueue[i]
            for i in range(self.rear+1):
                Queues=Queues+' '+self.circularQueue[i]
        return Queues

#driver code
#main function containg menu driven --> return nothing
def main():    
    while True:

        while True:
            print("\nFor Simple Queue Enter --> 1\nFor Circular Queue Enter --> 2\nFor Exit -->3")
            queueOption=input("Enter one option from above: ")  #taking option from user
            print('\n**********************************************************************************************************')
            if queueOption=='3':exit()
            elif queueOption=='1' or queueOption=='2': break      #if valid option
            else: print("Invalid option!! Enter Valid Option")

        que=Queue(int(input("\nEnter the size of Queue: ")))
            
       
        while True:
            print('**********************************************************************************************************')
            print('\nFor Enqueue Enter --> 1\nFor Dequeue Enter --> 2\nFor Display Enter 3\nFor Total Element in queu Enter -->4\nFor back --> 5')
            operation=input("Enter one option from above: ")

            print('**********************************************************************************************************')

            #menu drive
            #for exit from program
            if operation=='5':break

            #for equeue--> calling function to enqueue element
            elif operation=='1':
                if queueOption=='1':
                    #calling function to enqueue element
                    print(f"\nEnqueue --> '{que.enqueueSimpleQeue(input('Enter the Enqueue Element: '))}'")
                else:
                    print((f"\nEnqueue --> '{que.enqueueCircularQueue(input('Enter the Enqueue Element: '))}'"))

            #for dequeue  --> calling function to dequeue
            elif operation=='2':
                if queueOption=='1':
                    print(f"\nDequeue --> '{que.dequeueSimpleQueue()}'")
                else:
                    print(f"\nDequeue --> '{que.dequeueCircularQueue()}'")

            #for display --> calling function to display queue
            elif operation=='3':
                if queueOption=='1':
                    print("\nQueue Element: ")
                    print( *que.displaySimpleQueue(),sep=' , ')
                else:
                    queuee=que.displayCircularQueue()
                    if queuee==False:
                        print("Queue is Empty!!")
                    else:
                        print("\nQueue Element \n",queuee)

            #to get number of element in queue
            elif operation=='4':
                if queueOption=='1':
                    print(f"\nTotal Element in Queue: {que.TotalElement_SimpleQueue()}")
                else:
                    print(f"\nTotal Element in Queue: {que.TotalElement_CircularQueue()}")

            else:
                print("\nInvalid Option!! Enter vaild option")

if __name__=="__main__":
    main()