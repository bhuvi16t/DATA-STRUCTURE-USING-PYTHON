# Implement singly linked list Data structure 
 
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = None


class SinglyLinkList:
    def __init__(self, start=None):
        self.start = start

    def Is_Empty(self):
        return self.start is None

    def Insert_at_Start(self, data):
        new_node = Node(data, self.start)
        self.start = new_node

    def Insert_at_last(self, data):
        new_node = Node(data)
        if not self.Is_Empty():  # If the list is not empty
            temp = self.start
            while temp.next is not None:  # Traverse until the last node
                temp = temp.next
            temp.next = new_node
        else:
            self.start = new_node  # If the list is empty

    def Search(self, data):
        temp = self.start
        while temp is not None:
            if temp.data == data:
                return temp
            temp = temp.next
        return None

    def Insert_after(self, temp, data):
        if temp is not None:
            new_node = Node(data, temp.next)
            temp.next = new_node

    def print_list(self):
        temp = self.start
        while temp is not None:
            print(temp.data, end="$-->")
            temp = temp.next
        print()  # Newline after the list

    def delete_first(self) :
        if self.start is not None :
            self.start = self.start.next

    def delete_last(self) :
        if self.start is None :
            pass
        elif self.start.next is None :
            self.start.next = None

        else :
            temp = self.start
            while temp.next.next is not  None:
                temp = temp.next 
            temp.next= None
   
    def delete_item(self,data):
        if self.start is None :
            pass
        elif self.start.next is None:
            if self.start.data == data :
                self.start =None
        else : 
            temp = self.start
            if temp.data == data :
                self.start = temp.next
            else :
                while temp.next.item == data :
                    if temp.next.data==data :
                        temp.next=temp.next.next
                        break
                    temp = temp.next




# Testing the corrected implementation
my_list = SinglyLinkList()
my_list.Insert_at_Start(10) # Insert 10 at the start
my_list.Insert_at_Start(20)
my_list.Insert_after(my_list.Search(20),25)  # Insert 20 at the start
my_list.Insert_at_last(30)   # Insert 30 at the end
my_list.Insert_at_last(40) 
my_list.Insert_after(my_list.Search(40),45)
my_list.delete_item(25)
my_list.print_list()





    
