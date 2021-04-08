"""Program to take a number as an input and create a list of n list such that
ith list contain first five multiple of i
"""
def main():
    n=int(input('Enter the Length of List: '))#take length of list as input from user
    outputList(n)#calling the function to print the list
    matrix1=[[j*i for j in range  (1 , 6)] for i in range (1 , n+1)]
    print(matrix1)
    
def outputList(n):
    ''' purpose: this function is design to create a list such that
ith list contain first five multiple of i 
list
input:
   n:length of string
output:
    return the desire list
eg:
eg:i/p: Enter the length of list:3
o/p:
list is [[1,2,3,4,5],[2,4,6,8,10],[3,6,9,12,15]]
'''
    #first way
    list1=[] # create a list
    for i in range(1,n+1):#loop for create list of n length
        temp=[] #create temporary list to create list within list
        for j in range (1,6):
        #loop for list with list such that ith list contain first five multiple of i 
            temp.append(i*j) #add values to temp list
        list1.append(temp)# append temp list into list list1
    print(list1) #print desire list
    #second way
    list2=[[j*i for j in range  (1 , 6)] for i in range (1 , n+1)]
    '''first for start with i have range (1 to n) then it go to list part where
first for loop start with j range have (1,6) and then append i*j to list then
 list2 append that list
    '''
    print(list2)
    
    

main()
