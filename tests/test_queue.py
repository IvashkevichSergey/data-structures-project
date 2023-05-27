"""Здесь надо написать тесты с использованием unittest для модуля queue."""
import unittest
from src.queue import Queue, Node


class TestNode(unittest.TestCase):

    def test_node(self):
        self.assertEqual(Node('str', 'abc').data, 'str')
        self.assertEqual(Node('str', 'abc').next_node, 'abc')


class TestQueue(unittest.TestCase):
    def test_queue(self):
        queue = Queue()
        queue.enqueue('first')
        self.assertEqual(queue.enqueue('second'), None)
        self.assertIsInstance(queue.head, Node)
        self.assertIsInstance(queue.tail, Node)
        self.assertEqual(queue.head.data, 'first')
        self.assertEqual(queue.tail.data, 'second')
        self.assertEqual(str(queue), 'first\nsecond')
        queue.enqueue('third')
        self.assertEqual(queue.head.next_node.data, 'second')
        self.assertEqual(queue.tail.next_node, None)

