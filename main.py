import math


class RBush:

    def __init__(self, max_entries=9):
        # max entries in a node is 9 by default; min node fill is 40% for best performance
        self._max_entries = max(4, max_entries)
        self._min_entries = max(2, math.ceil(self._max_entries * 0.4))

    def clear(self):
        self.data = create_node([])
        return self


def create_node(children):
    return {
        "children": children,
        "height": 1,
        "leaf": True,
        "minX": math.inf,
        "minY": math.inf,
        "maxX": -math.inf,
        "maxY": -math.inf
    }
