# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        l = []
        m = []
        tem = head
        while tem:
            l.append(tem.val)
            tem = tem.next
        
        for i in range(0,len(l),k):
            if i+k > len(l):
                m.append(l[i:])
                break
            m.append(l[i:i+k][::-1])

        l[:] = []
        for sublist in m:
            for item in sublist:
                l.append(item)
        
        main = ListNode(l[0])
        current = main

        for i in range(1, len(l)):
            current.next = ListNode(l[i])
            current = current.next
        
        return main