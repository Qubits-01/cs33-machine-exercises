def main():
    my_AVL_tree = AVLTree()
    root = None
    temp_input = None

    while True:
        temp_input = int(input())
        if temp_input == 0:
            break

        root = my_AVL_tree.insert(root, temp_input)
        my_AVL_tree.print_preorder(root)
        print()


class BinaryTreeNode(object):
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


class AVLTree(object):
    def insert(self, root, key):
        # Determine where to insert the node.
        if not root:
            return BinaryTreeNode(key)
        elif key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        # Balance the tree (if needed).
        balance_factor = self.get_balance_factor(root)
        if balance_factor > 1:
            if key < root.left.key:
                return self.right_rotate(root)
            else:
                root.left = self.left_rotate(root.left)
                return self.right_rotate(root)

        if balance_factor < -1:
            if key > root.right.key:
                return self.left_rotate(root)
            else:
                root.right = self.right_rotate(root.right)
                return self.left_rotate(root)

        return root

    def delete(self, root, key):
        if not root:
            return root
        elif key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp

            temp = self.get_min_value_node(root.right)
            root.key = temp.key
            root.right = self.delete(root.right, temp.key)

        if root is None:
            return root

        # Update the balance factor (if needed).
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        balance_factor = self.get_balance_factor(root)

        if balance_factor > 1:
            if self.get_balance_factor(root.left) >= 0:
                return self.right_rotate(root)
            else:
                root.left = self.left_rotate(root.left)
                return self.right_rotate(root)

        if balance_factor < -1:
            if self.get_balance_factor(root.right) <= 0:
                return self.left_rotate(root)
            else:
                root.right = self.right_rotate(root.right)
                return self.left_rotate(root)

        return root

    # Left rotation.
    def left_rotate(self, alpha):
        beta = alpha.right
        temp = beta.left
        beta.left = alpha
        alpha.right = temp

        alpha.height = 1 + max(self.get_height(alpha.left), self.get_height(alpha.right))
        beta.height = 1 + max(self.get_height(beta.left), self.get_height(beta.right))

        return beta

    # Right rotation.
    def right_rotate(self, alpha):
        beta = alpha.left
        temp = beta.right
        beta.right = alpha
        alpha.left = temp

        alpha.height = 1 + max(self.get_height(alpha.left), self.get_height(alpha.right))
        beta.height = 1 + max(self.get_height(beta.left), self.get_height(beta.right))

        return beta

    # Get the height of the node
    def get_height(self, root):
        if not root:
            return 0

        return root.height

    def get_balance_factor(self, root):
        if not root:
            return 0

        return self.get_height(root.left) - self.get_height(root.right)

    def get_min_value_node(self, root):
        if root is None or root.left is None:
            return root

        return self.get_min_value_node(root.left)

    def print_preorder(self, root):
        if not root:
            return

        print(f'-{root.key}-', end='')
        self.print_preorder(root.left)
        self.print_preorder(root.right)


if __name__ == '__main__':
    main()
