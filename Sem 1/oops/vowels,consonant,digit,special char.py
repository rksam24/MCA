''' program to count numbers of vowels , consonants,digit and special character
    eg:
    ip: my name is Rohit. 54
    o/p: Vowels:4
         Consonant:8
         Digit:2
         Special Character:5
'''
def main():
    str=input("Enter a String:") #take input from user as string
    countCharType(str)
#calling function for print number of vowel,consonant,digit,special Character



    
#Function to count number of vowels,consonant, digits and special character in string.
def countCharType(str):
#declare the variable vowels,consonant,digit,specialChar
    digit=0
    vowels=0
    consonant=0
    specialChar=0
    str=str.lower()
#convert uppercase to lowercase so that we don't need uppercase for also
    for char in str:
        if(char>='a' and char<='z'):
        #check if a character in string in b/w a to z i.e if its alphabate
            if(char=='a' or char=='e' or char=='i' or char=='o' or char=='u'):
        #check if character is a,e,i,o,u or not i.e check its vowel or not if not then go to else statement
                vowels+=1
        #if above condition true then value of vowels increase by 1
            else:
                consonant+=1
        #if a character is not vowels then value of consonant add by 1
        elif(char>='0' and char<='9'):
        #if character is not alphabate then it then if its b/w 0 to 9 i.e its digit or not
            digit+=1 #if its digit then value of digit increase by 1
        else:
            specialChar+=1
        #if character is not alphabate nor digit then its special character then the value of specialChar increase by 1
    print("Vowels:",vowels)#Print the value of vowels
    print("consonant:",consonant)#print the value of consonat
    print("Digit:",digit)#print the value of digit
    print("Special Character",specialChar) # print the value of specialChar
main()
