class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None

    def search(self, target):
        curr = self.head
        while curr:
            if curr.data == target:
                return curr
            curr = curr.next
        return None

    def insert(self, node):
        node.next = self.head
        if self.head:
            self.head.prev = node

        self.head = node
        node.prev = None

    def remove(self, node):
        if node.prev is not None:
            node.prev.next = node.next
        else:
            self.haed = node.next

        if node.next is not None:
            node.next.prev = node.prev