"""ベンチマーク結果をプロットする。"""

import gzip
import os

import msgpack
import pandas
import plotly.express as px
import plotly.graph_objects

THIS_DIR = os.path.dirname(os.path.abspath(__file__))


# アルゴリズムの実装用の名前を表示用の名前に変換する辞書
ALGORITHM_NAME_DICT = {
    "steepest_descent": "Steepest Descent",
    "downhill_simplex": "Downhill Simplex",
    "dfp_optimizer": "Quasi-Newton (DFP Formula)",
    "bfgs_optimizer": "Quasi-Newton (BFGS Formula)",
    "dividing_rectangles": "Dividing Rectangle",
}


def _load_data() -> pandas.DataFrame:
    with gzip.open(
        os.path.join(THIS_DIR, "rosenbrock_function.data"), mode="rb"
    ) as file:
        results = msgpack.unpack(file)

    data_list = []
    for measurement in results["measurements"]:
        if measurement["measurer_name"] != "Mean Processing Time":
            continue

        algorithm_implementation_name = measurement["case_name"]
        algorithm_name = ALGORITHM_NAME_DICT.get(algorithm_implementation_name)
        if algorithm_name is None:
            continue

        iterations = 0
        evaluations = 0
        for output in measurement["custom_outputs"]:
            if output["name"] == "iterations":
                iterations = int(output["value"])
            if output["name"] == "evaluations":
                evaluations = int(output["value"])

        data_list.append(
            {
                "Algorithm": algorithm_name,
                "Function": "Rosenbrock",
                "Iterations": iterations,
                "Function Evaluations": evaluations,
                "Time [sec]": float(measurement["durations"]["stat"]["mean"]),
                "Std. Err. of Time [sec]": float(
                    measurement["durations"]["stat"]["standard_error"]
                ),
            }
        )

    with gzip.open(os.path.join(THIS_DIR, "powell4_function.data"), mode="rb") as file:
        results = msgpack.unpack(file)

    for measurement in results["measurements"]:
        if measurement["measurer_name"] != "Mean Processing Time":
            continue

        algorithm_implementation_name = measurement["case_name"]
        algorithm_name = ALGORITHM_NAME_DICT.get(algorithm_implementation_name)
        if algorithm_name is None:
            continue

        iterations = 0
        evaluations = 0
        for output in measurement["custom_outputs"]:
            if output["name"] == "iterations":
                iterations = int(output["value"])
            if output["name"] == "evaluations":
                evaluations = int(output["value"])

        data_list.append(
            {
                "Algorithm": algorithm_name,
                "Function": "Powell4",
                "Iterations": iterations,
                "Function Evaluations": evaluations,
                "Time [sec]": float(measurement["durations"]["stat"]["mean"]),
                "Std. Err. of Time [sec]": float(
                    measurement["durations"]["stat"]["standard_error"]
                ),
            }
        )

    return pandas.DataFrame(data_list)


def opt_convex_difficult_functions_time() -> plotly.graph_objects.Figure:
    """ベンチマーク結果をプロットする。

    Returns:
        plotly.graph_objects.Figure: プロット結果。
    """
    data_frame = _load_data()

    return px.scatter(
        data_frame,
        x="Function",
        y="Time [sec]",
        error_y="Std. Err. of Time [sec]",
        color="Algorithm",
        hover_data=[
            "Algorithm",
            "Function",
            "Iterations",
            "Function Evaluations",
            "Time [sec]",
        ],
        log_y=True,
        title="Processing Time of Optimization of Sample Convex Functions",
        template="plotly_white",
    )


def opt_convex_difficult_functions_evaluations() -> plotly.graph_objects.Figure:
    """ベンチマーク結果をプロットする。

    Returns:
        plotly.graph_objects.Figure: プロット結果。
    """
    data_frame = _load_data()

    return px.scatter(
        data_frame,
        x="Function",
        y="Function Evaluations",
        color="Algorithm",
        hover_data=[
            "Algorithm",
            "Function",
            "Iterations",
            "Function Evaluations",
            "Time [sec]",
        ],
        log_y=True,
        title="Function Evaluations in Optimization of Sample Convex Functions",
        template="plotly_white",
    )
