class Style:
    WIDTH, HEIGHT = 800, 450
    PADDING = 100

    NODE_CIRCLE = dict(
        r=32,
        stroke='gray',
        fill='lightgray',
    )

    NODE_LABEL = dict(
        text_anchor='middle',
        alignment_baseline='middle',
        font_size=10,
        stroke='none',
        fill='black',
        font_family='sans-serif',
    )

    EDGE_LINE = dict(
        stroke='gray',
        fill='none',
    )
