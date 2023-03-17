import unittest

from wdg import Edge


class TestNode(unittest.TestCase):
    def test_init(self):
        edge = Edge(
            id='1-2', label='Edge 1-2', source='1', target='2', weight=10
        )
        self.assertEqual(edge.id, '1-2')
        self.assertEqual(edge.label, 'Edge 1-2')
        self.assertEqual(edge.source, '1')
        self.assertEqual(edge.target, '2')
        self.assertEqual(edge.weight, 10)
