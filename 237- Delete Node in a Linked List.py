class Node:
    
    def __init__(self,data):
        self.data = data
        self.next = None
        
class LinkedList:
    
    def __init__(self):
        self.head = None
        
    def printList(self):
        temp=self.head
        while (temp):
            print(temp.data)
            temp = temp.next
            
    def deleteNode(self, node):
        node.data=node.next.data
        node.next=node.next.next
        
if __name__== '__main__':
    
    llist=LinkedList()
    
    #Data
    llist.head  = Node (5)
    node2      = Node (4)
    node3       = Node (3)
    node4       = Node (6)
    
    #Next
    llist.head.next = node2
    node2.next     = node3
    node3.next     = node4
    
    print("Created Linked List: ")
    llist.printList()
    llist.deleteNode(node3)
    print("\nLinked List after Deletion :")
    llist.printList()
