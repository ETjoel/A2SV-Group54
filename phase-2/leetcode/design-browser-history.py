class Node:
    def __init__(self, page: str):
        self.page = page
        self.prev = None
        self.next = None

class BrowserHistory:

    def __init__(self, homepage: str):
        self.home = Node(homepage)

    def visit(self, url: str) -> None:
        newNode = Node(url)
        self.home.next = newNode
        newNode.prev = self.home
        self.home = newNode

    def back(self, steps: int) -> str:
        curr = self.home
        while curr and curr.prev and steps > 0:
            curr = curr.prev
            steps-=1
        self.home = curr
        return curr.page

    def forward(self, steps: int) -> str:
        curr = self.home
        while curr and curr.next and steps > 0:
            curr = curr.next
            steps-=1
            if steps == 0:
                self.home = curr
                return curr.page
        self.home = curr
        return curr.page


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)