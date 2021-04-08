"""
We have dictinary which contain contain word and its meaning.
program to create dictinary which contain Synonym of words.

condition: Without use recursion
"""
def main():
    #Dictinary which contain word and its meaning
    myDict={'Human being':'Human','Mother tongue':'Language',
            'Hemosapien':'Human','Mankind':'Human',
            'Dialect':'Language','Personal computer':'Computer',
            'Laptop':'Computer','H2O':'Water'}
    #calling the function which return the dict which contain word and its synonym 
    print('Synonym Dictinaory: \n')
    for word,synonyms in synonym(myDict).items():#loop to print to get synonym of words
        print(word,': ',end="")#print the word. end is use to continue in same line
        print(*synonyms,sep=',')#print synonyms of word. sept is use to seperate each word with comma

'''
Function to create the dictinary contain word and its Synonyms
Parameter: myDict = dictinary which contain word and its meaning
return: synonym_dict which contain word and its synonyms
'''
def synonym(myDict):
    synonym_dict=dict() #create the dict for word and its synonym
    for word,meaning in myDict.items():#loop to get synonym of each word
        if meaning not in synonym_dict:#cheching if word is not in dict already
            synonym_dict[meaning]=list()#assign word as a key and create empty list as its value
            synonym_dict[meaning].append(word)#add the value/synonym for word
        else:
            synonym_dict[meaning].append(word) #add the synonym for word
            
    return synonym_dict #return the dictianry which conatin word and its synonyms

main()
