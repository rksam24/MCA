#deepcopy
def copy1(list1,l,list2=list(),i=0):
    if i>l:
        return list2
    elif type(list1[i]) is list:
        list2.append(copy1(list1[i],len(list1[i])-1,list2=list(),i=0))
        i=i+1
        return copy1(list1,l,list2,i)
    else:
        list2.append(list1[i])
        i=i+1
        return copy1(list1,l,list2,i)


def main():
    list1=[1,2,3,[4,5,6],7]
    
    maxIndex=len(list1)-1
    print('List1=',list1)
    list2=copy1(list1,maxIndex)

    
    print('List2=',list2)
    list1[2][1]='a'
    
    
    print('\nAfter change the list1')
    print('List1=',list1)
    print('List2=',list2)
    #loop
    
main()
