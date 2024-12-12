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
            while n.ref is not None:
                 n=n.ref
            while n is not None:
                print(n.data,end="")
                n=n.pref


db=DoublyLL()
db.Print_LL()
db.Print_rev()