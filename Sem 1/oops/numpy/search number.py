import numpy as np
import os

def main():
    fileName=input('Enter the file name: ')+'.txt'
    
    print('Choose one option\n1.use exist file\n2.Create new file\n3.Exit')
    choice=input('Enter the choice from above: ')
    while True:
        if choice=='1':
            arr=readFile(fileName)
            print(arr)
            break
        if choice=='2':
            arrays=np.array([int(i) for i in input('Enter the number with spaces: ').split()])
            writeFile(fileName,arrays)
            arr=readFile(fileName)
            break
        if choice=='3':
            exit()
        else:
            print('Invalide Option try again!!')
    num=int(input('Enter the Number you wants to Search: '))
    result=search(arr,num)
    if result==False:
        print('Number not found!!')
    else:
        print('Number {} found at postion {}'.format(num,result))
        
def writeFile(fileName,arr,mode='w'):
    if(os.path.exists(fileName)):                    # checking if file exists
        print("\nfile already exists!!!!\n")
        exit()
    else:
        with open(fileName,mode) as file:#open the file
            np.savetxt(file,arr)#write the detail in file 
            


def readFile(fileName,mode='r'):
    try:                                                    #try block if error occur execute except block
        with open(fileName,mode) as file:        #open the file
                data=np.loadtxt(file)                        #read the file
                return data                                 #return data of file
    except FileNotFoundError:                               #if error occur in try block it execute
        print('File not exit/found')
        exit()

def search(arr,num):
    position=1
    for i in arr:
        if i==num:
            return position
        else:
            position+=1
    return False

if __name__ == '__main__':
    main()