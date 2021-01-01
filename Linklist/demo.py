class Node:
    def __init__(self,data,next,prev):
        self.data = data
        self.next = next
        self.prev = prev

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_ele_beggining(self,data):
        node = Node(data,self.head)
        self.head=node

    def print_ele_fwd(self):

        if self.head is None:
            print("list is empty")
            return

        itr = self.head
        listr = ''
        while itr:
            listr += str(itr.data) + '-->'
            itr = itr.next
        print(listr)

        def print_backward(self):

            if self.tail is None:
                print("list is empty")
                return

            itr = self.tail
            listr = ''
            while itr:
                listr += str(itr.data) + '-->'
                itr = itr.prev
            print(listr)

    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data,None)
            return

        itr = self.head

        while itr.next:
            itr = itr.next

        itr.next = Node(data,None)

    def insert_values(self,data_list):
        for data in data_list:
            #self.insert_ele_beggining(data)
            self.insert_at_end(data)

    def get_length(self):
        count = 0
        itr = self.head

        while itr:
            itr = itr.next
            count+=1
        return count

    def remove_at(self,index):
        if index<0 or index>=self.get_length():
            print("invalid index")
            raise Exception("invalid index")

        if index == 0:
            self.head=self.head.next
            return


        count = 0

        itr = self.head

        while itr:
            if count == index -1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count+=1

    def insert_at(self,index,data):
        if index < 0 or index >= self.get_length():
            print("invalid index")
            raise Exception("invalid index")

        if index == 0:
            self.head = Node(data,index)
            return

        count = 0

        itr = self.head

        while itr.next:
            if count == index-1:
                itr.next=Node(data,itr.next)
                break


            itr = itr.next
            count+=1



    def remove_by_Value (self,data):

        if self.head.data is None:
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        itr = self.head
        while itr.next:
            if itr.next.data == data:
                itr.next = itr.next.next
                break
            itr = itr.next


    def insert_by_value(self,data_after,data_to_insert):
        if self.head is None:
            return

        if self.head.data==data_after:
            self.head.next = Node(data_to_insert,self.head.next)
            return

        itr = self.head

        while itr:
            if itr.data == data_after:
                itr.next=Node(data_to_insert,itr.next)
                break

            itr = itr.next







ll = LinkedList()
#ll.insert_ele_beggining(23)
#ll.insert_ele_beggining(34)
#ll.insert_at_end(89)
ll.insert_values(['spoorthi','raj','jnana','supriya'])

#ll.get_length()
#ll.remove_at(0)
#ll.insert_at(3,'raja')
#ll.remove_by_Value('raj')
#ll.insert_by_value('jnana','puttu')
#ll.print_ele()

