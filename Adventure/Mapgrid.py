class MapGrid:
    def __init__(self, width, height):
        self.width = width
        self.height = height


def draw_grid(graph, width=2):
    for y in range(graph.height):
