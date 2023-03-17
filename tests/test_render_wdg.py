import unittest

from utils import File

from wdg import RenderWDG, WDGraph

TEST_WDGRAPH = WDGraph.load_from_file('tests/example.json')


class TestRenderWDG(unittest.TestCase):
    def test_write(self):
        render_wdg = RenderWDG(TEST_WDGRAPH)
        render_wdg.write('tests/example.actual.svg')
        self.assertEqual(
            File('tests/example.expected.svg').read(),
            File('tests/example.actual.svg').read(),
        )

    def test_write_colombo_busses(self):
        wdgraph = WDGraph.load_from_file('tests/colombo-busses.json')
        render_wdg = RenderWDG(wdgraph)
        render_wdg.write('tests/colombo-busses.svg')
