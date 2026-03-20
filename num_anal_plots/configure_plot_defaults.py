"""Plotly のデフォルト設定を行う。"""

import ms37_designs.plotly_templates
import plotly.io


def configure_plot_defaults():
    """Plotly のデフォルト設定を行う。

    PDF と Jupyter の両方に必要な設定だけ記載する。
    """
    ms37_designs.plotly_templates.load_templates()
    plotly.io.templates.default = "ms37_white"
