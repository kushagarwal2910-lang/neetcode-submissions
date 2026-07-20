# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l = []
        temp1 = list1
        while temp1:
            l.append(temp1.val)
            temp1 = temp1.next
        temp2 = list2
        while temp2:
            l.append(temp2.val)
            temp2 = temp2.next
        l = sorted(l)
        if not l:
            return None
        head = ListNode(l[0])
        temp = head
        for i in range(1,len(l)):
            if i==len(l)-1:
                temp.next = None
            temp.next = ListNode(l[i])
            temp = temp.next
        return head
        