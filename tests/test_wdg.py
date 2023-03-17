import unittest

from wdg import WDGraph

class TestWDG(unittest.TestCase):
    def test_load_from_file(self):
        wdg = WDGraph.load_from_file('tests/example.json')
        
        self.assertEqual(len(wdg.nodes), 3)
        self.assertEqual(wdg.nodes[0].id, '1')
        self.assertEqual(wdg.nodes[0].label, 'Node 1')
        self.assertEqual(wdg.nodes[0].xy, [0, 0])

        self.assertEqual(len(wdg.edges), 3)
        self.assertEqual(wdg.edges[0].id, '1-2')
        self.assertEqual(wdg.edges[0].source, '1')
        self.assertEqual(wdg.edges[0].target, '2')
        self.assertEqual(wdg.edges[0].weight, 10)


