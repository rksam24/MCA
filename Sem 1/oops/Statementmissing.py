#Function to take input marks of students in list ‘marksList’ with total strength ‘numStudent’
def inputMarks(numStudents):
    marksList=list() 
    for i in range(numStudents):
        m1=int(input("Enter marks for student "+str(i+1)+":"))
        marksList.append(m1) #STATEMENT 1- append the input from user to marksList
    return marksList


#Function to validate the input marks i.e. marks should be between 0 to 100.
#returns TRUE if list of marks is valid otherwise returns FALSE
def validateMarks(marks):
    for i in marks: # Traverse each element
        if i<=0 and i>=100:#STATEMENT 2
            return False
        return Tu
        


#Main Script
TotalMarks=[]
numStudents=int(input("Enter Total Number of students:"))
print("Enter Marks for 1st subject")
marks1=inputMarks(numStudents)
print("Enter Marks for 2nd subject")
marks2=inputMarks(numStudents)

if validateMarks(marks1) or validateMarks(marks2)==False:  #checking marks is more than 100 then its not valid
    print("Invalid Marks")
else:
    for i in range(numStudents):
        TotalMarks.append(marks1[i]+marks2[i])
    print(TotalMarks)
