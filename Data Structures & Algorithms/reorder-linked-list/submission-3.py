# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next

        #get fast to the end and slow to the middle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        #Start of the second list, set prev 
        second = slow.next
        #Cut first off from the second
        prev = slow.next = None
        
        
        while second:
            tmp, second.next = second.next, prev
            prev, second = second, tmp

        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2

        