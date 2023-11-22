"""
Category: Behavioural patter

Intent: This pattern lets us traverse elements of a collection without
exposing its underlying representation.

Problem:
    - A collection needs to provide some way of accessing its elements so
    that client code can use these elements.
    - However, adding more and more traversal algorithms to the collection
    gradually blurs its primary responsibility, which is efficient data
    storage. It's also weird to include some algorithms into a genric coll-
    ection class as some algorithms might be tailored for a specific appli-
    cation.

Solution:
    - Use the Iterator pattern to extract the traversal behaviour of a coll-
    ection into a seperate object called an iterator.

Additional points:
    - Most objects in Python have built-in iterators. Thus,
we can conveniently iterate through an array/list using `in` keyword,
    - for complex objects, such as linkedlist, tree, stack, etc., we need
    write our own way to access their elements so that client code can
    use these elements.

Implementation note:
    - We need to implement the `__iter__()` method in the iterated object
    (collection), and the `__next__()` method in the iterator.

Real-world analogy:
    to be searched later
"""
from __future__ import annotations
from collections.abc import Iterable, Iterator
from typing import List, Any


class WordsCollection(Iterable):
    def __init__(self, collection: List[Any] = []) -> None:
        self._collection = collection

    def __iter__(self) -> AlphabeticalOrderIterator:
        return AlphabeticalOrderIterator(self._collection)

    def get_reverse_iterator(self) -> AlphabeticalOrderIterator:
        return AlphabeticalOrderIterator(self._collection, True)

    def add_item(self, item: Any):
        self._collection.append(item)


class AlphabeticalOrderIterator(Iterator):
    # _position is used to store the current traversal position.
    # It depends on the particular type of collection, we might
    # have other fields for storing iteration state.
    _position: int = None
    # this attribute controls the traversal direction
    _reverse: bool = False

    def __init__(self, collection: WordsCollection,
                 reverse: bool = False) -> None:
        self._collection = collection
        self._reverse = reverse
        self._position = -1 if reverse else 0

    def __next__(self):
        """
        This is the primary method of an iterator used for fetching
        elements of the collection. The client can keep running this
        method until it does not return anything.
        """
        try:
            value = self._collection[self._position]
            self._position += -1 if self._reverse else 1
        except IndexError:
            raise StopIteration
        return value


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
    print("=" * 78)
    print("Words Collection Example")
    collection = WordsCollection()
    collection.add_item("First")
    collection.add_item("Second")
    collection.add_item("Third")

    print("Direct traversal")
    print("\n".join(collection))
    print("Reverse traversal:")
    print("\n".join(collection.get_reverse_iterator()), end="")

    print("=" * 78)
    print("Linked List Example")
    head = ListNode(1)
    head.next_ = ListNode(2)
    head.next_.next_ = ListNode(3)

    linkedlist = LinkedList(head)

    # iterate
    for i in linkedlist:
        print(i)
