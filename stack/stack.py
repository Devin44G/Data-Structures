
"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order.

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when
   implementing a Stack?
"""
# class Stack:
#     def __init__(self):
#         self.size = 0
#         self.storage = []
#
#     def __len__(self):
#         return self.size
#
#     def push(self, value):
#         self.storage.append(value)
#         self.size = len(self.storage)
#
#     def pop(self):
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

    # we don't have access to the end of the linked list
    # when we want to add to the end, we need to traverse the whole linked list to get to the end
    # O(n) - linear

    # we have direct access to end of the list so we can add nodes to it directly
    def add_to_tail(self, value):
        # regardless of if the list is empty or not, we need to wrap the value in a Node
        new_node = Node(value)
        # what if the list is empty?
        if not self.head and not self.tail:
            # set both head and tail to new_node
            self.head = new_node
            self.tail = new_node
        # what if the list isn't empty?
        else:
            # set the current tail's next to the new node
            self.tail.set_next(new_node)
            # set self.tail to the new node
            self.tail = new_node

    def remove_tail(self):
        if self.head is None:
            return None
        else:
            self.head = self.head.get_value()
            return self.head


class Stack:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.size

    def push(self, value):
        self.storage.add_to_tail(value)
        self.size = self.size + 1

    def pop(self):
        if self.size > 0:
            self.size = self.size - 1
            self.storage.remove_tail()
