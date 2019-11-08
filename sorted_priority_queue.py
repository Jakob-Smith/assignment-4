from _queue import Empty
from priority_queue_base import PriorityQueueBase
from positional_list import PositionalList

"""The following classes (above) were taken from in class examples"""
class SortedPriorityQueue(PriorityQueueBase):  # base class defines _Item
    """A min-oriented priority queue implemented with a sorted list."""

    def __init__(self):
        """Create a new empty Priority Queue."""
        self.data = PositionalList()

    def __len__(self):
        """Return the number of items in the priority queue."""
        return len(self.data)

    """The add function uses insertion sort to add a key-value pair to the sorted priority queue"""

    def add(self, key, value):
        """Add a key-value pair."""
        newest = self._Item(key, value)
        walk = self.data.last()
        while walk is not None and newest < walk.element():
            walk = self.data.before(walk)
        if walk is None:
            self.data.add_first(newest)
        else:
            self.data.add_after(walk, newest)

    def min(self):
        """Return but do not remove (k,v) tuple with minimum key.

        Raise Empty exception if empty.
        """
        p = self.data.first()
        item = p.element()
        return item._key, item._value

    def remove_min(self):
        if self.is_empty():
            print("priority Queue is empty")
            return
        item = self.data.delete(self.data.first())
        return item._value

    def __iter__(self):
        """Generate iteration of the map's keys."""
        for item in self.data:
            yield item  # yield the KEY


test = SortedPriorityQueue()
test.add(1, 3)
test.add(4, 2)
test.add(2, 1)
test.add(3, 4)

for i in test:
    print(i, end=' ')


