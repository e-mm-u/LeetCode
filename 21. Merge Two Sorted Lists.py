# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1, list2):
        merged_ll_head = ListNode()
        merged_ll = merged_ll_head

        while list1 and list2:
            if(list1.val<list2.val):
                merged_ll.next = list1
                list1 = list1.next
            else:
                merged_ll.next = list2
                list2 = list2.next
            
            merged_ll = merged_ll.next
        
        if list1 :
            merged_ll.next = list1
        if list2:
            merged_ll.next = list2

        return merged_ll_head.next

test = Solution()
list1 = [1,2,4]
list2 = [1,3,4]
print(test.mergeTwoLists(list1, list2))