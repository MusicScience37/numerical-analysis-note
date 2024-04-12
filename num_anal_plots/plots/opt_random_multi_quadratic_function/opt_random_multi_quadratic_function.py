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
    "conjugate_gradient": "Conjugate Gradient",
    "dividing_rectangles": "Dividing Rectangle",
}


def _load_data() -> pandas.DataFrame:
    with gzip.open(os.path.join(THIS_DIR, "bench.data"), mode="rb") as file:
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
        iterations_stderr = 0
        evaluations = 0
        evaluations_stderr = 0
        for output in measurement["custom_stat_outputs"]:
            if output["name"] == "iterations":
                iterations = float(output["stat"]["mean"])
                iterations_stderr = float(output["stat"]["standard_error"])
            if output["name"] == "evaluations":
                evaluations = float(output["stat"]["mean"])
                evaluations_stderr = float(output["stat"]["standard_error"])

        data_list.append(
            {
                "Algorithm": algorithm_name,
                "Variable Dimension": int(measurement["params"]["dimension"]),
                "Iterations": iterations,
                "Std. Err. of Iterations": iterations_stderr,
                "Function Evaluations": evaluations,
                "Std. Err. of Function Evaluations": evaluations_stderr,
                "Time [sec]": float(measurement["durations"]["stat"]["mean"]),
                "Std. Err. of Time [sec]": float(
                    measurement["durations"]["stat"]["standard_error"]
                ),
            }
        )

    return pandas.DataFrame(data_list)


def opt_random_multi_quadratic_function_time() -> plotly.graph_objects.Figure:
    """ベンチマーク結果をプロットする。

    Returns:
        plotly.graph_objects.Figure: プロット結果。
    """
    data_frame = _load_data()

    return px.line(
        data_frame,
        x="Variable Dimension",
        y="Time [sec]",
        error_y="Std. Err. of Time [sec]",
        color="Algorithm",
        line_dash="Algorithm",
        hover_data=[
            "Algorithm",
            "Variable Dimension",
            "Iterations",
            "Function Evaluations",
            "Time [sec]",
        ],
        markers=True,
        log_x=True,
        log_y=True,
        title="Processing Time of Optimization of Random Quadratic Functions",
        template="plotly_white",
    )


def opt_random_multi_quadratic_function_evaluations() -> plotly.graph_objects.Figure:
    """ベンチマーク結果をプロットする。

    Returns:
        plotly.graph_objects.Figure: プロット結果。
    """
    data_frame = _load_data()

    return px.line(
        data_frame,
        x="Variable Dimension",
        y="Function Evaluations",
        error_y="Std. Err. of Function Evaluations",
        color="Algorithm",
        line_dash="Algorithm",
        hover_data=[
            "Algorithm",
            "Variable Dimension",
            "Iterations",
            "Function Evaluations",
            "Time [sec]",
        ],
        markers=True,
        log_x=True,
        log_y=True,
        title="Function Evaluations in Optimization of Random Quadratic Functions",
        template="plotly_white",
    )
