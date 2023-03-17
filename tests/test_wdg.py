import unittest

from wdg import WDGraph


class TestWDG(unittest.TestCase):
    def test_load_from_file(self):
        wdgraph = WDGraph.load_from_file('tests/example.json')

        self.assertEqual(len(wdgraph.nodes), 3)
        self.assertEqual(wdgraph.nodes[0].id, '1')
        self.assertEqual(wdgraph.nodes[0].label, 'Node 1')
        self.assertEqual(wdgraph.nodes[0].xy, [0, 0])

        self.assertEqual(len(wdgraph.edges), 3)
        self.assertEqual(wdgraph.edges[0].id, '1-2')
        self.assertEqual(wdgraph.edges[0].source, '1')
        self.assertEqual(wdgraph.edges[0].target, '2')
        self.assertEqual(wdgraph.edges[0].weight, 10)
