#
# Author: angel suleiman
# Student Number:152961231
#
# Place the code for your lab 3 here.  Read the specs carefully.  
#
# To test, run the following command :
#     python test_lab3.py
#


class DoublyLinked:

    class Node:
        def __init__(self, data, next=None, prev=None):
            self.data = data
            self.next = next
            self.prev = prev

        def get_data(self):
            return self.data

        def get_next(self):
            return self.next

        def get_previous(self):
            return self.prev

    def __init__(self):
        self.head = None
        self.tail = None

    def get_front(self):
        return self.head

    def get_back(self):
        return self.tail

    def push_front(self, data):
        new_node = self.Node(data, self.head, None)
        if self.head:
            self.head.prev = new_node
        else:
            self.tail = new_node
        self.head = new_node

    def push_back(self, data):
        new_node = self.Node(data, None, self.tail)
        if self.tail:
            self.tail.next = new_node
        else:
            self.head = new_node
        self.tail = new_node

    def pop_front(self):
        if not self.head:
            raise IndexError("pop_front() used on empty list")
        value = self.head.data
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        else:
            self.tail = None
        return value

    def pop_back(self):
        if not self.tail:
            raise IndexError("pop_back() used on empty list")
        value = self.tail.data
        self.tail = self.tail.prev
        if self.tail:
            self.tail.next = None
        else:
            self.head = None
        return value


class Sentinel:

    class Node:
        def __init__(self, data=None, next=None, prev=None):
            self.data = data
            self.next = next
            self.prev = prev

        def get_data(self):
            return self.data

        def get_next(self):
            return self.next

        def get_previous(self):
            return self.prev

    def __init__(self):
        # Create dummy head and tail sentinels
        self.head = self.Node()
        self.tail = self.Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get_front(self):
        return self.head.next if self.head.next != self.tail else None

    def get_back(self):
        return self.tail.prev if self.tail.prev != self.head else None

    def push_front(self, data):
        node = self.Node(data, self.head.next, self.head)
        self.head.next.prev = node
        self.head.next = node

    def push_back(self, data):
        node = self.Node(data, self.tail, self.tail.prev)
        self.tail.prev.next = node
        self.tail.prev = node

    def pop_front(self):
        if self.head.next == self.tail:
            raise IndexError("pop_front() used on empty list")
        node = self.head.next
        value = node.data
        self.head.next = node.next
        node.next.prev = self.head
        return value

    def pop_back(self):
        if self.tail.prev == self.head:
            raise IndexError("pop_back() used on empty list")
        node = self.tail.prev
        value = node.data
        self.tail.prev = node.prev
        node.prev.next = self.tail
        return value
