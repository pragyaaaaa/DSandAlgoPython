from LinkedList.SLLNode import Node


class SinglyLinkedList(object):

    def __init__(self, node=None):
        self.length = 0
        self.head = node

    # reverse a SLL
    def reverse_list_iter(self):
        previous_node = None
        current_node = self.head
        while current_node is not None:
            next_node = current_node.next
            current_node = previous_node
            previous_node = current_node
            current_node = next_node
        self.head = previous_node

    def reverse_list_rec(self, node):
        if None != node:
            right = node.next
        if self.head != node:
            node = self.head
            self.head = node
        else:
            node = None
            self.reverse_list_rec(right)
