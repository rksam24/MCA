import pickle
import os

def writeFile(fileName,arr,mode='w'):
    with open(fileName,mode) as file:#open the file
        str1=' '
        for i in arr:
            str1=str1+str(i)+' '
        file.write(str1) 
    with open(fileName,'r') as file:
        data=[int(i) for i in (file.read()).split()]
        print(data)
        print(type(data))
        for i in data:
            print(i)

list1=[1,2,3,4,5,6,10]
writeFile('abc.txt',list1)