"""ベンチマーク結果などをプロットする。"""

import gzip
import os

import msgpack
import pandas
import plotly.express as px
import plotly.graph_objects

THIS_DIR = os.path.dirname(os.path.abspath(__file__))


def integ_gauss_legendre_kronrod_time() -> plotly.graph_objects.Figure:
    """Gauss-Legendre-Kronrod 公式による計算時間をプロットする。

    Returns:
        plotly.graph_objects.Figure: プロット結果。
    """
    with gzip.open(os.path.join(THIS_DIR, "exp.data"), mode="rb") as file:
        results = msgpack.unpack(file)

    data_list = []
    for measurement in results["measurements"]:
        if measurement["measurer_name"] != "Mean Processing Time":
            continue

        if measurement["case_name"] != "gauss_legendre_kronrod":
            continue

        degree = int(measurement["params"]["degree"])

        data_list.append(
            {
                "Degree": degree,
                "Target": r"$\int_{0}^{1}\exp(x)dx$",
                "Time [sec]": float(measurement["durations"]["stat"]["mean"]),
                "Std. Err. of Time [sec]": float(
                    measurement["durations"]["stat"]["standard_error"]
                ),
            }
        )

    with gzip.open(os.path.join(THIS_DIR, "sqrt_1mx2.data"), mode="rb") as file:
        results = msgpack.unpack(file)

    for measurement in results["measurements"]:
        if measurement["measurer_name"] != "Mean Processing Time":
            continue

        if measurement["case_name"] != "gauss_legendre_kronrod":
            continue

        degree = int(measurement["params"]["degree"])

        data_list.append(
            {
                "Degree": degree,
                "Target": r"$\int_{-1}^{1}\sqrt{1-x^2}dx$",
                "Time [sec]": float(measurement["durations"]["stat"]["mean"]),
                "Std. Err. of Time [sec]": float(
                    measurement["durations"]["stat"]["standard_error"]
                ),
            }
        )

    with gzip.open(os.path.join(THIS_DIR, "inv_sqrt_1mx2.data"), mode="rb") as file:
        results = msgpack.unpack(file)

    for measurement in results["measurements"]:
        if measurement["measurer_name"] != "Mean Processing Time":
            continue

        if measurement["case_name"] != "gauss_legendre_kronrod":
            continue

        degree = int(measurement["params"]["degree"])

        data_list.append(
            {
                "Degree": degree,
                "Target": r"$\int_{-1}^{1}1/\sqrt{1-x^2}dx$",
                "Time [sec]": float(measurement["durations"]["stat"]["mean"]),
                "Std. Err. of Time [sec]": float(
                    measurement["durations"]["stat"]["standard_error"]
                ),
            }
        )

    data_frame = pandas.DataFrame(data_list)

    return px.line(
        data_frame,
        x="Degree",
        y="Time [sec]",
        color="Target",
        line_dash="Target",
        error_y="Std. Err. of Time [sec]",
        markers=True,
        log_y=True,
        title="Processing Time of Numerical Integration Using Gauss-Legendre-Kronrod Formula",
    )
