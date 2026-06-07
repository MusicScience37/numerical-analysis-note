"""RBF のプロットを作成する。"""

import numpy
import plotly.express
import plotly.graph_objects


def rbf_general_rbfs() -> plotly.graph_objects.Figure:
    """RBF をプロットする。

    Returns:
        plotly.graph_objects.Figure: プロット結果。
    """
    x_list: list[float] = []
    y_list: list[float] = []
    function_list: list[str] = []

    x = numpy.linspace(0.0, 3.0, num=301)

    # Gaussian.
    y = numpy.exp(-numpy.power(x, 2))
    x_list = x_list + list(x)
    y_list = y_list + list(y)
    function_list = function_list + ["Gaussian"] * len(x)

    # Multi-quadric.
    y = numpy.sqrt(1.0 + numpy.power(x, 2))
    x_list = x_list + list(x)
    y_list = y_list + list(y)
    function_list = function_list + ["Multi-quadric"] * len(x)

    # Inverse multi-quadric.
    y = 1.0 / numpy.sqrt(1.0 + numpy.power(x, 2))
    x_list = x_list + list(x)
    y_list = y_list + list(y)
    function_list = function_list + ["Inverse multi-quadric"] * len(x)

    # Inverse quadratic.
    y = 1.0 / (1.0 + numpy.power(x, 2))
    x_list = x_list + list(x)
    y_list = y_list + list(y)
    function_list = function_list + ["Inverse quadratic"] * len(x)

    # Sech.
    y = 1.0 / numpy.cosh(x)
    x_list = x_list + list(x)
    y_list = y_list + list(y)
    function_list = function_list + ["Sech"] * len(x)

    figure = plotly.express.line(
        x=x_list,
        y=y_list,
        color=function_list,
        line_dash=function_list,
        labels={
            "x": "r",
            "y": "Value of RBF",
            "color": "RBF",
            "line_dash": "RBF",
        },
        title="RBFs",
        range_y=[0.0, 2.0],
    )
    return figure
