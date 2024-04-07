"""ベンチマーク結果をプロットする。"""

import gzip
import os

import msgpack
import pandas
import plotly.express as px
import plotly.graph_objects

THIS_DIR = os.path.dirname(os.path.abspath(__file__))


def ode_runge_kutta_sparse_solvers() -> plotly.graph_objects.Figure:
    """ベンチマーク結果をプロットする。

    Returns:
        plotly.graph_objects.Figure: プロット結果。
    """
    with gzip.open(os.path.join(THIS_DIR, "bench.data"), mode="rb") as file:
        results = msgpack.unpack(file)

    data_list = []
    for measurement in results["measurements"]:
        if measurement["measurer_name"] != "Mean Processing Time":
            continue

        if measurement["case_name"] == "repeated_gmres":
            solver_name = f'Repeated GMRES (m={int(measurement["params"]["sub_dim"])})'
        elif measurement["case_name"] == "BiCGSTAB":
            solver_name = "BiCGstab"
        else:
            continue

        iterations = 0
        for output in measurement["custom_outputs"]:
            if output["name"] == "iterations":
                iterations = int(output["value"])

        data_list.append(
            {
                "Solver": solver_name,
                "Problem Dimension": int(measurement["params"]["dim"]),
                "Iterations": iterations,
                "Time [sec]": float(measurement["durations"]["stat"]["mean"]),
                "Std. Err. of Time [sec]": float(
                    measurement["durations"]["stat"]["standard_error"]
                ),
            }
        )

    data_frame = pandas.DataFrame(data_list)

    return px.line(
        data_frame,
        x="Problem Dimension",
        y="Time [sec]",
        error_y="Std. Err. of Time [sec]",
        color="Solver",
        line_dash="Solver",
        markers=True,
        log_x=True,
        log_y=True,
        title="Processing Time of Solvers of Sparse Linear Equations",
        template="plotly_white",
    )


def ode_runge_kutta_sparse_solvers_gmres() -> plotly.graph_objects.Figure:
    """ベンチマーク結果をプロットする。

    Returns:
        plotly.graph_objects.Figure: プロット結果。
    """
    with gzip.open(os.path.join(THIS_DIR, "bench.data"), mode="rb") as file:
        results = msgpack.unpack(file)

    data_list = []
    for measurement in results["measurements"]:
        if measurement["measurer_name"] != "Mean Processing Time":
            continue

        if measurement["case_name"] == "repeated_gmres":
            solver_name = f'Repeated GMRES (m={int(measurement["params"]["sub_dim"])})'
        else:
            continue

        iterations = 0
        for output in measurement["custom_outputs"]:
            if output["name"] == "iterations":
                iterations = int(output["value"])

        data_list.append(
            {
                "Solver": solver_name,
                "Problem Dimension": int(measurement["params"]["dim"]),
                "Iterations": iterations,
                "Time [sec]": float(measurement["durations"]["stat"]["mean"]),
                "Std. Err. of Time [sec]": float(
                    measurement["durations"]["stat"]["standard_error"]
                ),
            }
        )

    data_frame = pandas.DataFrame(data_list)

    return px.line(
        data_frame,
        x="Problem Dimension",
        y="Time [sec]",
        error_y="Std. Err. of Time [sec]",
        color="Solver",
        line_dash="Solver",
        markers=True,
        log_x=True,
        log_y=True,
        title="Processing Time of Solvers of Sparse Linear Equations",
        template="plotly_white",
    )
