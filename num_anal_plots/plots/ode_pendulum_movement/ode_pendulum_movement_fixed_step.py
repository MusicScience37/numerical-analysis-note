"""ベンチマーク結果をプロットする。"""

import gzip
import os

import msgpack
import pandas
import plotly.express as px
import plotly.graph_objects

THIS_DIR = os.path.dirname(os.path.abspath(__file__))


def ode_pendulum_movement_fixed_step_work_error() -> plotly.graph_objects.Figure:
    """ベンチマーク結果をプロットする。

    Returns:
        plotly.graph_objects.Figure: プロット結果。
    """
    with gzip.open(
        os.path.join(THIS_DIR, "pendulum_movement_problem_fixed_step.data"), mode="rb"
    ) as file:
        results = msgpack.unpack(file)
    data_frame = pandas.DataFrame(
        {
            "Solver": results["solver_list"],
            "Step Size": results["step_size_list"],
            "Error Rate": results["error_rate_list"],
            "Time [sec]": results["time_list"],
        }
    )

    return px.line(
        data_frame,
        x="Time [sec]",
        y="Error Rate",
        color="Solver",
        line_dash="Solver",
        hover_data=["Solver", "Step Size", "Error Rate", "Time [sec]"],
        markers=True,
        log_x=True,
        log_y=True,
        title="Work-Error Diagram of ODE solvers for Pendulum Movement",
        template="plotly_white",
    )
