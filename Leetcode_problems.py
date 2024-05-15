from typing import Optional, List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class LinkedList:
    def __init__(self,lst=[]):
        self.head = None
        self.lst2ll(lst)

    def lst2ll(self, lst: List[int]):
        if not lst:  # Check if the list is empty
            return None
        self.head = ListNode(lst[0])
        cur = self.head
        for item in lst[1:]:
            cur.next = ListNode(item)
            cur = cur.next
        return self.head

    def ll_print(self):
        cur = self.head
        while cur:
            print(cur.val, end="->")
            cur = cur.next
        print("None")

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def ll2int(ll:LinkedList):  
            cur=ll.head
            pow_count=0
            res=0
            while(cur):
                res+= cur.val*(10**pow_count)
                cur=cur.next
                pow_count+=1
            return res
        res=str(ll2int(l1)+ll2int(l2))
        # for _ in 
        return 

l1, l2 = [2, 4, 3], [5, 6, 4]
# Create instances of LinkedList
ll1,ll2 = LinkedList(l1),LinkedList(l2)
# Print the linked lists
ll1.ll_print();ll2.ll_print()
print(Solution().addTwoNumbers(ll1,ll2))