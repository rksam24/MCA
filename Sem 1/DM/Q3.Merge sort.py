#program for recurrence relation T(n)=2T(n/2)+1. i.e. Merge Sort

import math

#function to merge the two sub list
def merge(left_numList,right_numList,numLIst):
    i=0
    j=0
    k=0

    #merging two sub list
    while i<len(left_numList) and j<len(right_numList):
        if left_numList[i]<right_numList[j]:
            numLIst[k]=left_numList[i]
            k=k+1
            i=i+1
        else:
            numLIst[k]=right_numList[j]
            k=k+1
            j=j+1
    
    while i <len(left_numList):
        numLIst[k]=left_numList[i]
        i=i+1
        k=k+1
    
    while j<len(right_numList):
        numLIst[k]=right_numList[j]
        j=j+1
        k=k+1

    return numLIst

#function for merge sort
def mergeSort(numList):
    if len(numList)>1:
        #find mid od list
        mid= len(numList)//2

        #dividing numList into subList containg half element each
        left_numList=numList[:mid]
        right_numList=numList[mid:]

        #calling function to sort both halves
        mergeSort(left_numList)
        mergeSort(right_numList)

        #calling function to merge to halves
        merge(left_numList,right_numList,numList)

        #returning sorted numLIst
        return numList

#function to find complexity using master theorm
def complexity():
    print("\nComplexity for T(n)=2T(n/2)+1 i.e merge sort is")
    a=2
    b=2
    k=0
    p=0

    log=int( math.log(a,b) )

    #applying master thoerm
    if a>b**k:
        print(f"T(n)= O( n^{log} )" )
    elif a==b**k:
        if p>-1:
            print(f"T(n)= O( n^{log} * ( log(n) )^{p+1} ) ")
        elif p==-1:
            print(f"T(n)= O( n^{log} * log(log(n))) )")
        elif p<-1:
            print(f"T(n)= O( n^{log} ) ")
    elif a<b**k:
        if p>=0:
            print(f"T(n)= O( n^{k} * ( log(n) )^{p} )")
        elif p<0:
            print(f"T(n)= O( n^{k} ) ")

#driver code
def main():
    #taking numbers form user
    
    while True:
        try:
            numList=[int(i) for i in input("Enter the numbers with space\n").split()]
            break
        except:
            print("Enter the Number!!")
    
    print(f"\nBefore Sort \n{numList}")

    print("\nAfter Merge Sort:")
    #calling function for merge sort
    print(mergeSort(numList))

    #calling function to get complexity
    complexity()

if __name__=="__main__":
    main()