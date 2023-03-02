# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # find the size of the list
        temp = head
        length = 0
        while temp:
            length += 1
            temp = temp.next

        nth = length - n
        count = 0
        temp = head

        if nth==0:
            head = temp.next
            return head

        while temp:
            count += 1
            if count==nth:
                break
            temp = temp.next
        
        temp.next = temp.next.next
        return head
        
            
