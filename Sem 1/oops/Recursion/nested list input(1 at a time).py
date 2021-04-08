def fun():
    m=int(input('\nEnter number of element'))
    print('Enter the element of list')
    list2=[]
    for j in range (m):
        nli=input()
        if nli=='[':
            list2.append(fun())
            print('Nested list end')
            print('\nEnter the outer list element again')
        else:
            list2.append(nli)   
    return list2

print('Note: To add list as element in list press [ and press enter ')
list1=fun()
print('\nlist',list1)



n=input()
list1.pop(n)
print(list1)