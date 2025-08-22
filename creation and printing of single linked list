class Node:
    def __init__(self,val):
        self.data=val
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
    return head.next.data    
arr=list(map(int,input().split()))
print(createsinglelinkedlist(arr))     

       
