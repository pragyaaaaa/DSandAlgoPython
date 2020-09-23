class Node:

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def set_data(self, data):
        self.data = data

    def get_data(self):
        return self.data

    def set_next(self, next):
        self.next = next

    def get_next(self):
        return self.next

    def has_next(self):
        return self.next != None


class SinglyLinkedList(object):

    def __init__(self, node=None):
        self.length = 0
        self.head = node

    def length(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.next
        return count
