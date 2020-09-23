from LinkedList.SLLNode import Node


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

    # inserting node in beginning of the list
    def insert_at_begin(self, data):
        new_node = Node()
        new_node.data = data
        if self.length == 0:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    # inserting node at the end of the list
    def insert_at_end(self, data):
        new_node = Node()
        new_node.data = data
        current = self.head
        while current.next != Node:
            current = current.next
        current.next = new_node
        self.length += 1

    # inserting at given position
    def insert_at_pos(self, data, pos):
        if pos > self.length or pos < 0:
            return None
        else:
            if pos == 0:
                self.insert_at_begin(data)
            else:
                if pos == self.length:
                    self.insert_at_end(data)
                else:
                    new_node = Node()
                    new_node.data = data
                    count = 1
                    current = self.head
                    while count < pos - 1:
                        count += 1
                        current = current.next
                    new_node.next = current.next
                    current.next = new_node
                    self.length += 1
