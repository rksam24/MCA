#1. Create a file containing records of the students marks in each subject. 

import pickle #import the pickle libary

def main():
    details=studentDetails() #calling function to get student detail like name roll no, marks
    fileName='student_record' #filename
    studentRecord(fileName,details)#create file for student file
    read(fileName)

'''
function content/student detail 
parameter and variable use in function:
n: no of student
subject: list contain name of all subject
dict1: details of all student
name: name of student
rollno: rollo of student
'''
def studentDetails():
    n=int(input('Enter the number of student')) #aking number of user from user
    subjects=[sub for sub in input('Enter the Subject Name with space: ').split()] #enter the subjects
    dict1=dict() #declare dict to contain all student details
    for i in range(n):#loop to get student details
        name=input('Enter the Name of student: ')#asking name from user
        rollno=int(input('Enter the Rollno: '))#asking rollno from user
        dict2=dict()#declare dict which conatin a student detail
        dict2['RollNo']=rollno#add roll to dict
        for i in subjects: #
            print('Enter the marks of',i,end='')
            dict2[i]=int(input())#taking marks from user for each subject
        dict1[name]=dict2 #add detail for each person
    return dict1#return student details

'''
function to create file for student details
parameter and variable use in function:
fileName:name of file
content : student detail to write in file
mode: the mode in which file open
'''
def studentRecord(fileName,content,mode='wb'):
    with open(fileName,mode) as file:#open the file
        pickle.dump(content,file)#write the detail in file

def read(fileName,mode='rb'):
    with open(fileName,mode) as file:
        print(pickle.load(file))

if __name__ == '__main__':
    main()
    