class Node():
    def __init__(self,data):
        self.data=data
        self.nref=None
        self.pref=None
class DoublyLL():
    def __init__(self):
        self.head=None
    def Print_LL(self):
        if self.head is None:
            print("Doubly Linked List is empty")
        n=self.head
        while n is not None:
            print(n.data,"->",end=" ")
            n=n.nref

    def Print_rev(self):
        if self.head is None:
            print("Doubly Linked List is empty")
        else:
            n=self.head
            while n.nref is not None:
                  n=n.nref
            while n is not None:
                print(n.data,end="")
                n=n.pref
    def insert_empty(self,data):
        if self.head is None:
            new_node=Node(data)
            self.head=new_node
        else:
           print("linked List is Not Empty")
    def add_begin(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            new_node.nref=self.head
            self.head.pref=new_node
            self.head=new_node
    def add_end(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            n=self.head
            while n.nref is not None:
                n=n.nref
            n.nref=new_node
            new_node.nref=n
    def add_after(self, data, x):
        new_node = Node(data)
        if self.head is None:
            print("Linked List is empty")
        else:
            n = self.head
            while n is not None:
                if x == n.data:
                   break
                n = n.nref
            if n is None:
                print("Given node is not present")
            else:
                new_node.nref = n.nref
                new_node.pref = n
                if n.nref is not None:
                    n.nref.pref = new_node
                n.nref = new_node


db=DoublyLL()
db.add_begin(67)
db.add_end(78)
db.add_after(78,67)
db.Print_LL()
