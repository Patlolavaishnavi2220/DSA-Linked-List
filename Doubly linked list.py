#array to doubly linked list
class Node:
    def __init__(self,val):
        self.prev=None
        self.data=val
        self.next=None
def createdoublylinkedlist(arr):
    head=None
    for val in arr:
        if(head==None):
            head=Node(val)
            temp=head
        else:
            newNode=Node(val)
            temp.next=newNode
            newNode.prev=temp    
            temp=temp.next
    return head        
arr=list(map(int,input().split()))
print(createdoublylinkedlist(arr))
