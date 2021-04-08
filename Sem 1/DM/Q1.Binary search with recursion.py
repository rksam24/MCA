#low = lower index, high=highest index
def binarySearch_recursive(list1,low,high,number):
    if high>=low:
        mid=(low+high)//2
        if list1[mid]==number:
            return mid
        elif list1[mid]>number:
            return binarySearch_recursive(list1,low,mid-1,number)
        else:
            return binarySearch_recursive(list1,mid+1,high,number)

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
x=binarySearch_recursive(list1,0,len(list1)-1,number)
if x==False:
    print('Number is not present')
else:
    print('Number is present at index',x)