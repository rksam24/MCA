'''Define all getter and setter methods + __str__()
LAPTOP
Attributes:
Brand
Processor
RAM
Color'''

class computer:
    #contructor 
    def __init__(self,color,brand,processor,ram):
        self.color=color
        self.brand=brand
        self.processor=processor
        self.ram=ram

    #getter function
    def get_color(self):
        return self.color
    def get_brand(self):
        return self.brand
    def get_processor(self):
        return self.processor
    def get_ram(self):
        return self.ram

    #setter function
    def set_color(self):
        self.color=input('Enter the color: ')
    def set_brand(self):
        self.brand=input('Enter the brand: ')
    def set_processor(self):
        self.processor=input('Enter the processor: ')
    def set_ram(self):
        self.ram=input('Enter the Ram detail: ')
        
    #function to display
    def display(self):
        print('\nComputer configuration: ')
        print('\nColor: {}\nBrand: {}'.format( self.get_color(),self.get_brand() ))
        print('Processor: {}\nRam: {}'.format( self.get_processor(),self.get_ram() ))

    #__str__ function to return all the properties of computer
    def __str__(self):
        return self.color+','+self.brand+','+self.processor+','+self.ram


#function to change configuration of computer
def update(comp):
    print('what you want to change \n1.color\n2.Brand\n3.Processor\n4.Ram\n5.exit')
    #loop for choice and change details
    while(True):
        choice=input('\nEnter the choice: ') #taking option from user
        choice=choice.lower() #change option of user into lower case
        if choice=='1' or choice=='color': 
            comp.set_color()        #call function to change color
        elif choice=='2' or choice=='brand':
            comp.set_brand()        #call function to change brand
        elif choice=='3' or choice=='processor':
            comp.set_processor()    #call function to change processor
        elif choice=='4' or choice=='ram':
            comp.set_ram()          #call function to change ram
        elif choice=='5' or choice=='exit':
            break                   #end the loop
        else:                       #for invalid option
            print("Invalide Option")
        print('Enter other option which you want to change!!')
    comp.display()                  #display computer configuration


def main():
    print('Enter the configuration: ')
    #taking input from user
    color=input('Color: ')
    brand=input('Brand: ')
    pro=input('Processor: ')
    ram=input('Ram: ')     

    #creating object comp for class computer
    comp=computer(color,brand,pro,ram)
    comp.display()  #calling function to diplay the configuration of computer

    #if want to update the detail of computer
    print("\nEnter the wrong detail?, want to change then type 'yes' otherwise press enter")
    if input()=='yes':
        update(comp)
    
    #print detail with __]str__ function
    print('\nprinting configuration Using __str__')
    print(comp.__str__())   #call function for detail of computer

main()  #call function to start function