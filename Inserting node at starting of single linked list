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
        n_h=insertHead(head)
        printlinkedlist(n_h)
def printlinkedlist(n_h):
    temp=n_h
    while(temp):
        print(temp.val)
        temp=temp.next
def insertHead(head):
    firstnode=int(input())
    new_node=Node(firstnode)
    new_node.next=head
    return new_node
arr=list(map(int,input().split()))
createsinglelinkedlist(arr)
