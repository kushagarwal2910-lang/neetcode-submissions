# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        temp = head
        d = {}
        while temp:
            if temp in d:
                return True
            else:
                d[temp] = 1
            if temp.next == None:
                return False
            temp = temp.next
        return False