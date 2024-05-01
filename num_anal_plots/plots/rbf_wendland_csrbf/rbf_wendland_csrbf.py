"""Wendland の CSRBF のグラフを作成する。"""

import math

import numpy
import plotly.express
import plotly.graph_objects


def rbf_wendland_csrbf() -> plotly.graph_objects.Figure:
    """Legendre 関数をプロットする。

    Returns:
        plotly.graph_objects.Figure: プロット結果。
    """
    x_list = []
    y_list = []
    l_list = []
    k_list = []
    for x in numpy.linspace(0.0, 1.2, num=121):
        for l in [1, 2, 3]:
            k = 0
            if x < 1:
                y = math.pow(1.0 - x, l)
            else:
                y = 0
            x_list.append(x)
            y_list.append(y)
            l_list.append(l)
            k_list.append(k)

            k = 1
            if x < 1:
                y = math.pow(1 - x, l + 1) * ((l + 1) * x + 1.0)
            else:
                y = 0
            x_list.append(x)
            y_list.append(y)
            l_list.append(l)
            k_list.append(k)

            k = 2
            if x < 1:
                y = (
                    math.pow(1 - x, l + 2)
                    * ((l + 1) * (l + 3) * x * x + 3 * (l + 2) * x + 3)
                    / 3.0
                )
            else:
                y = 0
            x_list.append(x)
            y_list.append(y)
            l_list.append(l)
            k_list.append(k)

    figure = plotly.express.line(
        x=x_list,
        y=y_list,
        color=k_list,
        line_dash=k_list,
        facet_row=l_list,
        labels={
            "x": "r",
            "y": "Rate of Values of CSRBF",
            "color": "k",
            "line_dash": "k",
            "facet_row": "l",
        },
        title="Wendland's Compactly Supported RBF",
        template="plotly_white",
    )
    figure.update_layout(height=900)
    return figure
