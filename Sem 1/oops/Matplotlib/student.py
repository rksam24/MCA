import matplotlib.pyplot as plt
import numpy as np


class student:

    def __init__(self,name,subject):
        self.name=name
        self.marks=[]
    
    #function to get marks from user
    def getmarks(self):
        for i in range(5):
            self.marks.append(int(input(f'Enter marks in subject {i+1} : ')))


def main():

    #taking input from user
    subjects=['OOPS','CSA','MTCS','DM','TC']
    #list containing objectname of class student
    obj=[]
    #loop to create object name for student class
    for i in range( int( input('Enter number of student: ') ) ):
        obj.append('stu'+str(i))
    
    stack=[]    #create stack to store object
    for i in obj:
        #asking student name from user
        i=student(input("Enter the name of student: "),subjects)
        #qtaking marks of student
        i.getmarks()
        #push object to stack
        stack.append(i)
    
    while True:
        #asking for student name for student detail
        studentName=input('Enter the student name to Get Detail: ')

        #iterating through object
        for i in stack:

            #when student name found
            if i.name==studentName:
                #creating numpy array for bar chat
                x=np.array(subjects)
                y=np.array(i.marks)

                #to use in legend
                colors={'OOPS':'pink','CSA':'red','MTCS':'green','DM':'blue','TC':'gold'}
                labels=list(colors.keys())
                handles = [plt.Rectangle((0,0),1,1, color=colors[label]) for label in labels]

                #color for differenet subject
                c=['pink','red','green','blue','gold']

                #creating bar chart
                plt.bar(x,y,width=0.6,color=c)

                #for label
                plt.ylabel("Marks")
                plt.xlabel("Subjects")
                
                #for title of graph
                plt.title(studentName.capitalize())

                plt.legend(handles,labels)
                
                #to show bar graph
                plt.show()

                break
        #when want exit loop
        if input('For Exit Enter --> Exit otherwise Press Enter: ').lower()=='exit':
            break
    
if __name__=="__main__":
    main()