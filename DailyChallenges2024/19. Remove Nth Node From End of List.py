# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def getLength(node):
            cnt = 1
            while node.next:
                cnt += 1
                node = node.next
            return cnt
        
        if getLength(head)<=n:
            return head.next
        n = getLength(head) - n + 1
        
        cnt = 1
        tempHead = head
        prev = head
        while head.next and cnt<n:
            cnt += 1
            prev = head
            head = head.next
        prev.next = head.next
        
        return tempHead