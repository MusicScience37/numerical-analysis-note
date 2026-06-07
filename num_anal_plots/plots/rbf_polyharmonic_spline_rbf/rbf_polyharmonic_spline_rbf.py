"""Polyharmonic spline RBF のグラフを作成する。"""

import numpy
import plotly.express
import plotly.graph_objects


def rbf_polyharmonic_spline_rbf() -> plotly.graph_objects.Figure:
    """Polyharmonic spline RBF をプロットする。

    Returns:
        plotly.graph_objects.Figure: プロット結果。
    """
    x_list: list[float] = []
    y_list: list[float] = []
    degree_list: list[int] = []

    x = numpy.linspace(0.0, 2.0, num=201)
    x[0] = 1e-5
    y_max_in_data = 5.0
    for degree in [1, 2, 3, 4, 5, 6]:
        if degree % 2 == 0:
            y = x**degree * numpy.log(x)
        else:
            y = x**degree
        in_range = y <= y_max_in_data
        x_list = x_list + list(x[in_range])
        y_list = y_list + list(y[in_range])
        degree_list = degree_list + [degree] * len(x[in_range])

    figure = plotly.express.line(
        x=x_list,
        y=y_list,
        color=degree_list,
        line_dash=degree_list,
        labels={
            "x": "r",
            "y": "Value of RBF",
            "color": "Degree",
            "line_dash": "Degree",
        },
        range_y=[-0.5, 3.5],
        title="Polyharmonic spline RBF",
    )
    figure.update_layout(height=700)
    return figure
