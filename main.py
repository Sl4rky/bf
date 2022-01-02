#! /usr/bin/env python3

"""
    brainf**ck interpreter by Robert Eckwright 12-31-2021

"""


class Node:
    """
        Node in a linked list.
        contains a value(default 0), prev_node, and next_node
    """

    def __init__(self, value=0):
        self.value = value
        self.next_node = None
        self.prev_node = None

    def get_next_node(self):
        return self.next_node

    def get_prev_node(self):
        return self.prev_node

    def get_value(self):
        return self.value

    def set_next_node(self, new_node):
        self.next_node = new_node

    def set_prev_node(self, new_node):
        self.prev_node = new_node

    def set_value(self, new_value):
        self.value = new_value


class LinkedList:
    """
        array to store data

    """

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def add_tail(self):
        new_node = Node()
        if not self.head:
            self.head = new_node
            self.tail = new_node
        self.tail.set_next_node(new_node)
        new_node.set_prev_node(self.tail)
        self.tail = new_node
        self.length += 1

    def list_items(self):
        array = []
        current_node = self.head
        if self.length == 1:
            array.append(self.head.get_value())
            return array
        while current_node:
            array.append(current_node.get_value())
            current_node = current_node.get_next_node()
        return array


class Pointer:
    """
        Program pointer

    """

    def __init__(self):
        self.lst = LinkedList


def main():
    array = LinkedList()
    array.add_tail()
    print(array.length)
    print(array.list_items())


if __name__ == "__main__":
    main()
