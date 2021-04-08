class computer:
    def __init__(self,color,brand,processor,ram):
        self.color=color
        self.brand=brand
        self.processor=processor
        self.ram=ram
    def fetchAttributes(self):
        print('Color: {}\nBrand: {}\nProcessor: {}'.format(self.color,self.brand,self.processor))

#taking attribute from user
color=input('Enter the color: ')
brand=input('Enter the Brand of Computer: ')
pro=input('Enter the processor of computer: ')
ram=input('Enter the ram: ')

print('\nComputer detail\n')
ob1=computer(color,brand,pro,ram)
ob1.fetchAttributes()
