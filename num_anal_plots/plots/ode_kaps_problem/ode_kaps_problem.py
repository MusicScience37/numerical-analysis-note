"""ベンチマーク結果をプロットする。"""

import gzip
import os

import msgpack
import pandas
import plotly.express as px
import plotly.graph_objects

from num_anal_plots.plots.ode_common import MAIN_SOLVERS

THIS_DIR = os.path.dirname(os.path.abspath(__file__))


def load_data() -> pandas.DataFrame:
    """データを読み込む。

    Returns:
        pandas.DataFrame: データ。
    """
    with gzip.open(os.path.join(THIS_DIR, "kaps_problem0.data"), mode="rb") as file:
        results = msgpack.unpack(file)
    data_frame = pandas.DataFrame(
        {
            "Epsilon": ["1"] * len(results["solver_list"]),
            "Solver": results["solver_list"],
            "Err. Tol.": results["tolerance_list"],
            "Error Rate": results["error_rate_list"],
            "Time [sec]": results["time_list"],
        }
    )
    with gzip.open(os.path.join(THIS_DIR, "kaps_problem3.data"), mode="rb") as file:
        results = msgpack.unpack(file)
    data_frame = pandas.concat(
        [
            data_frame,
            pandas.DataFrame(
                {
                    "Epsilon": ["1e-3"] * len(results["solver_list"]),
                    "Solver": results["solver_list"],
                    "Err. Tol.": results["tolerance_list"],
                    "Error Rate": results["error_rate_list"],
                    "Time [sec]": results["time_list"],
                }
            ),
        ]
    )
    with gzip.open(os.path.join(THIS_DIR, "kaps_problem6.data"), mode="rb") as file:
        results = msgpack.unpack(file)
    data_frame = pandas.concat(
        [
            data_frame,
            pandas.DataFrame(
                {
                    "Epsilon": ["1e-6"] * len(results["solver_list"]),
                    "Solver": results["solver_list"],
                    "Err. Tol.": results["tolerance_list"],
                    "Error Rate": results["error_rate_list"],
                    "Time [sec]": results["time_list"],
                }
            ),
        ]
    )
    return data_frame


def ode_kaps_problem_work_error() -> plotly.graph_objects.Figure:
    """ベンチマーク結果をプロットする。

    Returns:
        plotly.graph_objects.Figure: プロット結果。
    """
    data_frame = load_data()

    data_frame = data_frame[data_frame["Solver"].isin(MAIN_SOLVERS)]

    figure = px.line(
        data_frame,
        x="Time [sec]",
        y="Error Rate",
        color="Solver",
        line_dash="Solver",
        facet_row="Epsilon",
        hover_data=["Solver", "Err. Tol.", "Error Rate", "Time [sec]"],
        markers=True,
        log_x=True,
        log_y=True,
        title="Work-Error Diagram of ODE solvers for Kaps' Problem",
        template="plotly_white",
    )
    figure.update_layout(height=900)
    return figure
