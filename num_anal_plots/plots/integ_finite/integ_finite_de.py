"""ベンチマーク結果などをプロットする。"""

import gzip
import os

import msgpack
import pandas
import plotly.express as px
import plotly.graph_objects

THIS_DIR = os.path.dirname(os.path.abspath(__file__))


def integ_de_errors() -> plotly.graph_objects.Figure:
    """DE 公式による誤差をプロットする。

    Returns:
        plotly.graph_objects.Figure: プロット結果。
    """
    with gzip.open(os.path.join(THIS_DIR, "exp.data"), mode="rb") as file:
        results = msgpack.unpack(file)

    data_list = []
    for measurement in results["measurements"]:
        if measurement["measurer_name"] != "Mean Processing Time":
            continue

        if measurement["case_name"] != "de_finite":
            continue

        points = int(measurement["params"]["points"])

        error = 0.0
        for outputs in measurement["custom_outputs"]:
            if outputs["name"] == "error":
                error = float(outputs["value"])
                break
        if error <= 0.0:
            continue

        data_list.append(
            {
                "Points": points,
                "Target": r"$\int_{0}^{1}\exp(x)dx$",
                "Error": error,
            }
        )

    with gzip.open(os.path.join(THIS_DIR, "sqrt_1mx2.data"), mode="rb") as file:
        results = msgpack.unpack(file)

    for measurement in results["measurements"]:
        if measurement["measurer_name"] != "Mean Processing Time":
            continue

        if measurement["case_name"] != "de_finite":
            continue

        points = int(measurement["params"]["points"])

        error = 0.0
        for outputs in measurement["custom_outputs"]:
            if outputs["name"] == "error":
                error = float(outputs["value"])
                break
        if error <= 0.0:
            continue

        data_list.append(
            {
                "Points": points,
                "Target": r"$\int_{-1}^{1}\sqrt{1-x^2}dx$",
                "Error": error,
            }
        )

    with gzip.open(os.path.join(THIS_DIR, "inv_sqrt_1mx2.data"), mode="rb") as file:
        results = msgpack.unpack(file)

    for measurement in results["measurements"]:
        if measurement["measurer_name"] != "Mean Processing Time":
            continue

        if measurement["case_name"] != "de_finite":
            continue

        points = int(measurement["params"]["points"])

        error = 0.0
        for outputs in measurement["custom_outputs"]:
            if outputs["name"] == "error":
                error = float(outputs["value"])
                break
        if error <= 0.0:
            continue

        data_list.append(
            {
                "Points": points,
                "Target": r"$\int_{-1}^{1}1/\sqrt{1-x^2}dx$",
                "Error": error,
            }
        )

    data_frame = pandas.DataFrame(data_list)

    figure = px.line(
        data_frame,
        x="Points",
        y="Error",
        color="Target",
        line_dash="Target",
        markers=True,
        log_y=True,
        title="Error of Numerical Integration Using Double Exponential Formula",
        template="plotly_white",
    )
    figure.update_layout(
        # cspell: disable
        yaxis=dict(
            showexponent="all",
            exponentformat="power",
        )
        # cspell: enable
    )
    return figure
