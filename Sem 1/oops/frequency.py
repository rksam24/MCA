'''
program to
a. to count frequency of items in a given list and return the frequency.
b. In a, also return the position of each item in the given list
'''

def main():
    n=int(input('Enter number of element in list'))#Taking input for number of element in list
    list1=[]#create empty list
    print('Enter the element in row: ')#print statement
    for i in range(1,n+1):#loop for list
        list1.append(int(input()))#taking input from user than append it to list
    print('List=',list1)#print the list
    print('Number \t Frequency \t Position')#print statement
    a=freq(list1)#calling function for frequence of number assign it variable a
    b=position(list1)#calling function for position of number assign it variable b
    for x,y in a.items():#loop for print frequence and position
        print(x,'\t',y,end='\t')#print number and frequence
        if x in b:#checking condition
            print('\t',b[x])#print postion of number
    

def freq(list1):
    ''' purpose: this function is design to create a list to find out frequence of number
input:
   list1:taking list containing number
output:
    return dictionary containing frequence of number
eg:i/p: [1,1,2,3,3]
o/p:
{1:2,
2:1,
3:2}
'''
    dict1={
        }#create empty dictionary
    for i in list1:#loop to find out frequence of number
        if i not in dict1:#checking of item of list is not in dict as key 
            dict1[i]=1#ading key and value(update) dict
        else:
            dict1[i]=dict1[i]+1#if item in dict then updating its value
    return dict1 #return the dict1

def position(list1):
    ''' purpose: this function is design to create a list to find out positions of number
input:
   list1:taking list containing number
output:
    return dictionary containing positions of number
eg:i/p: [1,1,2,3,3]
o/p:
{1:1,2
2:3,
3:4,5}
'''
    dict2={
        }#create the empty dict
    for i in range(len(list1)):#loop for findout the postions of number
        x=i+1#add 1 to index of list and assign it to x
        y=list1[i]#assign item of list at index i to y
        if y not in dict2:#checking if item of list is not in dict as key
            dict2[y]=[]#update the dict. y is key and [] is list which is value of key y
            dict2[y].append(x)#append the list
        else:
            dict2[y].append(x)#if item of list in dict as key then append the list at that key
    return dict2#return the dict2   
        

main()
