class Node:
     
    def __init__(self, data):
        self.data = data 
        self.next = None 
 
class LinkedList:
 
    def __init__(self):
        self.head = None
 
def Circular(head):
    if head==None:
        return True
        
    node = head.next
    i = 0
     
    while((node is not None) and (node is not head)):
        i += 1
        node = node.next
     
    return(node == head)
 
# main
list1 = LinkedList()
list1.head = Node(1)
second = Node(2)
third = Node(3)
fourth = Node(4)
     
list1.head.next = second;
second.next = third;
third.next = fourth
     
if (Circular(list1.head)):
    print('Yes')
else:
    print('No')
     
fourth.next = list1.head
     
if (Circular(list1.head)):
    print('Yes')
else:
    print('No')