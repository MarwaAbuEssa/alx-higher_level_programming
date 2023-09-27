#!/usr/bin/python3
""" singly-linked list."""

class Node:
    """ a node in a singly-linked list."""

    def __init__(self, data, next_node=None):
        """ create new node 
        Args:
        data (int): Node value
        next_node (Node): pointer to next node
        """
        self.data = data
        self.next_node = next_node

        @property
        def data(self):
            """ getter of node """
            return (self.__data)

        @data.setter
        def data(self, value):
            if not isinstance(value, int):
                raise TypeError("data must be an integer")
            self.__data = value

            @property
            def next_node(self):
                """ getter for next value """
                return (self.__next_node)

            @next_node.setter
            def next_node(self, value):
                """ setter for nex value """
                if not isinstance(value, Node) and value is not None:
                    raise TypeError("next_node must be a Node object")
                self.__next_node = value


class SinglyLinkedList:
    """ a singly-linked list."""

        def __init__(self):
            """ create a new SinglyLinkedList."""
            self.__head = None

        def sorted_insert(self, value):
            """ insert new node

            Args:
            value (Node): The new Node value
            """

            new_node = Node(value)
            if self.__head is None:
                new_node.next_node = None
                self.__head = new_node
            elif self.__head.data > value:
                new_node.next_node = self.__head
                self.__head = new_node
            else:
                tmp = self.__head
                while (tmp.next_node is not None and
                        tmp.next_node.data < value):
                    tmp = tmp.next_node
                new_node.next_node = tmp.next_node
                tmp.next_node = new_node


        def __str__(self):
            """ print()  SinglyLinkedList. """
            values = []
            tmp = self.__head
            while tmp is not None:
                values.append(str(tmp.data))
                tmp = tmp.next_node
            return ('\n'.join(values))
