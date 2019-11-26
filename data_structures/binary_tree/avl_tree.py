# =============================================================================
# Author: falseuser
# Created Time: 2019-11-05 16:02:43
# Last modified: 2019-11-07 11:43:10
# Description: AVL自平衡二叉查找树
# =============================================================================


class Node():

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

    def has_left_child(self):
        return True if self.left is not None else False

    def has_right_child(self):
        return True if self.right is not None else False

    def __repr__(self):
        return "Node({})".format(self.key)


class AVLTree():

    def __init__(self):
        self.root = None

    def is_empty(self):
        return not bool(self.root)

    def get_height(self, node):
        if node is not None:
            return node.height
        else:
            return 0

    def add_height(self, node):
        node.height = max(
            self.get_height(node.left),
            self.get_height(node.right)
        ) + 1

    def right_rotate(self, node):
        # 右旋为修复LL型不平衡现象的旋转为
        # 原node节点旋转后变成new_root的右子节点
        new_root = node.left
        node.left = new_root.right
        new_root.right = node
        self.add_height(node)
        self.add_height(new_root)
        return new_root

    def left_rotate(self, node):
        new_root = node.right
        node.right = new_root.left
        new_root.left = node
        self.add_height(node)
        self.add_height(new_root)
        return new_root

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if node is None:
            return Node(key)
        if key < node.key:
            node.left = self._insert(node.left, key)
            if self.get_height(node.left) - self.get_height(node.right) == 2:
                if key < node.left.key:  # LL
                    node = self.right_rotate(node)
                else:  # LR
                    node.left = self.left_rotate(node.left)
                    node = self.right_rotate(node)
        else:
            node.right = self._insert(node.right, key)
            if self.get_height(node.right) - self.get_height(node.left) == 2:
                if key > node.right.key:  # RR
                    node = self.left_rotate(node)
                else:  # RL
                    node.right = self.right_rotate(node.right)
                    node = self.left_rotate(node)

        self.add_height(node)
        return node

    def get_min_key(self, node):
        # 找到子树最小值
        while node.has_left_child():
            node = node.left
        return node.key

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        if node is None:
            return None
        if key == node.key:
            if node.left is not None and node.right is not None:
                min_key = self.get_min_key(node.right)
                # 将删除node节点改成删除min_key的节点
                node.key = min_key
                node.right = self._delete(node.right, min_key)
            elif node.left is not None:  # node.right is None
                node = node.left
            else:
                node = node.right   # None or else
        elif key < node.key:
            if not node.has_left_child():
                return node
            else:
                node.left = self._delete(node.left, key)
        elif key > node.key:
            if not node.has_right_child():
                return node
            else:
                node.right = self._delete(node.right, key)

        if node is None:
            return None

        if self.get_height(node.left) - self.get_height(node.right) == 2:
            left = node.left
            right = node.right
            if self.get_height(left.left) > self.get_height(left.right):
                node = self.right_rotate(node)
            else:
                node.left = self.left_rotate(node.left)
                node = self.right_rotate(node)
        elif self.get_height(node.right) - self.get_height(node.left) == 2:
            left = node.left
            right = node.right
            if self.get_height(right.left) > self.get_height(right.right):
                node.right = self.right_rotate(node.right)
                node = self.left_rotate(node)
            else:
                node = self.left_rotate(node)
        self.add_height(node)
        return node

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
    t = AVLTree()
    t.insert(4)
    t.insert(8)
    t.insert(6)
    t.insert(3)
    t.insert(7)
    t.insert(8)
    print(t.traversal())
    t.delete(3)
    print(t.traversal())
