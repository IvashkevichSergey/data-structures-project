"""Здесь надо написать тесты с использованием unittest для модуля linked_list."""
import unittest
from src.linked_list import LinkedList, Node


class TestNode(unittest.TestCase):

    def test_node(self):
        self.assertEqual(Node('str', 'abc').data, 'str')
        self.assertEqual(Node('str', 'abc').next_node, 'abc')


class TestLinkedList(unittest.TestCase):
    def test_linkedlist(self):
        ll = LinkedList()
        ll.insert_beginning({'id': 1})
        self.assertIsInstance(ll.head, Node)
        self.assertIsInstance(ll.head.data, dict)

        ll.insert_at_end({'id': 2})
        self.assertEqual(ll.head.data, {'id': 1})
        self.assertEqual(ll.tail.data, {'id': 2})

        ll.insert_at_end({'id': 3})
        self.assertEqual(ll.head.data, {'id': 1})
        self.assertEqual(ll.tail.data, {'id': 3})

        ll.insert_beginning({'id': 0})
        self.assertEqual(ll.head.data, {'id': 0})
        self.assertEqual(ll.tail.data, {'id': 3})
        self.assertEqual(ll.tail.next_node, None)
        self.assertIsInstance(ll.head.next_node, Node)
        self.assertEqual(str(ll), "{'id': 0} -> {'id': 1} -> {'id': 2} -> {'id': 3} -> None")
