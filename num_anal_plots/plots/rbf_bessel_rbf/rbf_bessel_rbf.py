"""Bessel RBF のグラフを作成する。"""

import numpy
import plotly.express
import plotly.graph_objects
import scipy.special


def rbf_bessel_rbf() -> plotly.graph_objects.Figure:
    """Bessel RBF をプロットする。

    Returns:
        plotly.graph_objects.Figure: プロット結果。
    """
    x_list: list[float] = []
    y_list: list[float] = []
    d_list: list[int] = []
    x = numpy.linspace(0.0, 10.0, num=101)
    x[0] = 1e-5
    for d in [1, 2, 3, 4]:
        order = float(d) / 2.0 - 1.0
        y = scipy.special.jv(order, x) / (x**order)
        x_list = x_list + list(x)
        y_list = y_list + list(y)
        d_list = d_list + [d] * len(x)

    figure = plotly.express.line(
        x=x_list,
        y=y_list,
        color=d_list,
        line_dash=d_list,
        labels={
            "x": "r",
            "y": "Value of RBF",
            "color": "d",
            "line_dash": "d",
        },
        title="Bessel RBF",
    )
    return figure
