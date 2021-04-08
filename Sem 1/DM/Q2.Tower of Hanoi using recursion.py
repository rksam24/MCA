#Program to implement tower of Hanoi Recursive
''''
source: where all disk
destination: where disk have to move
auxiliary: only to help move disk from source to distination
'''

#funtion for tower of hanoi
def TowerOfHanoi(n , source, destination, auxiliary): 
    if n==1: 
        print("Move disk 1 from source",source,"to destination",destination )
        return
    else:
        TowerOfHanoi(n-1, source, auxiliary, destination) 
        print("Move disk",n,"from source",source,"to destination",destination)
        TowerOfHanoi(n-1, auxiliary, destination, source) 
          
# program excute from here
n=int(input('Enter thw number of disks: ')) #taking input from user for number of disk
TowerOfHanoi(n,'A','B','C')  # call the function to print move of tower of honoi for n disk