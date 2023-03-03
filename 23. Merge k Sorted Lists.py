# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

        # solultion 01 
# class Solution:
#     def mergeKLists(self, lists):
#         arr = []
#         for i in range(len(lists)):
#              head = lists[i]
#              while head:
#                  arr.append(head.val)
#                  head = head.next
        
#         arr.sort()
#         dummy = ListNode(0)
#         temp = dummy
#         for i in range(len(arr)):
#             node = ListNode(arr[i])
#             temp.next = node
#             temp = temp.next
        
#         return dummy.next

        # solution 02

class Solution:
    def mergeKLists(self, lists):
        def merge(l1,l2):
            dummy = ListNode()
            tail = dummy
            while l1 and l2:
                if l1.val<=l2.val:
                    tail.next = l1
                    l1 = l1.next
                else:
                    tail.next = l2
                    l2 = l2.next
                tail = tail.next
            if l1:
                tail.next = l1
            if l2:
                tail.next = l2
            return dummy.next


        if not lists or len(lists)==0:
            return None

        while len(lists)>1:
            mergedLists = []
            
            i = 0
            while i<len(lists):
                l1 = lists[i]
                l2 = lists[i+1] if i+1<len(lists) else None
                mergedLists.append(merge(l1,l2))
                i = i+2
        
            lists = mergedLists
        
        return lists[0]

