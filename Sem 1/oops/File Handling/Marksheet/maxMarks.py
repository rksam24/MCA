#3. Also generate a file containing name of students scoring highest marks subject-wise. 

import pickle

#function to create file conataing higest marks in each subject
def highest_marks():
    marksFile= open('student_record','rb') #open the file
    data=pickle.load(marksFile) # load the data
    dict1={}
    dict1['name']=[]
    for i,j in data.items(): #loop to create dict subjects as keys and marks as value
        dict1['name'].append(i)
        for x,y in j.items():
            if x not in dict1:
                dict1[x]=[]
                dict1[x].append(y)
            else:
                dict1[x].append(y)
    file= open('maxfile.txt',"w") #create which contain highest marks of each subject

    #loop fot highest marks
    for sub in dict1:
        if sub not in ("name","RollNo"):
            maximum = max(dict1[sub])
            ind = dict1[sub].index(maximum)
            file.write("Max of {} is {} of {} and Rollno {}\n".format(sub,maximum,dict1["name"][ind],dict1["RollNo"][ind]))
    file.close() #close the file
    marksFile.close()#close the file
highest_marks()