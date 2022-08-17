"""ベンチマーク結果をプロットする。"""

import json
import os

import plotly.express as px

THIS_DIR = os.path.dirname(os.path.abspath(__file__))


def plot():
    """ベンチマーク結果をプロットする。"""

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

    fig = px.line(
        data_list,
        x="Problem Dimension",
        y="Time [sec]",
        color="Subspace Dimension",
        line_dash="Subspace Dimension",
        log_y=True,
        title="Processing Time of GMRES",
    )

    # PDF を出力させると MathJax の読み込み中の表示が画像内に出力されるため、
    # SVG で出力させたものを Inkscape で PDF 化している。
    fig.write_image(os.path.join(THIS_DIR, "dimension-to-time.svg"))


if __name__ == "__main__":
    plot()
