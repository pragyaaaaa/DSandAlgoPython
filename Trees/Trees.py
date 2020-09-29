class BinaryTree(object):
    def __init__(self, root):
        self.value = root
        self.left_child = None
        self.right_child = None

    def insert_left_child(self, new_node):
        if self.left_child == None:
            self.left_child = BinaryTree(new_node)
        else:
            temp = BinaryTree(new_node)
            temp.left_child = self.left_child
            self.left_child = temp

    def insert_right_child(self, new_node):
        if self.right_child == None:
            self.right_child = BinaryTree(new_node)
        else:
            temp = BinaryTree(new_node)
            temp.right_child = self.right_child
            self.right_child = temp

    def get_right_child(self):
        return self.right_child

    def get_left_child(self):
        return self.left_child

    def set_root_value(self, val):
        self.value = val

    def get_root_value(self):
        return self.value


r = BinaryTree('a')
r.insert_left_child('b')
r.insert_left_child('c')
r.insert_right_child('d')
print(r.get_left_child().get_root_value())
