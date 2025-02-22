''' Singly Linkedlist'''

class Node :

    def __init__(self,data = None,next=None):

        self.data=data
        self.next=next

class LinkedList:

    def __init__(self):
        self.head=None

    def insert_at_begning(self,data):
        node=Node(data,self.head)
        self.head=node

    def insert_at_end(self,data):
        if self.head is None:
            self.head=Node(data,None)

        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next =  Node(data)


        
    def print(self):
        itr=self.head
        llstr=''
        while itr:
            suffix =''
            if itr.next:
                suffix='--->'
            llstr += str(itr.data) + suffix
            itr = itr.next
        print(llstr)

    def get_length(self):

        count=0
        itr=self.head
        while itr:
            count += 1
            itr=itr.next
        return count

    def insert_at(self,index,data):

        if index <0 or index > self.get_length():
            raise Exception( 'Invalid index')
        if index == 0:
            self.insert_at_begning(data)

        itr = self.head
        counter = 0
        while itr:
    
            if counter == index -1 :
                node = Node(data,itr.next)
                itr.next=node
            itr = itr.next
            counter += 1

    def remove_at(self,index):

        if index <0 or index > self.get_length():
            raise Exception( 'Invalid index')
        if index == 0:
            self.head = self.head.next
            return

        itr = self.head
        counter = 0
        while itr: 
            if counter == index - 1 :
                itr.next = itr.next.next
                break
            itr = iter.next
            counter += 1


ll=LinkedList()
ll.insert_at_begning(10)
ll.insert_at_end(50)
ll.insert_at_end(100)
ll.insert_at_end(150)
ll.print()
ll.insert_at(3,5)
ll.print()
ll.remove_at(3)
ll.print()

    


