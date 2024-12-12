class Node():
    def __init__(self,data):
        self.data=data
        self.ref=None
class SinglyLL():
    def __init__(self):
        self.head=None
 
    def printLL(self):
        if self.head is None:
            print("Linked List is empty")
        else:
            n=self.head
            while n is not None:
                print(n.data,"->",end=" ")
                n=n.ref


    def Insert_Begin(self,data):
        new_data=Node(data)
        new_data.ref=self.head
        self.head=new_data


    def add_end(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            n=self.head
            while n.ref is not None:
                n=n.ref
            n.ref=new_node
    def before_node(self,data,x):
        if self.head.data==x:
            new_node=Node(data)
            new_node.ref=self.head
        else:
            if self.head is None:
                print("Linked List is Empty") 
            n=self.head
            while n.ref is not None:
                if n.ref.data==x:
                    break
                n=n.ref
            if n.ref is None:
               print("Node is not Found")
            else:
                    new_node=Node(data)
                    new_node.ref=n.ref
                    n.ref=new_node
    
    def After_node(self, x, data):
       n = self.head
       while n is not None:
          if n.data == x:
             break
          n = n.ref
       if n is None:
          print(f"Node with data {x} not found in the list.")
       else:
          new_node = Node(data)
          new_node.ref = n.ref
          n.ref = new_node
    def deletebegin(self):
        if self.head is None:
            print("Could not delete because linked list is empty")
        else:
            self.head=self.head.ref  
    def delete_end(self):
        if self.head is None:
            print("LL is empty")
        if self.head.ref is None:
            self.head=None
        n=self.head
        while n.ref.ref is not None:
            n=n.ref
        n.ref=None
    def delete_by_value(self,x):
        if self.head is None:
            print("Could Not delete linked list is empty")
        if x==self.head.data:
            self.head=self.head.ref
        n=self.head
        while n.ref is not None:
            if x==n.ref.data:
                break
            n=n.ref
        if n.ref is None:
            print("Node is not present")
        else:
            n.ref=n.ref.ref
    
                    
        
LL=SinglyLL()
LL.Insert_Begin(34)
LL.Insert_Begin(94)
LL.Insert_Begin(84)
LL.add_end(56)
LL.delete_end()
LL.delete_by_value(34)
LL.before_node(87,94)
LL.After_node(94,44)
LL.deletebegin()
LL.printLL()