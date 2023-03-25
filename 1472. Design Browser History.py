class ListNode:
    def __init__(self,val=0,pre=None,nxt=None):
        self.pre = pre
        self.val = val
        self.nxt = nxt

class BrowserHistory:

    def __init__(self, homepage: str):
        self.curr = ListNode(homepage)


    def visit(self, url: str) -> None:

        node = ListNode(url)
        node.pre = self.curr
        self.curr.nxt = node
        self.curr = node


    def back(self, steps: int) -> str:
        while steps and self.curr.pre:
            self.curr = self.curr.pre
            steps -= 1
        return self.curr.val


    def forward(self, steps: int) -> str:
        while steps and self.curr.nxt:
            self.curr = self.curr.nxt
            steps -= 1
        return self.curr.val
        



# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)