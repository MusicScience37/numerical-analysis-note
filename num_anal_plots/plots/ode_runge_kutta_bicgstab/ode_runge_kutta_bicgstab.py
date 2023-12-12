"""ベンチマーク結果をプロットする。"""

import json
import os

import pandas
import plotly.express as px
import plotly.graph_objects

THIS_DIR = os.path.dirname(os.path.abspath(__file__))


def ode_runge_kutta_bicgstab() -> plotly.graph_objects.Figure:
    """ベンチマーク結果をプロットする。

    Returns:
        plotly.graph_objects.Figure: プロット結果。
    """
    with open(os.path.join(THIS_DIR, "result.json"), mode="r") as file:
        results = json.load(file)

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
            }
        )

    data_frame = pandas.DataFrame(data_list)
    data_frame = data_frame[
        (data_frame["Solver"] == "BiCGstab")
        | (data_frame["Solver"] == "Repeated GMRES (m=2)")
    ]

    return px.line(
        data_frame,
        x="Problem Dimension",
        y="Time [sec]",
        category_orders={"Solver": ["BiCGstab", "Repeated GMRES (m=2)"]},
        color="Solver",
        line_dash="Solver",
        log_x=True,
        log_y=True,
        title="Processing Time of BiCGstab Compared to GMRES",
    )
