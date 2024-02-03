"""ベンチマーク結果をプロットする。"""

import json
import os

import plotly.express as px
import plotly.graph_objects

THIS_DIR = os.path.dirname(os.path.abspath(__file__))


def ode_runge_kutta_gmres() -> plotly.graph_objects.Figure:
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
        if measurement["case_name"] != "repeated_gmres":
            continue

        iterations = 0
        for output in measurement["custom_outputs"]:
            if output["name"] == "iterations":
                iterations = int(output["value"])

        data_list.append(
            {
                "Subspace Dimension": int(measurement["params"]["sub_dim"]),
                "Problem Dimension": int(measurement["params"]["dim"]),
                "Iterations": iterations,
                "Time [sec]": float(measurement["durations"]["stat"]["mean"]),
            }
        )

    return px.line(
        data_list,
        x="Problem Dimension",
        y="Time [sec]",
        color="Subspace Dimension",
        line_dash="Subspace Dimension",
        markers=True,
        log_x=True,
        log_y=True,
        title="Processing Time of GMRES",
    )
