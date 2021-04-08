def main():
    #option
    print("""1.Number of Words in String
2.Reverse of String
3.Reverse each word of String
4.Largest word in String""") #used multiline string to print the option
    option() #calling function to select option

def option():
    print() #for next line
    #select choice
    ch=int(input('Enter your choice from above option: ')) # take the input from user for option
    if ch<=4:
        str=input("Enter the String: ") # take the input from user as string
        if ch==1:
            length(str) # calling the function to print no of in string
        elif ch==2:
            reverse(str) #calling the functiion to print revverse of string
        elif ch==3:
            wordReverse(str)
            ''' calling the function to reverse each word in the string
                ex: i/p my name is Rohit. o/p: ym eman is tihot
            '''
        else:
            largeWord(str) # calling the function to print largest word in the string
    else:
        print("Invalide Option, please try again") # print the statement when select option is not valid
        

def length(str):
    print("Number of Words in String:", len(str.split()))
"""split string into list with split() then find the number of element in list with len()
    then print the number of word in string """
def reverse(str):
    print("Reverse of String:", str[::-1])
#reverse the string with slicing and print it
    
def wordReverse(str):
    word=str[::-1].split()
    #reverse the string with slicing then split into list
    RW="" #create empty string RW
    for i in word: 
        RW=i+" "+RW
    """
    ex:word=['my','name','is','rohit']
    then using for loop first time i=my then  RW=i+' '+'RW.
    ex: if RW='n' then are RW=my n
    """
    print("Reverse each word of String:", RW)
    #print the value of RW which each word reverse in string
    
def largeWord(str):
    x=str.split() # split the string str into list then assign it to x
    largestWord ='' # create a string
    for i in x: #looping to find out the largest number in list
        if len(i) > len(largestWord):
            largestWord=i
    #checking if length of a word if more then next word if yes then assign that word to largestWord if not then goto next word
    print("Largest word in String:",largestWord)
    #print the largest word which we get from for loop


main()
 
