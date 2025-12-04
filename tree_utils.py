from __future__ import annotations

from dataclasses import dataclass
from typing import Optional


@dataclass
class Node:
    key: int
    left: Optional["Node"] = None
    right: Optional["Node"] = None


class BinarySearchTree:
    def __init__(self) -> None:
        self.root: Optional[Node] = None

    def insert(self, key: int) -> None:
        if self.root is None:
            self.root = Node(key)
            return

        current = self.root
        while True:
            if key < current.key:
                if current.left is None:
                    current.left = Node(key)
                    return
                current = current.left
            else:
                if current.right is None:
                    current.right = Node(key)
                    return
                current = current.right


def find_minimum(node: Optional[Node]) -> int:
    if node is None:
        raise ValueError("Cannot find minimum in an empty tree")

    current = node
    while current.left is not None:
        current = current.left
    return current.key


def find_maximum(node: Optional[Node]) -> int:
    if node is None:
        raise ValueError("Cannot find maximum in an empty tree")

    current = node
    while current.right is not None:
        current = current.right
    return current.key


def sum_values(node: Optional[Node]) -> int:
    if node is None:
        return 0
    return node.key + sum_values(node.left) + sum_values(node.right)


def build_sample_tree() -> BinarySearchTree:
    # Simple helper to create tree used in tasks
    bst = BinarySearchTree()
    for value in (50, 30, 70, 20, 40, 60, 80):
        bst.insert(value)
    return bst


__all__ = [
    "Node",
    "BinarySearchTree",
    "find_minimum",
    "find_maximum",
    "sum_values",
    "build_sample_tree",
]
