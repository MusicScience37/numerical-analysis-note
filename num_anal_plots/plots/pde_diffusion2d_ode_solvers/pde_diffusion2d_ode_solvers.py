"""ベンチマーク結果をプロットする。"""

import gzip
import os

import msgpack
import pandas
import plotly.express as px
import plotly.graph_objects

THIS_DIR = os.path.dirname(os.path.abspath(__file__))


def pde_diffusion2d_ode_solvers_work_error() -> plotly.graph_objects.Figure:
    """ベンチマーク結果をプロットする。

    Returns:
        plotly.graph_objects.Figure: プロット結果。
    """
    with gzip.open(
        os.path.join(THIS_DIR, "diffusion2d_dirichlet.data"), mode="rb"
    ) as file:
        results = msgpack.unpack(file)
    data_frame = pandas.DataFrame(
        {
            "Boundary Condition": ["Dirichlet"] * len(results["solver_list"]),
            "Solver": results["solver_list"],
            "Err. Tol.": results["tolerance_list"],
            "Error Rate": results["error_rate_list"],
            "Time [sec]": results["time_list"],
        }
    )
    with gzip.open(
        os.path.join(THIS_DIR, "diffusion2d_neumann.data"), mode="rb"
    ) as file:
        results = msgpack.unpack(file)
    data_frame = pandas.concat(
        [
            data_frame,
            pandas.DataFrame(
                {
                    "Boundary Condition": ["Neumann"] * len(results["solver_list"]),
                    "Solver": results["solver_list"],
                    "Err. Tol.": results["tolerance_list"],
                    "Error Rate": results["error_rate_list"],
                    "Time [sec]": results["time_list"],
                }
            ),
        ]
    )

    figure = px.line(
        data_frame,
        x="Time [sec]",
        y="Error Rate",
        color="Solver",
        line_dash="Solver",
        facet_row="Boundary Condition",
        hover_data=[
            "Boundary Condition",
            "Solver",
            "Err. Tol.",
            "Error Rate",
            "Time [sec]",
        ],
        markers=True,
        log_x=True,
        log_y=True,
        title="Work-Error Diagram of ODE solvers for 2D Diffusion Equation",
    )
    figure.update_layout(height=900)
    return figure
