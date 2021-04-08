'''Q1. Today Ms. GOOFY has to send a message to her friend but in a secure manner. She designed her own way of encoding and decoding messaging. 
Foe encoding, she assumed the following:
Given any number, she returns the corresponding text in words but in reverse order.
If it is a character, then take its ASCII value and reversed it.
Also, inserted a space between each encoded o/p.
For any special character, take it as it is
e.g. if input is : 3AD$2a
o/p:  eerht 56  86 $ owt 79
For decoding, the reverse of above is conducted.
i.e. input: eerht 56  86 $ owt 79
output: 3AD$2a 
help Ms Goofy to design a program for the same
Condition:use file for input
'''

'''
function to take file name and choice from user
variable used:
filename: name of file to decode or encode
choice: option for open the file or create new file
codeChoice: option for encode and decode 
fname: file name of encoded/decode file
'''
def choice():
    filename=input('Enter the file name: ')  #asking input from user
    print("\nPlease Choose one option.\n1.Open exit file.\n2.Create new file.\n3.Exit")    
    #loop for choice so that if enter option if invalid then take choice again
    while True: 
        choice=input('Enter your choice: ') #taking choice from user
        if choice=='1':                     #to open exit file
            data=readFile(filename)         #read the file and get data form it
            break                           #end the loop
        elif choice=='2':                   #create new file
            content=fileContent()           #calling function to get data for new file
            writeFile(filename,content)     #calling function to create new file
            print(filename,'is created')
            data=readFile(filename)         #calling function to read the created file
            break                           #end loop
        elif choice=='3':                   #to end the program
            print('Exit...')
            exit()                          #end the loop 
        else:
            print('Invalid choice. try again')
        

    print("\nPlease choose one option\n1.Encode the file\n2.Decode the file.\n3.Encode the file and create file for encode code.")
    print("4.Decode the file and create file for decoded code.\n5.Exit")
    #loop for choice so that if enter option if invalid then take choice again
    while True:
        codeChoice=input('Enter your choice: ') #taking choice from user
        if codeChoice=='1':                     #to encode data from file
            print('Encoded Message')
            print(encoder(data))                #calling function to endoced the data
            break                               #end the loop
        elif codeChoice=='2':                   #to decode data from file
            print('Decode Message')         
            print(decoder(data))                #calling function to decode the data
            break                               #end the loop
        elif codeChoice=='3':                   #to encode the data from file and create new file for encoded data
            content=encoder(data)               #calling fuction to get encoded message/data
            fname=filename+'_encoded'           #declare the name of encoded file
            writeFile(fname,content)            #calling function to create file for encoded data/message
            print(fname,'is created.')       
            break                               #end the loop
        elif codeChoice=='4':                   #to create file for decode data/message
            content=decoder(data)               #calling function to decoded data/messaege
            fname=filename+'_decoded'           #declare the name of decoded file
            writeFile(fname,content)            #calling function to create file for decoded data/message
            print(fname,'is created.')
            break                               #end the loop
        elif codeChoice=='5':                   #to end the code
            print('Exit...')
            exit()                              #exit the code
        else:                                   #for invalid option
            print('Enter the invalid choice ')


'''
function to read the file
parameter and variable:
filename: name of file in which data stored
mode: mode in which file open
data: content of file 
'''
def readFile(filename,mode='r'):
    try:                                                    #try block if error occur execute except block
        with open(filename+'.txt',mode) as codeFile:        #open the file
                data=codeFile.read()                        #read the file
                return data                                 #return data of file
    except FileNotFoundError:                               #if error occur in try block it execute
        print('File not exit/found')

'''
function to create the file(new file, encoded file, decode file)
parameter:
filename : name of new file which will  created
content: content/data which will stored in file
mode: mode in which file open
'''
def writeFile(filename,content,mode='w'):
    with open(filename+'.txt',mode) as codeFile:            #create the file
        codeFile.writelines(content)                        #write content/data in file

#funtion to take data/content from user for new file either single line or multiline
def fileContent():
    content=''                                              #data which will file contain
    print('Enter the file content to end file press enter twice:')
    #loop to take input from user either single line or multiline
    for i in range(50):                                     #50 max line user can enter 
        add=input()                                         #take input form user
        if add=='':                                         #when user don't write anything loop break 
            break                                           #end the loop 
        else:               
            content=content+'\n'+ add                       #join the all the input together
    return content                                          #return the user input

'''
function to encode the message
parameter:
message: data/message which will encoded
'''
def encoder(message):
    code=''                                                 #create string for encoded message
    #dictionary if message contain any digit/number to get its value
    number={'0':'zero','1':'one','2':'two','3':'three','4':'four','5':'five','6':'six','7':'seven','8':'eight','9':'nine'}
    #loop to encode the given message
    for i in message:
        if i>='0' and i<='9':                               #if element is number
            #fetching its value from our dictionary
            #concatenate it by reversing it and appending space
            code=code+' '+(number[i])[::-1]
        elif (i>='a' and i<='z') or (i>='A' and i<='Z') or (i==' ') or (i=='\n') :#if element is character or space
            charASCII=str(ord(i))                            #using ord function to fetch ascii value
            #reversing ascii value and concatenate it with code
            code=code+' '+charASCII[::-1]
        else: #if element is not space neither number nor character
            code=code+' '+i                                  #concatenate as it is
    return code                                              #return ecoded message

'''
function to decode the encode message
paramete:
code: message/data which will decode
'''
def decoder(code):
    number={'zero':'0','one':'1','two':'2','three':'3','four':'4','five':'5','six':'6','seven':'7','eight':'8','nine':'9'}
    decode=''                                               #create string to decodeg message
    for i in code.split():                                  #loop to decode encode message
        i=i[::-1]                                           #reverse the element
        if i.isnumeric():                                   #if element is number
           #casting element in integer and give it in char function for getting character from ascii    
            decode=decode+chr(int(i))
        elif i in number.keys():                            #checking if element is in dictionary as key
            decode=decode+number[i]                         #fetching element value from dictionary and concatent it
        else:                                               #if element is not space neither number nor character
            decode=decode+i                                 #concatenate as it is
    return decode                                           #return decode message

choice()   #calling function to start the code