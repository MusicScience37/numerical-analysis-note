"""Matérn RBF のグラフを作成する。"""

import numpy
import plotly.express
import plotly.graph_objects
import scipy.special


def rbf_matern_rbf() -> plotly.graph_objects.Figure:
    """Matérn RBF をプロットする。

    Returns:
        plotly.graph_objects.Figure: プロット結果。
    """
    x_list: list[float] = []
    y_list: list[float] = []
    order_list: list[float] = []
    x = numpy.linspace(0.0, 5.0, num=501)
    x[0] = 1e-5
    for order in [0.5, 1.0, 1.5, 2.0, 2.5]:
        y = (
            (2.0 ** (1.0 - order))
            / scipy.special.gamma(order)
            * (x**order)
            * scipy.special.kv(order, x)
        )
        x_list = x_list + list(x)
        y_list = y_list + list(y)
        order_list = order_list + [order] * len(x)

    figure = plotly.express.line(
        x=x_list,
        y=y_list,
        color=order_list,
        line_dash=order_list,
        labels={
            "x": "r",
            "y": "Value of RBF",
            "color": "Order",
            "line_dash": "Order",
        },
        title="Matérn RBF",
    )
    return figure
