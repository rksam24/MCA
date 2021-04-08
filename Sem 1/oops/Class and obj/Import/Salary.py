'''Create a class employee with following attributes:
1. Name
2. EmpID
3. Designation: Worker/ Supervisor/Manager
4. Salary
5. Experience
Define all getter and setter methods + show method+__str__()
Calculate Salary according to Designation and experience
BaseSalary+AddSal+HRA
BaseSalary is
{10000, 15000, 20000} for Worker, Supervisor, Manager resp
AddSal=%age experience of BaseSalary
HRA=5% of BaseSalary
'''
class employee:
    #contructor
    def __init__(self,name,empId,designation,experience):
        #value takig
        self.name=name
        self.empId=empId
        self.designation=designation
        self.experience=experience
        #default value
        self.salary=0
        self.baseSalary=0
        self.HRA=0
        self.addSal=0
    
    #getter function
    def get_name(self):
        return self.name
    def get_empId(self):
        return self.empId
    def get_designation(self):
        return self.designation
    def get_experience(self):
        return self.experience
    
    #setter function
    def set_name(self):
        self.name=input("Enter Employee's name: ")
    def set_empId(self):
        self.empId=input("Enter Employee's ID: ")
    def set_designation(self):
        self.designation=input("Enter Employee's Designation: ")
    def set_experience(self):
        self.experience=input("Enter Employee's experince in years: ")

    #function to set base salary
    def baseSalaryCalculate(self):
        if (self.designation).lower()=='worker':
            self.baseSalary=10000
        elif (self.designation).lower()=='supervisor':
            self.baseSalary=15000
        elif (self.designation).lower()=='manager':
            self.baseSalary=20000
        else:
            self.baseSalary=5000
        return self.baseSalary

    #function to calculate HRA
    def hraCalculate(self):
        self.baseSalaryCalculate() #calling function for base salary
        self.hra=(5/100)* self.baseSalary
        return self.hra
    
    #function to calculate addsalary based on experience
    def additionSalaryCalculate(self):
        self.baseSalaryCalculate() #calling function for base salary
        self.addSal=(self.experience/100) * self.baseSalary
        return self.addSal
    
    #function to get total salary
    def get_salary(self):
        self.hraCalculate() #calling function for base salary
        self.additionSalaryCalculate() #calling function for base salary
        self.salary=self.baseSalary + self.HRA + self.addSal
        return self.salary
    
    #function to display the details
    def display(self):
        print("\n\t****Employee Detail****")
        print('Name: {}\nEmployee ID: {}\nDesignation: {}'.format(self.get_name(),self.get_empId(),self.get_designation() ) )
        print("Experience in year: {}\nBase Salary: {}".format(self.get_experience() ,self.baseSalaryCalculate() ) )
        print('Additional Salary: {}\nHRA: {}'.format(self.additionSalaryCalculate() ,self.hraCalculate()))
        print('Total Salary: {}'.format(self.get_salary() ))

    def __str__(self):
        return '****Employee Detail****'+'\nName:'+self.name+'\nEmpID: '+self.empId+'\nDesignation: '+self.designation+'\nExperience: '+str(self.experience)+'\nSalary: '+str(self.salary)

#function to update employee details
def  update(emp):
    print('what you want to change \n1.Name\n2.Employee Id\n3.Designation\n4.Experience\n5.exit')
    #loop for choice and change details
    while(True):
        choice=input('\nEnter the choice: ') #taking option from user
        choice=choice.lower() #change option of user into lower case
        if choice=='1' or choice=='name': 
            emp.set_name()        #call function to change name
        elif choice=='2' or choice=='employee id':
            emp.set_empId()        #call function to change employee id
        elif choice=='3' or choice=='designation':
            emp.set_designation()   #call function to change Designation
        elif choice=='4' or choice=='experience':
            emp.set_experience()         #call function to change Experience
        elif choice=='5' or choice=='exit':
            break                   #end the loop
        else:                       #for invalid option
            print("Invalide Option")
        print('Enter other option which you want to change!!')
    emp.display()                  #display the details

def main():
    #taking employee details from user
    name=input("Enter Employee's details \nName:")
    empId=input('Employee ID: ')
    designation=input('Designation (Worker,Supervisor,manager,other): ')

    while(True):
        try:
            exp=int(input("Enter the Experience in year: "))
            break
        except ValueError:
            print('Enter Experience again!!')
    
    #creating object emp of class employee
    emp=employee(name,empId,designation,exp)
    emp.display() #calling function for display

    #asking from user for changes
    print("\nEnter the wrong detail? want to change the type 'yes' otherwise press enter ")
    if input().lower()=='yes':
        update(emp)

    print('\nPrint details with __str__')
    print(emp.__str__()) #calling function to print detail with __str__ function

main() 