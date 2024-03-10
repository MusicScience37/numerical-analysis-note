"""Jupyter でプロットを表示する。"""

from num_anal_plots.plots.plots import PLOT_INFO_DICT


def show_plot_in_jupyter(name: str, *, version: int = 1) -> None:
    """Jupyter でプロットを表示する。

    Args:
        name (str): プロットの名前。
        version (int): バージョン。
            myst-nb ライブラリのキャッシュで別のプロットと認識させるために適当な値を入れる。
    """
    info = PLOT_INFO_DICT[name]
    figure = info.figure_factory()
    figure.show(renderer="notebook_connected")
