"""ベンチマーク結果をプロットする。"""

import msgpack
import os

import pandas
import plotly.express as px

THIS_DIR = os.path.dirname(os.path.abspath(__file__))


SOLVERS = ["CG", "BiCGstab"]


def plot():
    """ベンチマーク結果をプロットする。"""

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
    fig = px.line(
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

    # PDF を出力させると MathJax の読み込み中の表示が画像内に出力されるため、
    # SVG で出力させたものを Inkscape で PDF 化している。
    fig.write_image(os.path.join(THIS_DIR, "bench.svg"))


if __name__ == "__main__":
    plot()
