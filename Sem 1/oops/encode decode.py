'''Today Ms. GOOFY has to send a message to her friend but in a secure manner. She designed her own way of encoding and decoding messaging. 
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

help Ms Goofy to design a program for the same. 
'''
def main():
    #taking message from user
    message=input('Enter the message: ')
    code=endcoder(message)#calling function to encode the message
    print('\nMessage after Encode: ',code)#print the encode message
    decode=decoder(code)#calling function to decode the encode message
    print('\nMessage after decode the code:',decode)#print the decoded message


#function to encode the message
def endcoder(message):
    code=''#create string for encoded message
    #dictionary if message contain any digit/number to get its value
    number={'0':'zero','1':'one','2':'two','3':'three','4':'four','5':'five','6':'six','7':'seven','8':'eight','9':'nine'}
    #loop to encode the given message
    for i in message:
        if i>='0' and i<='9':#if element is number
            #fetching its value from our dictionary
            #concatenate it by reversing it and appending space
            code=code+' '+(number[i])[::-1]
        elif (i>='a' and i<='z') or (i>='A' and i<='Z') or (i==' '):#if element is character or space
            charASCII=str(ord(i))#using ord function to fetch ascii value
            #reversing ascii value and concatenate it with code
            code=code+' '+charASCII[::-1]
        else: #if element is not space neither number nor character
            code=code+' '+i #concatenate as it is
    return code #return ecoded message

#function to decode the encode message
def decoder(code):
    number={'zero':'0','one':'1','two':'2','three':'3','four':'4','five':'5','six':'6','seven':'7','eight':'8','nine':'9'}
    decode='' #create string to decodeg message
    for i in code.split():#loop to decode encode message
        i=i[::-1]#reverse the element
        if i.isnumeric():#if element is number
           #casting element in integer and give it in char function for getting character from ascii    
            decode=decode+chr(int(i))
        elif i in number.keys():#checking if element is in dictionary as key
            decode=decode+number[i] #fetching element value from dictionary and concatent it
        else:#if element is not space neither number nor character
            decode=decode+i#concatenate as it is
    return decode     #return decode message

if(__name__=="__main__" ): 
   main() # calling main function