#Read the file created in step 1, generate the marksheets of individual student and save it in a file named <studentName_rollno>.

import pickle
def main():
    marksFile= open('student_record','rb') #open the file
    data=pickle.load(marksFile)
    #loop to call function to create marksheet for each student
    for name in data:
        rollno=data[name]['RollNo'] #rollno contain rollno of student
        fileName=name+'_'+str(rollno)+'.txt' #create name of file of markssheet for each student
        createMarksheet(fileName,name,rollno,data[name]) #calling the function to create marksheet 
        print(fileName,'is created')
    marksFile.close() #close the file

'''
function to create marksheet for each student
parameter and function use in function
fileName: name of file opened
name: name of student
rollno: rollno of student
marks: dict contain marks of student
'''
def createMarksheet(fileName,name,rollno,marks,mode='wt'):
    marks.pop('RollNo')#pop the rollno so that its don't write twice
    with open(fileName,mode) as markSheet:#open the file
        markSheet.write('\t\tMarks Sheet\n\tName:')
        markSheet.write(name)#write the name
        markSheet.write('\tRoll No.:')
        markSheet.write(str(rollno))#write rollno
        markSheet.write('\n\t------Marks-----\n')
        markSheet.write('\tSubject\t\tMarks\n')
        for subject in marks:#loop for write marks in marksheet
            markSheet.write('\t')#for tab space
            markSheet.write(subject) #write the subject name 
            markSheet.write('\t\t')#for tab space
            markSheet.write(str(marks[subject])) #write marks for parcticular subject
            markSheet.write('\n')#for enter

main()