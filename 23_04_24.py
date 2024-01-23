#------Linked List-----

class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class ll:
    def __init__(self):
        self.head=None
    def print(self):
        if self.head is None:
            print("LL is empty")
        else:
            n=self.head
            while n is not None:
                print(n.data )
                n=n.next
    def add_begin(self,data):
        new_node=node(data)
        new_node.next=self.head
        self.head=new_node
    def add_end(self,data):
        new_node=node(data)
        n=self.head
        if n is None:
            self.head=new_node
        else:
            while n is not None:
                n=n.next
            n.next=new_node
            
    

n=ll()
n.add_begin(20)
n.add_begin(40)
n.add_begin(80)
n.add_begin(100)
n.add_end(20)
n.print()


        