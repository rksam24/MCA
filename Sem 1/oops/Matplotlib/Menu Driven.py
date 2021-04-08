import matplotlib.pyplot as plt
#class student to store name and marks of students
class student:
     #constructor
     #name --> for student name
     #OOPS,CSA,MTCS,DM,TC --> marks of each subject
    def __init__(self,name,OOPS,CSA,MTCS,DM,TC):
        self.name=name
        self.OOPS=OOPS
        self.CSA=CSA
        self.MTCS=MTCS
        self.DM=DM
        self.TC=TC
    
    #function to calculate percentage --> return percentage
    def percentage(self):
        return (self.OOPS+self.CSA+self.MTCS+self.DM+self.TC)/5


'''
function to create scatter plot --> return nothing just create scatter plot
parameter:
name --> list containg name of student
subject--> list containg marks of subject
subName --> subject name
font1 , font2 --> dict contaning fontsytle for x,y lable and title
'''
def scatterGraph(name,subjectMarks,subName,font1,font2):
    plt.scatter(name,subjectMarks,edgecolor='red',color='gold',s=80) #plotting Scatter
    plt.xlabel('Student Name', fontdict = font2)#set x label
    plt.ylabel('Marks', fontdict = font2)#setting y label
    plt.title(f"Marks in {subName}", fontdict = font1) #set title
    plt.show()

'''
function to create bar chart --> return nothing just create barchart
parameter:
name --> list containg name of student
percentage--> list containg percentage of student
font1 , font2 --> dict contaning fontsytle for x,y lable and title
'''
def barGraph(name,percentage,font1,font2):
    plt.bar(name,percentage,width=0.6,linewidth=4,edgecolor='red',color='gold') #ploting bar 
    plt.xlabel('Student Name', fontdict = font2) #set x label
    plt.ylabel('Percentage %', fontdict = font2) #setting y label
    plt.title("Student's percentage", fontdict = font1) #set title
    plt.show()

'''
function to create pie chart --> return nothing just create pie chart
parameter:
stu --> object of student class
mylabel --> list containg  label for pie chart
'''
def pieChart(stu,mylabel):
    plt.pie( [stu.OOPS,stu.CSA,stu.MTCS,stu.DM,stu.TC] ,labels=mylabel) #plot pie chart
    plt.legend(title=f'{stu.name}') #setting legend title
    plt.show()

#driver code
def main():
    
    num=int(input('Enter number of students : ')) #user input for number of students
    stu=[] #list to store all objects of class student

    #loop to enter student class object details and store them in stu list
    for i in range(num):
        print(f'Details of student {i+1}')

        #taking student detail from user
        name=input('Enter name : ')
        OOPS=int(input('Enter marks in OOPS(max marks =100) : '))
        CSA=int(input('Enter marks in CSA(max marks =100) : '))
        MTCS=int(input('Enter marks in MTCS(max marks =100) : '))
        DM=int(input('Enter marks in DM(max marks =100) : '))
        TC=int(input('Enter marks in TC(max marks =100) : '))

        #storing object of class to list
        stu.append( student(name,OOPS,CSA,MTCS,DM,TC) )


    #lists that will contain subject wise marks , names and percentage of each student    
    name=[] #to store all students names
    OOPS=[] #to store all students oops marks
    CSA=[] #to store all students CSA marks
    MTCS=[] #to store all students MTCS marks
    DM=[] #to store all students DM marks
    TC=[] #to store all students TC marks
    perc=[] #to store all students percentage

    #loop that will append respective values in respective lists
    for i in range(0,len(stu)):
        name.append(stu[i].name)
        perc.append(stu[i].percentage())
        OOPS.append(stu[i].OOPS)
        CSA.append(stu[i].CSA)
        MTCS.append(stu[i].MTCS)
        DM.append(stu[i].DM)
        TC.append(stu[i].TC)

    #font for title and labels in chart
    font1 = {'family':'serif','color':'blue','size':20}
    font2 = {'family':'serif','color':'darkred','size':15}

    while True: #loop for menu driven
        #main driven
        print('***************************************************************************************************')
        print("1.To Show Percentage Comparison of all Students \n2.To Show Subjectwise marks of each student\n3.To Show Studentwise Marks in each subject\n4.Exit ")
        choice=input('Choose one option from above:')

        if choice=='4':exit()       #exit the code

        if choice=='1': #To Show Percentage Comparison of all Students
           barGraph(name,perc,font1,font2)

        elif choice=='2':#To Show Subjectwise marks of each student

            while True:
                print('***************************************************************************************************')
                print('1.OOPS \n2.CSA \n3.MTCS\n4.DM\n5.TC\n6.Back' )
                subChoice=input('Choose One subject from above(type 1/2/3/4/5/6) : ')

                #calling function to create scatter graph in when subChoice is 1 to 5
                if subChoice=='1': scatterGraph(name,OOPS,"OOPS",font1,font2)

                elif subChoice=='2': scatterGraph(name,CSA,"CSA",font1,font2)

                elif subChoice=='3': scatterGraph(name,MTCS,"MTCS",font1,font2)

                elif subChoice=='4': scatterGraph(name,DM,"DM",font1,font2)

                elif subChoice=='5': scatterGraph(name,TC,"TC",font1,font2)

                elif subChoice=='6': break

                else: print('Invalid choice')

        elif choice=='3': #To Show Student Marks in each subject
            print("Student Name:")
            for j in range(len(name)):
                print(f"{j+1}. {name[j]}")
            names=input("\nEnter name of student to search : ") #user input to serach name of student if its already entered
            found=False
            for i in stu: #looping in all objects
                mylabel=['OOPS','CSA','MTCS','DM','TC'] #setting label 
                if names.lower()==i.name.lower(): #if name found
                    pieChart(i,mylabel) #callinf function to create pie chart
                    found=True
                    break
            if found==False: print('Name not Found')
        
        else: print("Invalid Choice")

if __name__=="__main__":
    main()