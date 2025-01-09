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
    def delete_begin(self):
        if self.head is None:
            print("Linked List is empty")
        if self.head.nref is None:
            self.head=None
        else:
            self.head=self.head.nref
            self.head.pref=None
    def delete_end(self):
        if self.head is None:
            print("Linked List is Empty")
        if self.head.nref is None:
            self.head=None
        else:
            n=self.head
            while n.nref is not None:
                n=n.nref
            n.pref.nref=None
    def delete_by_val(self,x):
        if self.head is None:
            print("LL is empty")
            return
        if self.head.nref is None:
            if x==self.head.data:
                self.head=None
            else:
                print("X is not present inside the Node")
        if self.head.data==x:
            self.head=self.head.nref
            self.head.pref=None
            return
        n=self.head
        while n.nref is not None:
            if x==n.data:
                break
            n=n.nref
        if n.nref is not None:
            n.nref.pref=n.pref
            n.pref.nref=n.nref
        else:
            if n.data==x:
                n.pref.nref=None
            else:
                print("Node is not present inside the Linked List")
            

        
        

db=DoublyLL()
db.add_begin(67)
db.add_begin(78)
db.add_begin(88)
db.add_begin(89)
db.delete_begin()
db.delete_end()
db.delete_by_val(88)
db.Print_LL()
