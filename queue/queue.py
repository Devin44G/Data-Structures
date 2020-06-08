"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order.

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when
   implementing a Queue?

Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""

# class Queue:
#     def __init__(self):
#         self.size = 0
#         self.storage = []
#
#     def __len__(self):
#         return self.size
#
#     def enqueue(self, value):
#         self.storage.insert(0, value)
#         self.size = len(self.storage)
#
#     def dequeue(self):
#         if self.storage != []:
#             value = self.storage.pop()
#             self.size = len(self.storage)
#             return value


# from guided project
class Node:
    def __init__(self, value=None, next_node=None):
        # value at this node
        self.value = value
        # reference to the next node in the list of nodes
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        # set this node's next reference to the passed in node
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        # first node in the list
        self.head = None
        # last node in the list
        self.tail = None

    def add_to_head(self, value):
        new_node = Node(value)
        # what if the list is empty?
        if not self.head and not self.tail:
            # set both head and tail to new_node
            self.head = new_node
            self.tail = new_node
        # what if the list isn't empty?
        else:
            self.tail.set_next(self.head)
            self.head = new_node

    def remove_tail(self):
        if self.tail is None:
            return None
        else:
            self.tail = self.tail.get_value()
            return self.tail


class Queue:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.size

    def enqueue(self, value):
        self.storage.add_to_head(value)
        self.size = self.size + 1

    def dequeue(self):
        if self.size != 0:
            value = self.storage.remove_tail()
            self.size = self.size - 1
            return value
