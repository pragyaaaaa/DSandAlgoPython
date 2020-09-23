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

    # reverse in pairs
    def rev_in_pairs(self):
        temp = self.head
        while None != temp and None != temp.next:
            self.swap_data(temp, temp.next)
            temp = temp.next.next

    def swap_data(self, a, b):
        tmp = a.data
        a.set_data(b.data)
        b.set_data(tmp)

    # middle of linked list
    def mid_of_sll(self):
        fast_ptr = self.head
        slow_ptr = self.head
        while fast_ptr != None:
            fast_ptr = fast_ptr.next
            if fast_ptr == None:
                return slow_ptr
            fast_ptr = fast_ptr.next
            slow_ptr = slow_ptr.next
        return slow_ptr

    # merge sorted LLs
    def merge_sorted(self, list_1, list_2):
        temp = Node(0)
        pointer = temp
        while list_1 != None and list_2 != None:
            if list_1.data < list_2.data:
                pointer = list_1
                list_1 = list_1.next
            else:
                pointer = list_2
                list_2 = list_2.next
            pointer = pointer.next
        if list_1 == None:
            pointer = list_2
        else:
            pointer = list_1
        return temp.next
