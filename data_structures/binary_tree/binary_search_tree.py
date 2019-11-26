# =============================================================================
# Author: falseuser
# Created Time: 2019-11-05 11:33:10
# Last modified: 2019-11-05 15:39:38
# Description: 二叉搜索树
# =============================================================================


class Node():

    def __init__(self, key, parent):
        self.key = key
        self.parent = parent
        self.left = None
        self.right = None

    def is_root(self):
        return not self.parent

    def is_leaf(self):
        return not (self.left or self.right)

    def is_right_child(self):
        if self.parent is not None and self.parent.right == self:
            return True
        else:
            return False

    def has_left_child(self):
        return bool(self.left)

    def has_right_child(self):
        return bool(self.right)

    def __repr__(self):
        return "Node({})".format(self.key)


class BinarySearchTree():

    def __init__(self):
        self.root = None

    def is_empty(self):
        return not bool(self.root)

    def get_max(self, root=None):
        if root is not None:
            current = root
        else:
            current = self.root
        if not self.is_empty():
            while current.has_right_child():
                current = current.right
        return current

    def get_min(self, root=None):
        if root is not None:
            current = root
        else:
            current = self.root
        if not self.is_empty():
            while current.has_left_child():
                current = current.left
        return current

    def get_node(self, key):
        current = None
        if not self.is_empty():
            current = self.root
            while current is not None and current.key != key:
                if key < current.key:
                    current = current.left
                else:
                    current = current.right
        return current

    def reassign_node(self, node, new_child):
        if new_child is not None:
            new_child.parent = node.parent
        if node.parent is not None:
            if node.is_right_child():
                node.parent.right = new_child
            else:
                node.parent.left = new_child

    def insert(self, key):
        node = Node(key, None)
        if self.is_empty():
            self.root = node
        else:
            current = self.root
            # 找到节点的parent节点
            while current is not None:
                parent = current
                if node.key < current.key:
                    current = current.left
                else:
                    current = current.right
            if node.key < parent.key:
                parent.left = node
            else:
                parent.right = node
            node.parent = parent

    def delete(self, key):
        if not self.is_empty():
            node = self.get_node(key)
            if node is not None:
                if node.left is None and node.right is None:
                    self.reassign_node(node, None)
                elif node.left is None and node.right is not None:
                    self.reassign_node(node. node.right)
                elif node.left is not None and node.right is None:
                    self.reassign_node(node, node.left)
                else:
                    max_node = self.get_max(node.left)
                    self.delete(max_node.key)
                    # 把左子树最大节点替换到要删除的节点位置
                    node.key = max_node.key

    def order_traversal(self, node):
        nodes = []
        if node is not None:
            nodes.insert(0, node)
            nodes = nodes + self.order_traversal(node.left)
            nodes = nodes + self.order_traversal(node.right)
        return nodes

    def traversal(self):
        return self.order_traversal(self.root)


if __name__ == "__main__":
    t = BinarySearchTree()
    t.insert(8)
    t.insert(4)
    t.insert(7)
    t.insert(2)
    t.insert(9)
    t.insert(5)
    t.insert(18)
    t.insert(11)
    t.insert(3)
    print(t.traversal())
    t.delete(18)
    print(t.traversal())
