def fileContent():

    content=''
    print('Enter the file content to end file press enter twice:')
    for i in range(50):
        add=input()
        if add=='':
            break
        else:
            content=content+'\n'+ add
    return content
    
print(fileContent())
