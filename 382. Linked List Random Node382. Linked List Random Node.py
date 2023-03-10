# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head

        node = self.head
        self.length = 0

        while node:
            self.length += 1
            node = node.next

    def getRandom(self) -> int:
        rand = random.randint(1,self.length)
        node = self.head
        while rand and node:
            if node.next == None:
                return node.val

            node = node.next
            rand -= 1
        return node.val

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()