"""Здесь надо написать тесты с использованием unittest для модуля stack."""
import unittest
from src.stack import Node, Stack


class TestNode(unittest.TestCase):

    def test_node(self):
        self.assertEqual(Node('str', 'abc').data, 'str')
        self.assertEqual(Node('str', 'abc').next_node, 'abc')


class TestStack(unittest.TestCase):

    def test_stack(self):
        stack = Stack()
        stack.push('first')
        self.assertEqual(stack.push('second'), None)
        self.assertIsInstance(stack.top, Node)
        self.assertEqual(stack.top.data, 'second')
        self.assertIsInstance(stack.top.next_node, Node)
        self.assertEqual(str(stack), 'second\nfirst')

        self.assertEqual(stack.pop(), 'second')
        self.assertEqual(str(stack), 'first')
        self.assertEqual(stack.pop(), 'first')
        self.assertEqual(str(stack), '')

        with self.assertRaises(Exception):
            stack.pop()
