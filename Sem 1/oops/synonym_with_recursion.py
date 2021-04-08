"""
We have dictinary which contain contain word and its meaning.
program to create dictinary which contain Synonym of words.

condition: use recursion
"""

def main():
    #create the Dictinary which contain word and its meaning
    myDict={'Human being':'Human','Mother tongue':'Language',
            'Hemosapien':'Human','Mankind':'Human',
            'Dialect':'Language','Personal computer':'Computer',
            'Laptop':'Computer','H2O':'Water'}
    word=input('\nEnter the word: ').capitalize() #asking word from user to get synonym of word

    meanings = meaning(myDict,word) #calling function to findout meaning of word and assign it to variable
    print('\nMeaning of word is ',meanings) #print the meaning of word
    
    
    dictKey=list(myDict.keys()) #converting keys of given dict into list
    dictValue=list(myDict.values()) #converting values of given dict into list respectively to list for key

    #calling the function to findout Synoym of word and print it. sep is used to separate with comma(,)
    print('\nSynoymn of',word,'are')
    print(*synoymn(meanings,dictKey,dictValue)[meanings],sep=',')

'''
functiion to findout meaning of word
parameter: myDict=dict containg word and its meaning
word= word for which meaning is need
'''
def meaning(myDict,word):
    if word in myDict: #checking desire word in dict if yes then return meaning of that word
        return myDict[word]
    else:
        #if dict don't have that word in dict then it ask user enter its meaning then that word and its meaning add to dictinary
        myDict[word]=input('\nThis word is not in Diary.\nPlease enter Meaning of word: ').capitalize()
        return myDict[word] #return the meaninf of word


'''
function to findout synoymn of word
paramenter:
meaning: its the meaning of the word which help to find synoymn by comparing its meaning
dictKey: its a list which containg ever word of dictinary.
dictValue: its a list which containg meaning of each word from dictKey list( which contain word ) in same order
           eg:dictKey=[a,b,c] and dictValue=[1,2,3] in this meaning of a is 1 ,meaning of b is 2, meaning of c is 3
list2=list() #its a blank list which will contain synoymn for particular word
'''
def synoymn(meaning,dictKey,dictValue,list2=list()):
    if len(dictValue)>0: #Check if list conating meaning is not empty
        if dictValue[0].lower()==meaning.lower(): #convert the meaning and first meaning/item of dictValue  and checking if its same
            list2.append(dictKey[0])#if above condition true that word with respect to that meaning add to list
        #remove word and its meaning which is checked from list
        dictKey.pop(0) 
        dictValue.pop(0)

        #calling the function again within function to check if there is synoymns in list or not
        synoymn(meaning,dictKey,dictValue,list2) #recursion
    synonym_dict={}#create empty dict for synoymns
    synonym_dict.update({meaning:list2}) #add that synonyms to dict with its meaning key
    return synonym_dict #return the dict


main()
