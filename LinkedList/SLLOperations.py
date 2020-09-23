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
