import unittest

from wdg import RenderWDG, WDGraph

TEST_WDGRAPH = WDGraph.load_from_file('tests/example.json')


class TestRenderWDG(unittest.TestCase):
    def test_write(self):
        render_wdg = RenderWDG(TEST_WDGRAPH)
        render_wdg.write('tests/example.png')
