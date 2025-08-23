"""Plotly のデフォルト設定を行う。"""

import plotly.graph_objects
import plotly.io


def configure_plot_defaults():
    """Plotly のデフォルト設定を行う。

    PDF と Jupyter の両方に必要な設定だけ記載する。
    """
    plotly.io.templates["num_anal_plot_overrides"] = (
        plotly.graph_objects.layout.Template(
            layout_xaxis={  # cspell: disable-line
                "showline": True,  # cspell: disable-line
                "linecolor": "rgb(36,36,36)",  # cspell: disable-line
                "gridcolor": "rgb(200,200,200)",  # cspell: disable-line
                "zerolinecolor": "rgb(200,200,200)",  # cspell: disable-line
                "ticks": "outside",
            },
            layout_yaxis={  # cspell: disable-line
                "showline": True,  # cspell: disable-line
                "linecolor": "rgb(36,36,36)",  # cspell: disable-line
                "gridcolor": "rgb(200,200,200)",  # cspell: disable-line
                "zerolinecolor": "rgb(200,200,200)",  # cspell: disable-line
                "ticks": "outside",
            },
            layout_colorway=[
                "#DA6212",
                "#3AB111",
                "#5B19D9",
                "#F61EAF",
                "#2EC1F3",
                "#E0B70C",
                "#80807F",
                "#825308",
                "#8F0C6F",
            ],
        )
    )
    plotly.io.templates.default = "plotly_white+num_anal_plot_overrides"
