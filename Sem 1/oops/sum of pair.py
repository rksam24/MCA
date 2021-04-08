"""
program to take 'n' numbes from the user and a number 'm '. and find all possible
pair of numbers from inputted 'n' number that sum up to m
eg: i/p: n=5
5 number are 10,30,8,23,1
m=31
o/p:[30,1] and [8,23]

"""
def main():
    n=int(input('How many number need: '))#take numbers of value in list from user
    m=int(input('Enter Sum of pairs: '))#take total sum of pair from user
    print('Enter the',n,'nummbers')#print statement
    numbers=[]#create empty list to enter numbers
    for i in range(n):#loop to enter number in list
        numbers.append(int(input()))#take input from user and add to the list
    print()
    print(n,'Numbers are:',numbers)#print the number user give input
    sumOfPair(numbers,m)#calling number to print pair

def sumOfPair(numbers,m):
    ''' purpose: this function is desigen to find pair for m sum from
number user give
input:
    numbers: take list as input, list contain input number from user
    m:sum of pair
output:
    print pair with total sum m
'''
    pair=[] #create a list which will contain pair
    for i in range(len(numbers)): #loop to find out the pair       
        for j in range(i + 1, len(numbers)): #inner loop to findout the pair
            temp=[] #create a temporary list
            if numbers[i] + numbers[j] == m:
            # check the condition to findout two number is list equal to sum given by user
                temp.append(numbers[i]) #add first number to temporary list
                temp.append(numbers[j])#add second number to temporary list
                if temp not in pair: #check temp list in pair list or not
                    if temp[::-1] not in pair:
                        #check reverse of temp list is in pair list eg: temp=[1,2] then check for [2,1]
                        pair.append(temp)#add whole temp list to pair list
    print('All Possible pair with sum',m,'are:')  # print statement  
    print(*pair)#Print pairs
  
main()
