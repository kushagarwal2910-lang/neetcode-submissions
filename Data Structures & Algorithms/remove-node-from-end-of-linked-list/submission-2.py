# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None
        temp1 = head
        l = 0
        while temp1:
            l +=1
            temp1 = temp1.next
        n = l-n

        dummy = ListNode(0, head)
        prev = dummy
        temp = head
        e = 0
        while temp and e!=n:
            e+=1
            prev = temp
            temp = temp.next
        
        prev.next = temp.next
        return dummy.next

