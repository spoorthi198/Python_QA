class Node:
    def __init__(self,data,next):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beggining(self,data):
        node = Node(data,self.head)
        self.head = node

    def print_the_ele(self):
        if self.head is None:
            print("linked list is empty")
            return

        itr = self.head
        listr = ' '
        while itr:
            listr += str(itr.data)+ '-->'
            itr = itr.next


        print(listr)

    def insert_at_end(self,data):
        if self.head is None:
            self.head=Node(data,None)
            return

        itr = self.head

        while itr.next:
            itr = itr.next

        itr.next=Node(data,None)

    def insert_values(self,data_list):
        if self.head is None:
            for data in data_list:
                self.insert_at_end(data)

    def get_length(self):
        count = 0
        itr = self.head

        while itr:
            itr = itr.next
            count += 1
        return count


    def remove_at(self,index):
        if index<0 or index >= self.get_length():
            print("not valid index")
            raise Exception("invalid index")

        if index==0:
            self.head=self.head.next
            return

        count = 0
        itr = self.head

        while itr:
            if count == index - 1:
                itr.next=itr.next.next
                break

            itr = itr.next
            count+=1
    def insert_at(self,index,data):
        if index<0 or index>=self.get_length():
            print("invalid index")
            raise Exception("invalid index")
        if index==0:
            self.insert_at_beggining(data)
            return

        count= 0
        itr = self.head
        while itr:
            if count== index-1:
                node = Node(data,itr.next)
                itr.next=node
            itr = itr.next
            count+=1

ll = LinkedList()

ll.insert_values(['raj','jnana','jayamm','puttamma'])
ll.remove_at(2)
ll.print_the_ele()

ll.get_length()



