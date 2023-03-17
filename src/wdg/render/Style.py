class Style:
    WIDTH, HEIGHT = 800, 450
    PADDING = 100

    TEXT = dict(
        text_anchor='middle',
        alignment_baseline='middle',
        font_size=10,
        stroke='none',
        fill='black',
        font_family='sans-serif',
    )

    NODE_CIRCLE = dict(
        r=32,
        stroke='gray',
        fill='lightgray',
    )

    NODE_TEXT = TEXT

    EDGE_LINE = dict(
        stroke='gray',
        fill='none',
    )

    EDGE_TEXT = TEXT
