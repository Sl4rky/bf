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
        self.lst = LinkedList()
        for _ in range(2):
            self.lst.add_tail()
        self.ptr = self.lst.head

    def move_left(self):
        if not self.ptr.get_prev_node():
            print("Error: Out of index")
        self.ptr = self.ptr.get_prev_node()

    def move_right(self):
        if not self.ptr.get_next_node():
            self.lst.add_tail()
        self.ptr = self.ptr.get_next_node()

    def add_to_node(self):
        self.ptr.set_value(self.ptr.get_value() + 1)

    def sub_from_node(self):
        self.ptr.set_value(self.ptr.get_value() - 1)

    def get_node_value(self):
        return self.ptr.get_value()

    def print_node(self):
        print(chr(self.ptr.get_value()), end="")

    def input_node(self):
        self.ptr.set_value(int(input("Enter a number: ")))


def main():
    prog = """
                >++++++++[<+++++++++>-]<.>++++[<+++++++>-]<+.+++++++..+++.>>++++++[<+++++++>-]<+
                +.------------.>++++++[<+++++++++>-]<+.<.+++.------.--------.>>>++++[<++++++++>-
                ]<+.
           """
    program = Pointer()
    jump_lst = []
    i = 0

    while i <= len(prog) - 1:
        char = prog[i]
        if char == "+":
            program.add_to_node()
        elif char == "-":
            program.sub_from_node()
        elif char == "<":
            program.move_left()
        elif char == ">":
            program.move_right()
        elif char == ".":
            program.print_node()
        elif char == ",":
            program.input_node()
        elif char == "[":
            jump_lst.append(i)
        elif char == "]":
            try:
                new_index = jump_lst[-1]
            except IndexError:
                print("Mismatched brackets")
                break
            if program.get_node_value() != 0:
                i = new_index
            else:
                jump_lst.pop()
        i += 1
    print()
    print(program.lst.list_items())
    print(jump_lst)


if __name__ == "__main__":
    main()
