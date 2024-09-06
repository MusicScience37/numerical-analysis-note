"""Jupyter でプロットを表示する。"""

import typing

from num_anal_plots.configure_plot_defaults import configure_plot_defaults
from num_anal_plots.plots.plots import PLOT_INFO_DICT


def _ignore(_: typing.Any) -> None:
    """変数を無視する。

    Args:
        _ (typing.Any): 無視する変数。
    """


def show_plot_in_jupyter(name: str, *, version: int = 1) -> None:
    """Jupyter でプロットを表示する。

    Args:
        name (str): プロットの名前。
        version (int): バージョン。
            myst-nb ライブラリのキャッシュで別のプロットと認識させるために適当な値を入れる。
    """
    _ignore(version)

    configure_plot_defaults()

    info = PLOT_INFO_DICT[name]
    figure = info.figure_factory()
    figure.show(renderer="notebook_connected")
