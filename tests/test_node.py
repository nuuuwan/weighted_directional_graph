import unittest

from wdg import Node


class TestNode(unittest.TestCase):
    def test_init(self):
        node = Node(id='1', xy=[0, 0])
        self.assertEqual(node.id, '1')
        self.assertEqual(node.xy, [0, 0])
