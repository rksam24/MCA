'''
functiion to findout meaning of word
parameter: myDict=dict containg word and its meaning
word= word for which meaning is need
'''
def main():
    #Dictinary which contain word and its meaning
    myDict={'Human being':'Human','Mother tongue':'Language',
            'Hemosapien':'Human','Mankind':'Human',
            'Dialect':'Language','Personal computer':'Computer',
            'Laptop':'Computer','H2O':'Water'}
    copyDict=myDict.copy() # copy the myDict into copydict
    #calling the function which return the dict which contain word and its synonym
    print('Synonym Dictinaory: \n')
    for word,synonyms in synonym(copyDict).items():#loop to print to get synonym of words
        print(word,': ',end="")#print the word. end is use to continue in same line
        print(*synonyms,sep=',')#print synonyms of word. sept is use to seperate each word with comma
'''
Function to create the dictinary contain word and its Synonyms
Parameter: myDict = dictinary which contain word and its meaning
synonym_dict=dict(): empty dict which contain synonyms of word
return: synonym_dict which contain word and its synonyms
'''
def synonym(copyDict,synonym_dict=dict()):
    if copyDict=={}:#checking if dictinary is empty if yes required dictinary return
        return synonym_dict
    else:
        key=list(copyDict.keys())#converting keys of given dict into list
        if copyDict[key[0]] not in synonym_dict:#cheching if word is not in dict already
            synonym_dict[copyDict[key[0]]] = list()#assign word as a key and create empty list as its value
            synonym_dict[copyDict[key[0]]].append(key[0])#add the value/synonym for word
        else:
            synonym_dict[copyDict[key[0]]].append(key[0])#add the synonym for word
        copyDict.pop(key[0]) #remove checked word for myDict
        return synonym(copyDict,synonym_dict) #call the function to find remaining synonyms

main()
