#Program to find a Preorder, Inorder and Postorder traversal of 3-ary Tree.

import copy
#function to create 3 ary tree
def create3aryTree(nodes):
    tree=dict()     #dict will contain parents and child nodes
    nodeCheck=True  
    for i in nodes: #iterating nodes
        compare=[nodes[0]] 
        count=1
        for n in nodes: #iterating loop to check when outer loop break
            if len(tree)==0: break
            for child in tree.values(): #iterating in tree
                if n in child:      #check if node is in tree
                    compare.append(n)   #append the node to compare list
                    count+=1
            if compare==nodes: nodeCheck=False
            if n not in  tree:  #if statement to add node to tree with no child
                tree[n]=[]
        if nodeCheck==False:break #to break loop when all node placed in tree

        #loop to take number of child node for root from user
        while(True):
            connection=int(input(f"\nEnter the number of child node '{i}' have(atmost 3): "))
            if connection<=3 and connection<=(len(nodes)-count):
                break #break loop when child node less than 3 and child also less than total node remain which are not child node yet
            print('Enter correct number of connection!!')
        #loop to take child nodes from user
        while(True):
            childNode=[ i for i in input(f"\nEnter the child node of '{i}':\n").split()] #takingig child node from user
            tree[i]=childNode   #add child node to parent node in tree
            if len(childNode)!=connection or (i in childNode): #to check user enter correct number of child node
                print('Enter correct number of chile nodes or correct child node!!')
                continue 
            flag=True   #to check when loop is break
            for child in childNode: #iterting in child
                for childs in tree.values():
                    if ((child in childs) and (childs!=tree[i])) or child not in nodes: #to check if child node user enter is not child node of another parent
                        print('Enter correct child nodes!!')
                        flag=False
                        break
                if flag==False: break
            if flag==True: break    #breal loop when child nodes are correct
    return tree

#function to traverse tree in postorder
def postorder(tree,root,result=''):
    if tree[root]==[]: #when node not have any child node
        return root     #return root
    else:
        for i in tree[root]:      #loop to visit left node then right node then root
            result=result+postorder(tree,i)+' --> '
        tree[root]=[]
        result=result+postorder(tree,root) #return the postorder traversed of tree
        return result

#function to traverse tree in preorder
def preorder(tree,root,result=''):
    if tree[root]==[]: #when root not have child node return root
        return root     
    else:
        result=result+ root #visit root 
        for i in tree[root]:#loop to visit left node then right node
            result=result+' --> '+ preorder(tree,i)
        return result   #return all visited node

#function to traverse tree in in inorder
def inorder(tree,root,result=''):
    if tree[root]==[]:  #when root not have child node return root
        return root
    else:
        for i in tree[root]: #loop to visit
            if result!='' and result[-1].isalnum(): result=result +' --> '
            result=result+inorder(tree,i) #visit root
            
            if tree[root].index(i)+1==1:
                result=result+' --> '+root
        return result   #return all visited node

#driver code
nodes=[i for i in input('\nEnter the nodes(first node is root of tree) with space b/w each nodes:\n').split()]
#calling function to create tree
tree=create3aryTree(nodes)
#printing tree
print("\nParent Node\t\tChild node(from left to right)")
for parent,child in tree.items():
    print(parent,'\t\t:\t',*child,sep=' ')
tree1=copy.deepcopy(tree)

#callling function to traversed the tree
print("\nVisited node if Postordered traversal are \n",postorder(tree1,nodes[0]))
print("\nVisited node if Preordered traversal are \n",preorder(tree,nodes[0]))
print("\nVisited node if Inordered traversal are \n",inorder(tree,nodes[0]))