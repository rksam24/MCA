#Program to findout Union and Intersection of two given set

def main():
    print('Enter the value for set1:')
    #taking input for first set
    set1={i for i in input().split()}
    print('set1=',set1)

    print('Enter the value of set 2:')
    #taking input for second set
    set2={i for i in input().split()}
    print('set2=',set2)
    
    #print the union and intersection of two given set
    print('\nUnion of set1 and set 2:',set1.union(set2))
    print('Intesection of set1 and set2:',set1.intersection(set2))

main()