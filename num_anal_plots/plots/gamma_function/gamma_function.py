"""Gamma 関数をプロットする。"""

import numpy
import plotly.express
import plotly.graph_objects
import scipy.special


def gamma_function() -> plotly.graph_objects.Figure:
    """Gamma 関数をプロットする。

    Returns:
        plotly.graph_objects.Figure: プロット結果。
    """
    x_list: list[float] = []
    y_list: list[float] = []
    for x in numpy.linspace(-2.0, 5.0, num=141):
        y = scipy.special.gamma(x)
        x_list.append(x)
        y_list.append(y)

    return plotly.express.line(
        x=x_list,
        y=y_list,
        labels={
            "x": "$x$",
            "y": "$\\Gamma(x)$",
        },
        title="Gamma Function",
        range_y=[-10.0, 10.0],
    )
