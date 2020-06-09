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

    def add_to_tail(self, value):
        new_node = Node(value)

        # if queue is empty set new_node as the head
        if not self.head:
            self.head = new_node
        else:
            # start at the head
            current = self.head
            # as long as there is another node
            while current.get_next() is not None:
                # traverse the list to the end
                current = current.get_next()
            # add new_node to the end
            current.set_next(new_node)

    def remove_head(self):
        if self.head:
            # store value to return later
            value = self.head.get_value()
            # set head to the next node
            self.head = self.head.get_next()
            return value


class Queue:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.size

    def enqueue(self, value):
        self.storage.add_to_tail(value)
        self.size = self.size + 1

    def dequeue(self):
        if self.size != 0:
            value = self.storage.remove_head()
            self.size = self.size - 1
            return value
