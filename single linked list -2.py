class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
def createsinglelinkedlist(arr):
    head=None
    for val in arr:
        if(head==None):
            head=Node(val)
            temp=head
        else:
            temp.next=Node(val)
            temp=temp.next
    n_h=deleteHead(head) 
    printLinkedList(n_h)  
def printLinkedList(n_h):
    temp=n_h 
    while(temp):
        print(temp.val)
        temp=temp.next 
def deleteHead(head):
    n_head=head.next
    head.next=None
    return n_head     
arr=list(map(int,input().split()))
createsinglelinkedlist(arr)       
