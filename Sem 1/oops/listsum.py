def sumTwoNum(x,y):
    z=x+y
    return z

def sumList(list1,list2): #function for sum of element of list
    listSum=[]#create empty list
    for i in range(len(list1)):#loop for sum of element of list
        z=sumTwoNum(list1[i],list2[i])#calling function to sum element
        listSum.append(z)#append sum of element of list to new list
    return listSum #return list

n=int(input('Enter the length of list')) #input for length of list
print('enter element of list1')
list1=[int(input()) for x in range (n) ]#taking input list from user
print('enter element of list')
list2=[int(input()) for x in range (n)]#taking input list from user


print('Sum of element of list=',sumList(list1,list2))#print the result list

