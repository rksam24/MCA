#Program to implement Binary search ( Iterative).

#function for binaary search
def binarySearch_iteration(list1,number):
    low=0 #lowerst index
    high=len(list1)-1 #highest index
    mid=0 #middle index of list

    #loop for binary search
    while low<=high:
        mid=low+high//2
        if number==list1[mid]:#if number is at mid index then return that index
            return mid
        #if number is not at mid index check if mid number is larger or small 
        elif number>list1[mid]:
            low=mid+1
        else:
            high=mid-1
    return False #return false when number not find

#program start from here
print('Enter the numbers with space')
#taking number from user as input
list1=[int(i) for i in input().split()]
print(list1)

#sort the list
list1.sort()
print('After sort the list')
print(list1)

number=int(input('Enter the number'))

#calling function for bianry search 
x=binarySearch_iteration(list1,number) #x is index of number search
#print the statement if its found in list or not
if x==False:
    print('Number is not present')
else:
    print('Number is present at index',x)