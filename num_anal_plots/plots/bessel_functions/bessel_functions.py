"""Bessel 関数をプロットする。"""

import numpy
import plotly.express
import plotly.graph_objects
import scipy.special


def cylindrical_bessel_functions() -> plotly.graph_objects.Figure:
    """Bessel 関数をプロットする。

    Returns:
        plotly.graph_objects.Figure: プロット結果。
    """
    x_list: list[float] = []
    y_list: list[float] = []
    n_list: list[int] = []
    function_type_list: list[str] = []
    n_max = 5
    y_min_in_data = -2.0

    # First kind.
    x = numpy.linspace(0.0, 10.0, num=201)
    for n in range(n_max + 1):
        y = scipy.special.jv(n, x)
        x_list = x_list + list(x)
        y_list = y_list + list(y)
        n_list = n_list + [n] * len(x)
        function_type_list = function_type_list + ["First Kind (J)"] * len(x)

    # Second kind.
    x = x[1:]  # Avoid x=0 for second kind.
    for n in range(n_max + 1):
        y = scipy.special.yv(n, x)
        in_range = y > y_min_in_data
        x_list = x_list + list(x[in_range])
        y_list = y_list + list(y[in_range])
        n_list = n_list + [n] * sum(in_range)
        function_type_list = function_type_list + ["Second Kind (N)"] * sum(in_range)

    figure = plotly.express.line(
        x=x_list,
        y=y_list,
        color=n_list,
        line_dash=n_list,
        facet_row=function_type_list,
        labels={
            "x": "$x$",
            "y": "Function Value",
            "color": "Order",
            "line_dash": "Order",
            "facet_row": "Function",
        },
        title="Bessel Functions",
        range_y=[-1.5, 1.0],
    )
    figure.update_layout(height=900)
    return figure


def modified_bessel_functions() -> plotly.graph_objects.Figure:
    """修正 Bessel 関数をプロットする。

    Returns:
        plotly.graph_objects.Figure: プロット結果。
    """
    x_list: list[float] = []
    y_list: list[float] = []
    n_list: list[int] = []
    function_type_list: list[str] = []
    n_max = 5
    y_max_in_data = 4.0

    # First kind.
    x = numpy.linspace(0.0, 5.0, num=201)
    for n in range(n_max + 1):
        y = scipy.special.iv(n, x)
        in_range = y < y_max_in_data
        x_list = x_list + list(x[in_range])
        y_list = y_list + list(y[in_range])
        n_list = n_list + [n] * sum(in_range)
        function_type_list = function_type_list + ["First Kind (I)"] * sum(in_range)

    # Second kind.
    x = x[1:]  # Avoid x=0 for second kind.
    for n in range(n_max + 1):
        y = scipy.special.kv(n, x)
        in_range = y < y_max_in_data
        x_list = x_list + list(x[in_range])
        y_list = y_list + list(y[in_range])
        n_list = n_list + [n] * sum(in_range)
        function_type_list = function_type_list + ["Second Kind (K)"] * sum(in_range)

    figure = plotly.express.line(
        x=x_list,
        y=y_list,
        color=n_list,
        line_dash=n_list,
        facet_row=function_type_list,
        labels={
            "x": "$x$",
            "y": "Function Value",
            "color": "Order",
            "line_dash": "Order",
            "facet_row": "Function",
        },
        title="Modified Bessel Functions",
        range_y=[0.0, 3.0],
    )
    figure.update_layout(height=900)
    return figure
