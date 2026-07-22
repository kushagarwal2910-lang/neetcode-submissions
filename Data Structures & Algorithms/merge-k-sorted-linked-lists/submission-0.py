# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        l = []

        if not lists:
            return None

        for i in lists:
            temp = i
            while temp:
                l.append(temp.val)
                temp = temp.next
        l = sorted(l)

        head = ListNode(l[0])
        current = head
        for i in range(1, len(l)):
            current.next = ListNode(l[i])
            current = current.next
        return head