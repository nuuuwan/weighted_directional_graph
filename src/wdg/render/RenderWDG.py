from functools import cache, cached_property

from utils import Log
from utils.xmlx import _

from wdg.core.WDGraph import WDGraph
from wdg.render.Style import Style

log = Log('RenderWDG')


class RenderWDG:
    def __init__(self, wdg: WDGraph):
        self.wdg = wdg

    @cached_property
    def xys(self):
        return [node.xy for node in self.wdg.nodes]

    @cache
    def get_transform(self):
        xys = self.xys
        xs = [xy[0] for xy in xys]
        ys = [xy[1] for xy in xys]
        x_min, x_max = min(xs), max(xs)
        y_min, y_max = min(ys), max(ys)
        x_range = x_max - x_min
        y_range = y_max - y_min

        def transform(xy):
            x, y = xy
            x2 = (x - x_min) / x_range * Style.WIDTH + Style.PADDING
            y2 = (y_max - y) / y_range * Style.HEIGHT + Style.PADDING
            return x2, y2

        return transform

    @cached_property
    def node_idx(self):
        return {node.id: node for node in self.wdg.nodes}

    @cache
    def get_node_radius(self, id):
        weight_sum = 0
        for edge in self.wdg.edges:
            if edge.source == id or edge.target == id:
                weight_sum += edge.weight

        radius = weight_sum
        return radius

    def render_node(self, node):
        transform = self.get_transform()
        x, y = transform(node.xy)
        r = self.get_node_radius(node.id)
        return _(
            'g',
            [
                _('circle', None, Style.NODE_CIRCLE | dict(cx=x, cy=y, r=r)),
                _('text', node.id, Style.NODE_TEXT | dict(x=x, y=y)),
            ],
        )

    def render_nodes(self):
        return [self.render_node(node) for node in self.wdg.nodes]

    def render_edge(self, edge):
        transform = self.get_transform()
        node_idx = self.node_idx
        node1 = node_idx[edge.source]
        node2 = node_idx[edge.target]
        x1, y1 = transform(node1.xy)
        x2, y2 = transform(node2.xy)
        x_mid = (x1 + x2) / 2
        y_mid = (y1 + y2) / 2

        return _(
            'g',
            [
                _(
                    'line',
                    None,
                    Style.EDGE_LINE
                    | dict(
                        x1=x1, y1=y1, x2=x2, y2=y2, stroke_width=edge.weight
                    ),
                ),
                _(
                    'text',
                    edge.id,
                    Style.EDGE_TEXT
                    | dict(
                        x=x_mid,
                        y=y_mid,
                    ),
                ),
            ],
        )

    def render_edges(self):
        return [self.render_edge(edge) for edge in self.wdg.edges]

    def render_svg(self):
        return _(
            'svg',
            self.render_edges() + self.render_nodes(),
            dict(
                width=Style.WIDTH + Style.PADDING * 2,
                height=Style.HEIGHT + Style.PADDING * 2,
            ),
        )

    def write(self, path: str):
        svg = self.render_svg()
        svg.store(path)
        log.info(f'Saved {path}')
