"""ベンチマーク結果をプロットする。"""

import gzip
import os

import msgpack
import pandas
import plotly.express as px
import plotly.graph_objects

from num_anal_plots.plots.ode_common import MAIN_SOLVERS, SOLVER_TYPE_MAPPING

THIS_DIR = os.path.dirname(os.path.abspath(__file__))


def ode_pendulum_movement_auto_step_work_error() -> plotly.graph_objects.Figure:
    """ベンチマーク結果をプロットする。

    Returns:
        plotly.graph_objects.Figure: プロット結果。
    """
    with gzip.open(
        os.path.join(THIS_DIR, "pendulum_movement_problem.data"), mode="rb"
    ) as file:
        results = msgpack.unpack(file)
    data_frame = pandas.DataFrame(
        {
            "Solver": results["solver_list"],
            "Err. Tol.": results["tolerance_list"],
            "Error Rate": results["error_rate_list"],
            "Time [sec]": results["time_list"],
        }
    )

    data_frame = data_frame[data_frame["Solver"].isin(MAIN_SOLVERS)]

    return px.line(
        data_frame,
        x="Time [sec]",
        y="Error Rate",
        color="Solver",
        line_dash="Solver",
        hover_data=["Solver", "Err. Tol.", "Error Rate", "Time [sec]"],
        markers=True,
        log_x=True,
        log_y=True,
        title="Work-Error Diagram of ODE solvers for Pendulum Movement",
        template="plotly_white",
    )


def ode_pendulum_movement_auto_step_all_work_error() -> plotly.graph_objects.Figure:
    """ベンチマーク結果をプロットする。

    Returns:
        plotly.graph_objects.Figure: プロット結果。
    """
    with gzip.open(
        os.path.join(THIS_DIR, "pendulum_movement_problem.data"), mode="rb"
    ) as file:
        results = msgpack.unpack(file)
    data_frame = pandas.DataFrame(
        {
            "Solver": results["solver_list"],
            "Err. Tol.": results["tolerance_list"],
            "Error Rate": results["error_rate_list"],
            "Time [sec]": results["time_list"],
        }
    )

    data_frame["Solver Type"] = data_frame["Solver"].map(SOLVER_TYPE_MAPPING)

    figure = px.line(
        data_frame,
        x="Time [sec]",
        y="Error Rate",
        color="Solver",
        facet_row="Solver Type",
        line_dash="Solver",
        hover_data=["Solver", "Err. Tol.", "Error Rate", "Time [sec]"],
        markers=True,
        log_x=True,
        log_y=True,
        title="Work-Error Diagram of ODE solvers for Pendulum Movement",
        template="plotly_white",
    )
    figure.update_layout(height=800)
    return figure
