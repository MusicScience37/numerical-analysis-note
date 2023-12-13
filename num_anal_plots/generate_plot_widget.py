"""Jupyter で表示する用のプロットのウィジェットを生成する。"""

import plotly.graph_objects

from num_anal_plots.plots.plots import PLOT_INFO_DICT


def generate_plot_widget(
    name: str, *, height: int = 500
) -> plotly.graph_objects.FigureWidget:
    """Jupyter で表示する用のプロットのウィジェットを生成する。

    Args:
        name (str): プロットの名前。
        height (int): プロットの領域の高さ。単位はピクセル。

    Returns:
        plotly.graph_objects.FigureWidget: プロットのウィジェット。
    """
    info = PLOT_INFO_DICT[name]
    figure = info.figure_factory()
    figure.update_layout(height=height)
    return plotly.graph_objects.FigureWidget(figure)
