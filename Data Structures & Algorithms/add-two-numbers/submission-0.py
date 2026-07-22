# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ll1 = []
        ll2 = []
        temp1 = l1
        while temp1:
            ll1.append(str(temp1.val))
            temp1 = temp1.next
        temp2 = l2
        while temp2:
            ll2.append(str(temp2.val))
            temp2 = temp2.next
        ll1 = list(reversed(ll1))
        ll2 = list(reversed(ll2))

        ll1 = int("".join(ll1))
        ll2 = int("".join(ll2))
        ll3 = str(ll1+ll2)
        l3 =[int(x) for x in ll3]
        l3 = list(reversed(l3))
        n = len(l3)
        i = 0

        head = ListNode(l3[0])
        current = head
        for i in range(1, len(l3)):
            current.next = ListNode(l3[i])
            current = current.next
        return head
