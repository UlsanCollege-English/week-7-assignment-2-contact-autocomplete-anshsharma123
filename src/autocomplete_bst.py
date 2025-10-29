class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        """Insert key into BST. Return False if duplicate."""
        if self.root is None:
            self.root = Node(key)
            return True

        cur = self.root
        while True:
            if key == cur.key:
                return False  # reject duplicates
            elif key < cur.key:
                if cur.left:
                    cur = cur.left
                else:
                    cur.left = Node(key)
                    return True
            else:
                if cur.right:
                    cur = cur.right
                else:
                    cur.right = Node(key)
                    return True

    def find(self, key):
        """Return True if key exists in BST."""
        cur = self.root
        while cur:
            if key == cur.key:
                return True
            elif key < cur.key:
                cur = cur.left
            else:
                cur = cur.right
        return False

    def autocomplete(self, prefix, k):
        """
        Return up to k keys that start with prefix.
        If there are no prefix matches, include following lexicographically larger keys.
        """
        if not self.root or k <= 0:
            return []

        # Step 1: collect all keys in sorted order
        all_keys = []

        def inorder(node):
            if not node:
                return
            inorder(node.left)
            all_keys.append(node.key)
            inorder(node.right)

        inorder(self.root)

        # Step 2: find matches that start with prefix
        matches = [w for w in all_keys if w.startswith(prefix)]

        # If we found any prefix matches, return only those (up to k)
        if matches:
            return matches[:k]

        # Otherwise, find the next lexicographic keys after prefix
        next_keys = [w for w in all_keys if w > prefix]
        return next_keys[:k]