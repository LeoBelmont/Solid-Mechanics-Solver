import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Wedge
from StructuresExplained.solutions import functions

from typing import (
    Union,
    List,
    Dict,
    Any
)


class fig_generator:
    def __init__(self, subareas_rectangle, subareas_circle, total_cg_x, total_cg_y):
        self.subareas_rectangle: Dict[int, list] = subareas_rectangle
        self.subareas_circle: Dict[int, List[Union[float, Any]]] = subareas_circle
        self.total_cg_x: float = total_cg_x
        self.total_cg_y: float = total_cg_y

    bbox_setting = dict(boxstyle="round,pad=0.1", fc="grey", ec="black", lw=1)

    def det_color(self, key, subarea_id):
        if key == subarea_id:
            color = 'r'
        else:
            color = 'dodgerblue'
        return color

    def plot_rect(self, rectangle_subarea_id):
        for key, (x1, y1, x2, y2) in self.subareas_rectangle.items():
            base = x2 - x1
            height = y1 - y2
            self.subplot.text(x1, y1, f'({x1},{y1})', size=functions.size, ha='center', va='bottom',
                              bbox=self.bbox_setting)
            self.subplot.plot(x1, y1, 'ro')

            self.subplot.text(x2, y2, f'({x2},{y2})', size=functions.size, ha='center', va='bottom',
                              bbox=self.bbox_setting)
            self.subplot.plot(x2, y2, 'ro')

            color = self.det_color(key, rectangle_subarea_id)

            self.subplot.add_patch(
                Rectangle((x1, y2), base, height, linewidth=5, edgecolor=(10 / 255, 60 / 255, 100 / 255),
                          facecolor=color,
                          alpha=1))

    def plot_cir(self, circle_subarea_id):
        for key, (x, y, radius, angle) in self.subareas_circle.items():
            self.subplot.plot(x, y, 'ro')
            self.subplot.text(x, y, f'({x},{y})', size=functions.size, ha='center', va='bottom', bbox=self.bbox_setting)
            color = self.det_color(key, circle_subarea_id)
            self.subplot.add_patch(
                Wedge((x, y), radius, -angle, -angle - 180, linewidth=5, edgecolor='black', facecolor=color))

    def plot(self, rectangle_subarea_id=None, circle_subarea_id=None, fig=None):
        if fig is None:
            fig = plt.figure()
        else:
            fig.clear()

        self.subplot = fig.add_subplot(111)

        self.plot_rect(rectangle_subarea_id)
        self.plot_cir(circle_subarea_id)

        self.subplot.plot(self.total_cg_x, self.total_cg_y, 'ro')
        self.subplot.text(self.total_cg_x, self.total_cg_y, f"CG ({self.total_cg_x},{self.total_cg_y})",
                          size=functions.size, ha='center',
                          va='bottom', bbox=self.bbox_setting)

        plt.tight_layout()
        self.subplot.set_aspect('equal', 'datalim')
        self.subplot.set_alpha(0.2)
        return fig