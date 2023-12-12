"""ベンチマーク結果をプロットする。"""

import msgpack
import os

import pandas
import plotly.express as px
import plotly.graph_objects

THIS_DIR = os.path.dirname(os.path.abspath(__file__))


SOLVERS = ["CG", "BiCGstab"]


def laplacian_2d_grid() -> plotly.graph_objects.Figure:
    """ベンチマーク結果をプロットする。

    Returns:
        plotly.graph_objects.Figure: プロット結果。
    """
    with open(os.path.join(THIS_DIR, "bench.data"), mode="rb") as file:
        results = msgpack.unpack(file)

    data_list = []
    for measurement in results["measurements"]:
        if measurement["measurer_name"] != "Mean Processing Time":
            continue

        solver_name = measurement["case_name"]
        if solver_name not in SOLVERS:
            continue

        data_list.append(
            {
                "Solver": solver_name,
                "Size of Coefficient Matrix": int(measurement["params"]["size"]),
                "Time [sec]": float(measurement["durations"]["stat"]["mean"]),
            }
        )

    data_frame = pandas.DataFrame(data_list)
    return px.line(
        data_frame,
        x="Size of Coefficient Matrix",
        y="Time [sec]",
        category_orders={"Solver": SOLVERS},
        color="Solver",
        line_dash="Solver",
        log_x=True,
        log_y=True,
        title="Time to Solve Linear Equations of Laplacian Matrices",
    )
