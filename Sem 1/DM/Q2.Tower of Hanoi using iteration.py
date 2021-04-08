'''
Program to implement tower of Hanoi iteration
source: where all disk
destination : where disk have to move
help: only to help move disk from source to distination
'''          

def main():
    disks=int(input('Enter the number of disks: ')) #taking input from user for number of disk
    source=[i for i in range(disks,0,-1)] #sourse tower
    destination=list()#destination tower
    help=list()#help tower
    move=2**disks-1 #no of  move required
    #print all three tower before move disk from sourse to destination
    print('Soure Tower ---> {}\nDestination Tower ---> {}\nHelp Tower ---> {}'.format(source,destination,help)) 
    print('Note: disk get smaller when go from left to right')
    print('Total number of move Required: ',move) #print number of moves
    print('\nStep:\n')
    hanoi_iteration(source,destination,help,move,disks) #class function to print steps for tower of hanoi

#function to all step for tower of hanoi
def hanoi_iteration(source,destination,help,move,disks):
    #loop to print all steps
    for i in range(1,move+1):
        if i%3==1:              #move disk from source to destination or vice versa                                     
            if destination==[]: #when destination tower not have any disk
                #move top disk from source to destination
                destination.append(source[-1])
                source.pop()
            #when source tower is empty or top disk of source is large then top disk of destination tower
            elif source==[] or source[-1]>destination[-1]:      
                #move top disk from destination to source
                source.append(destination[-1])
                destination.pop()
            elif destination[-1]>source[-1]: #when top disk of destination is larger than top disk of source tower
                #move disk from destination tower to source tower
                destination.append(source[-1])
                source.pop()

        elif i%3==2: #move disk from help tower to source tower or vice versa 
            if help==[] : #when help tower don't have any disk
                #move top disk from source to help tower
                help.append(source[-1])
                source.pop()
            #when source tower is empty or top disk of source tower is large then top disk of help tower
            elif source==[] or source[-1]>help[-1]:
                #move disk from help tower to source tower         
                source.append(help[-1])
                help.pop()
            elif help[-1]>source[-1]:   #when top disk of help tower is larger than top disk of source tower
                #move top disk from sorce tower to help tower
                help.append(source[-1])
                source.pop()

        elif i%3==0:        #move disk from destination tower to help tower or vice versa
            if destination[-1]>help[-1]:    #when top disk of destination tower is larger than top disk of help tower
                #move top disk from help tower to destination tower
                destination.append(help[-1])
                help.pop()
            elif help[-1]>destination[-1]:  #when top disk of help tower is larger than top disk of destination tower
                #move top disk from destination tower to help tower
                help.append(destination[-1])
                destination.pop()

        if disks%2==0: #when there is even disk
            print("step {}:\nSource Tower ---> {}\nDestination Tower ---> {}\nHelp Tower ---> {}\n".format(i,source,help,destination))
        else: #when no of disk is odd
            print("step {}:\nSource Tower ---> {}\nDestination Tower ---> {}\nHelp Tower ---> {}\n".format(i,source,destination,help))

main()  #call function to start program
