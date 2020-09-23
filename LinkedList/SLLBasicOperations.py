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

    # delete from begin
    def delete_from_begin(self):
        if self.length == 0:
            print("The list is empty.")
        else:
            self.head = self.head.next
            self.length += 1

    # deleting last node
    def delete_from_end(self):
        if self.length == 0:
            print("The list is empty")
        else:
            current_node = self.head
            previous_node = self.head
            while current_node != None:
                previous_node = current_node
                current_node = current_node.next
            previous_node.next = None
            self.length -= 1

    # deleting by node
    def delete_with_node(self, node):
        if self.length == 0:
            print("The list is empty.")
        else:
            current_node = self.head
            previous_node = None
            found = False
            while not found:
                if current_node == node:
                    found = True
                elif current_node is None:
                    raise ValueError("Node not in LL")
                else:
                    previous_node = current_node
                    current_node = current_node.next
            if previous_node is None:
                self.head = current_node.next
            else:
                previous_node = current_node.next
            self.length -= 1

    # deleting with data
    def delete_by_data(self, val):
        current_node = self.head
        previous_node = self.head
        while current_node.next != None or current_node.data != val:
            if current_node.data == val:
                previous_node.next = current_node.next
                self.length -= 1
                return
            else:
                previous_node = current_node
                current_node = current_node.next
            print("Value is not in LL.")

    # deleting with position
    def delete_by_pos(self, pos):
        count = 0
        current_node = self.head
        previous_node = self.head
        if pos > self.length or pos < 0:
            print("Invalid position")
        else:
            while current_node.next != None or count < pos:
                count = count + 1
                if count == pos:
                    previous_node.next = current_node.next
                    self.length -= 1
                    return
                else:
                    previous_node = current_node
                    current_node = current_node.next

    # reclaim memory in Python
    def clear(self):
        self.head = None
