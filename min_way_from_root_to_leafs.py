class Node():
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class Tree():

    def __init__(self, root=None):
        self.root = root

    def add(self, insertion, start="start"):
        if start == "start":
            start = self.root
        if start is None:
            self.root = Node(insertion)
            return
        if insertion > start.data:
            if start.right is None:
                start.right = Node(insertion)
                return
            else:
                self.add(insertion, start.right)
        elif insertion < start.data:
            if start.left is None:
                start.left = Node(insertion)
                return
            else:
                self.add(insertion, start.left)


    def print(self, start="start"):
        if start == "start":
            start = self.root
        if start is None:
            return
        self.print(start.left)
        print(start.data)
        self.print(start.right)

    def min_dist(self, start="start"):
        if start == "start":
            start = self.root
        if start is None or (start.left is None and start.right is None):
            return 0
        return min(self.min_dist(start.left), self.min_dist(start.right)) + 1

    def max_dist(self, start="start"):
        if start == "start":
            start = self.root
        if start is None or (start.left is None and start.right is None):
            return 0

        return max(self.max_dist(start.left), self.max_dist(start.right)) + 1
tree = Tree()
for num in input().split():
    tree.add(int(num))
print(tree.min_dist() + tree.max_dist())


