class ListNode:

   def __init__(self, val=0, next=None):
       self.val = val
       self.next = next


class Solution:

    def __init__(self, val=0):
         self.val = val



    def merge(self, l1: ListNode, l2: ListNode) -> ListNode:

        temp = dummy = ListNode(0)

        if l1 is None:
            return l2
        elif l2 is None:
            return l1

        while(l1 and l2):
            if (l1.val < l2.val):
                temp.next = l1
                l1 = l1.next
            else:
                temp.next = l2
                l2 = l2.next
                temp = temp.next
        if(l1):
            temp.next=l1
        if(l2):
            temp.next=l2





        return dummy.next





ml=Solution()
res = ml.merge([1,2,3] ,[1,3,4])
