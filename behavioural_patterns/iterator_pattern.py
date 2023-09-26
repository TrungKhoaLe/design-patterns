"""
Category: Behavioural patter

Intent: This pattern lets us traverse elements of a collection without
exposing its underlying representation.

Additional points:
    - Most objects in Python have built-in iterators. Thus,
we can conveniently iterate through an array/list using `in` keyword,
    - for complex objects, such as linkedlist, tree, stack, etc., we need
    write our own way to access their elements so that client code can
    use these elements.

Real-world analogy:
    to be searched later
"""


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next_ = None


class LinkedList:
    def __init__(self, head):
        self.head = head
        self.cur = None

    def __iter__(self):
        self.cur = self.head
        return self

    def __next__(self):
        if self.cur:
            val = self.cur.val
            self.cur = self.cur.next_
            return val
        else:
            raise StopIteration


if __name__ == "__main__":
    head = ListNode(1)
    head.next_ = ListNode(2)
    head.next_.next_ = ListNode(3)

    linkedlist = LinkedList(head)

    # iterate
    for i in linkedlist:
        print(i)
