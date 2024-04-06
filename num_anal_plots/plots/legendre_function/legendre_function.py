"""Legendre 関数をプロットする。"""

import numpy
import plotly.express
import plotly.graph_objects
import scipy.special


def legendre_function() -> plotly.graph_objects.Figure:
    """Legendre 関数をプロットする。

    Returns:
        plotly.graph_objects.Figure: プロット結果。
    """
    x_list = []
    y_list = []
    n_list = []
    n_max = 5
    for x in numpy.linspace(-1.0, 1.0, num=101):
        y, _ = scipy.special.lpn(n_max, x)
        x_list = x_list + [x] * (n_max + 1)
        y_list = y_list + list(y)
        n_list = n_list + list(range(n_max + 1))

    return plotly.express.line(
        x=x_list,
        y=y_list,
        color=n_list,
        line_dash=n_list,
        labels={
            "x": "$x$",
            "y": "$P_n(x)$",
            "color": "Degree",
            "line_dash": "Degree",
        },
        title="Legendre Function",
        template="plotly_white",
    )
