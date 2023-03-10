from typing import List, Optional


class Node:
    def __init__(self, key: str, data: List[str]) -> None:
        self.key = key
        self.data = data
        self.next = None
        self.prev = None

    def get_data(self) -> List[str]:
        return self.data

    def get_key(self) -> str:
        return self.key


class Queue:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.size = 0

    def enqueue_at_first(self, key: str, data: List[str]) -> Node:
        new_node = Node(key, data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.size += 1
        return new_node

    def dequeue_from_last(self) -> str:
        if self.tail:
            key = self.tail.key
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.tail = self.tail.prev
                self.tail.next = None
            self.size -= 1
            return key
        else:
            return ''

    def move_to_head(self, node: Node) -> None:
        if self.head == node:
            return
        if self.tail == node:
            self.tail = self.tail.prev
            self.tail.next = None

            node.next = self.head
            node.prev = None

            self.head.prev = node
            self.head = self.head.prev
        else:
            node.prev.next = node.next
            node.next.prev = node.prev

            node.next = self.head
            node.prev = None

            self.head.prev = node
            self.head = self.head.prev

    def get_size(self) -> int:
        return self.size
