class computer:
    count=0 #to count number of object
    def __init__(self):
        self.color=''
        self.brand=''
        self.processor=''
        self.ram=''
        computer.count+=1

    def get_color(self): #to get color of computer
        return self.color
    def get_brand(self): #to get brrand of computer
        return self.brand
    def get_processor(self): #to get processor of computer
        return self.processor
    def get_ram(self): #to get ram of computet
        return self.ram

    #to take color, brand ,processor ,ram detail from user
    def set_color(self):
        self.color=input('Enter the color: ')
        return self.color
    def set_brand(self):
        self.brand=input('Enter the brand: ')
        return self.brand
    def set_processor(self):
        self.processor=input('Enter the processor of computer: ')
        return self.processor
    def set_ram(self):
        self.ram=input('Enter the Ram detail: ')
        return self.ram
    

    
    #display
    def display(self):
        self.set_color()
        self.set_brand()
        self.set_processor()
        self.set_ram()
        self.get_color()
        self.get_brand()
        self.get_processor()
        self.get_ram()
        return (self.color,self.brand,self.processor,self.ram)

    #compare the computer
    def compare(self,obj):
        if self.color==obj.color:
            print('\nColor of computer same')
        else:
            print('Color of computer different')
        if self.brand==obj.brand:
            print('Brand of computer same')
        else:
            print('Brand of computer different')
        if self.processor==obj.processor:
            print('Processor of computer same')
        else:
            print('Processor of computer different')
        if self.ram==obj.ram:
            print('ram of computer same')
        else:
            print('ram of computer different')
        

def main():  
    ob1=computer()
    print('Enter conguration of computer 1')
    w,x,y,z=ob1.display()
    print('\nEnter conguration of computer 2')
    ob2=computer()
    r,s,u,v=ob2.display()
    print('\nComputer 1 deatil')
    print('Color: {}\nBrand: {}\nProcessor {}\nRam: {}\n\n'.format(w,x,y,z))
    print('Computer 2 deatil')
    print('Color: {}\nBrand: {}\nProcessor {}\nRam: {}'.format(r,s,u,v))
    print('\nNumber of computer: ',computer.count)
    print('\nCompare both number')
    ob1.compare(ob2)
main()