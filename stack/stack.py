
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



class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next_node = next

    def get_value(self):
        # returns the node's data
        return self.value

    def get_next(self):
        # returns the thing pointed at by this node's `next` reference
        return self.next_node

    def set_next(self, new_next):
        # sets this node's `next` reference to `new_next`
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        # the first Node in the LinkedList
        self.head = None
        # the last Node in the LinkedList
        self.tail = None

    def add_to_tail(self, data):
        # wrap the `data` in a Node instance
        new_node = Node(data)
        # what about the empty case, when both self.head = None and self.tail = None?
        if not self.head and not self.tail:
            # list is empty
            # update both head and tail to point to the new node
            self.head = new_node
            self.tail = new_node
        # non-empty linked list case
        else:
            # call set_next with the new_node on the current tail node
            self.tail.set_next(new_node)
            # update self.tail to point to the new last Node in the linked list
            self.tail = new_node

    def remove_tail(self):
        # if the linked list is empty
        if self.tail is None:
            return None
        # save the tail Node's data
        data = self.tail.get_value()
        # both head and tail refer to the same Node
        # there's only one Node in the linked list
        if self.head is self.tail:
            # set both to be None
            self.head = None
            self.tail = None
        else:
            current = self.head
            while current.get_next() != self.tail:
                current = current.get_next()
            # `current` is now pointing at the Node right
            # before the tail Node
            self.tail = None
            self.tail = current
            # self.tail.set_next(None)

        return data

    def remove_head(self):
        if self.head is None:
            return None
        # save the head Node's data
        data = self.head.get_value()
        # both head and tail refer to the same Node
        # there's only one Node in the linked list
        if self.head is self.tail:
            # set both to be None
            self.head = None
            self.tail = None
        else:
            # we have more than one Node in the linked list
            # delete the head Node
            # update `self.head` to refer to the Node after the Node we just deleted
            self.head = self.head.get_next()

        return data


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
            return self.storage.remove_tail()
        else:
            return None
